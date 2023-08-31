import socket
import json
import random

HOST = '127.0.0.1'
PORT = 8000
BUFFER_SIZE = 1024

def get_turmas(json_data):
    return json_data["turmas"]

def get_alunos(turma):
    return turma['alunos']

def sortear_lider(turma):
    alunos_json = get_alunos(turma)
    return random.choice(alunos_json)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

dados = []

while True:
    data = client.recv(BUFFER_SIZE)
    if not data:
        break

    dados.append(data)
    if len(data) < BUFFER_SIZE:
        break

print(dados)
json_data = json.loads(dados[-1].decode())
turmas = get_turmas(json_data)

sorteio = {}
for turma in turmas:
    sorteio[turma['ano']] = sortear_lider(turma)
print('chegou')
client.send(json.dumps(sorteio).encode())


client.close()
