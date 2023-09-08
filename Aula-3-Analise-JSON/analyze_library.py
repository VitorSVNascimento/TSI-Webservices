from library_json import LIBRARY,QUESTIONS
import json
from typing import Dict
from functools import reduce
from collections import defaultdict

def get_books(library, category='any'):
    all = []
    if category == 'any':
        for category_books in library['livros']:
            for book in library['livros'][category_books]:
                all.append(book)
        return all
    else:
        if category in library['livros']:
            return library['livros'][category]
        return []  

def author_with_most_borrowed_books(all_books):
    author_borrowed_count = defaultdict(int)

    # Usamos defaultdict para inicializar automaticamente contagens para cada autor
    for book in all_books:
        author = book.get('autor', 'Autor Desconhecido')
        borrowed = book.get('emprestados', 0)
        author_borrowed_count[author] += borrowed

    # Encontra o autor com o máximo de livros emprestados
    if author_borrowed_count:
        max_author = max(author_borrowed_count, key=author_borrowed_count.get)
        return max_author
    else:
        return 'Nenhum livro emprestado encontrado.'

def book_with_most_copies(all_books):
    if not all_books:
        return 'Nenhum livro encontrado.'

    # Encontra o livro com o máximo de cópias
    max_copies_book = max(all_books, key=lambda x: x.get('copias', 0))

    return max_copies_book.get('titulo', 'Título Desconhecido')

def author_and_books_list(all_books):
    author_books_dict = {}

    # Preenche o dicionário com autores e seus livros
    for book in all_books:
        author = book.get('autor', 'Autor Desconhecido')
        title = book.get('titulo', 'Título Desconhecido')
        if author not in author_books_dict:
            author_books_dict[author] = []
        author_books_dict[author].append(title)

    # Cria a string formatada
    formatted_string = ''
    for author, books in author_books_dict.items():
        formatted_string += f"autor: {author}\n"
        formatted_string += f"livros: {', '.join(books)}\n\n"

    return formatted_string.strip()

def category_with_most_books(library_data):
    categories = library_data.get('livros', {})
    if not categories:
        return 'Nenhuma categoria encontrada.'

    max_category_count = max(len(category_books) for category_books in categories.values())
    most_categories = [category for category, category_books in categories.items() if len(category_books) == max_category_count]

    if not most_categories:
        return 'Nenhuma categoria encontrada.'
    elif len(most_categories) == 1:
        return most_categories[0]
    else:
        return ', '.join(most_categories)

def book_with_longest_title(all_books):
    if not all_books:
        return 'Nenhum livro encontrado.'

    max_title_length = max(len(book.get('titulo', '')) for book in all_books)
    longest_title_books = [book for book in all_books if len(book.get('titulo', '')) == max_title_length]

    if not longest_title_books:
        return 'Nenhum livro encontrado.'
    elif len(longest_title_books) == 1:
        return longest_title_books[0].get('titulo', 'Título Desconhecido')
    else:
        return ', '.join(book.get('titulo', 'Título Desconhecido') for book in longest_title_books)

def author_with_shortest_name(all_books):
    if not all_books:
        return 'Nenhum autor encontrado.'

    authors = set(book.get('autor', 'Autor Desconhecido') for book in all_books)
    shortest_author_name = min(authors, key=len)

    return shortest_author_name

def get_responses(library:Dict) -> list:
    responses = []
    all_books = get_books(library)
    responses.append(library['informacao']['nome'])
    responses.append(len(library['informacao']['telefones']))
    responses.append(len(get_books(library,'autoajuda')))
    responses.append(len(all_books))
    responses.append(sum(book['copias'] for book in all_books)) 
    responses.append(sum(book['emprestados'] for book in get_books(library,'romance')))
    responses.append(author_with_most_borrowed_books(all_books))
    responses.append(book_with_most_copies(all_books))
    responses.append(author_and_books_list(all_books))
    responses.append(category_with_most_books(library))
    responses.append(book_with_longest_title(all_books))
    responses.append(author_with_shortest_name(all_books))

    return responses

def show_results(results):
    for question,response in results:
        print(f'{question}:\n\t{response}')

def analyze_library():
    library = json.loads(LIBRARY)
    responses = get_responses(library)
    show_results(zip(QUESTIONS,responses))

if __name__ == '__main__':
    analyze_library()