package vsvn.serverSocket.model;

import java.util.ArrayList;
import java.util.List;

public class Turma {

	private int id,ano;
	private List<Aluno> alunos;
	
	public Turma(int id,int ano) {
		this(id,ano,null);
	}
	
	public Turma(int id,int ano,Aluno... alunos) {
		this.id = id;
		this.ano = ano;
		
		this.alunos = new ArrayList<Aluno>();
		if(alunos != null) {
			for(Aluno a: alunos)
				adicionarAluno(a);
		}
			
	}
	
	public List<Aluno> obterAlunos(){
		return alunos;
	}
	
	public Turma adicionarAluno(Aluno aluno) {
		alunos.add(aluno);
		return this;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getAno() {
		return ano;
	}

	public void setAno(int ano) {
		this.ano = ano;
	}

	public List<Aluno> getAlunos() {
		return alunos;
	}

	public void setAlunos(List<Aluno> alunos) {
		this.alunos = alunos;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		
		builder.append(String.format("Turma %d (%d)\n", id,ano));
		for(Aluno aluno : alunos) {
			builder.append((String.format("%s\n", aluno.toString())));
		}
		return builder.toString();
	}
	
	
	
	
	
	
}
