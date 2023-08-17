package vsvn.serverSocket.model;

public class Aluno {
	private int idade,matricula;
	private String nome;
	
	
	
	public Aluno(int idade, int matricula, String nome) {
		this.idade = idade;
		this.matricula = matricula;
		this.nome = nome;
	}

	public int getIdade() {
		return idade;
	}
	
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public int getMatricula() {
		return matricula;
	}

	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}

	@Override
	public String toString() {
		return "Aluno [idade=" + idade + ", matricula=" + matricula + ", nome=" + nome + "]";
	}
	
	
}
