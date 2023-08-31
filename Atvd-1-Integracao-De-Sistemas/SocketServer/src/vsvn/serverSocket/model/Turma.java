package vsvn.serverSocket.model;

import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

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
	
	
	   public JSONObject toJson() {
	        JSONObject turmaJson = new JSONObject();
	        turmaJson.put("id", id);
	        turmaJson.put("ano", ano);

	        JSONArray alunosJson = new JSONArray();
	        for (Aluno aluno : alunos) {
	            JSONObject alunoJson = new JSONObject();
	            alunoJson.put("nome", aluno.getNome());
	            alunoJson.put("idade", aluno.getIdade());
	            alunoJson.put("matricula", aluno.getMatricula());
	            // Adicione mais campos do aluno aqui, se necessário
	            alunosJson.add(alunoJson);
	        }
	        turmaJson.put("alunos", alunosJson);

	        return turmaJson;
	    }
	   
	    public static JSONObject turmasToJson(List<Turma> turmas) {
	        JSONArray turmasJson = new JSONArray();
	        for (Turma turma : turmas) {
	            turmasJson.add(turma.toJson());
	        }
	        JSONObject result = new JSONObject();
	        result.put("turmas", turmasJson);
	        return result;
	    }
	
	
}
