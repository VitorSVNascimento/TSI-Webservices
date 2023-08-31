package vsvn.serverSocket.app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

import vsvn.serverSocket.model.Aluno;
import vsvn.serverSocket.model.Turma;

public class Server {

	public static void main(String[] args) {
		serverSocker();

	}

	public static void serverSocker() {
		
		Turma turma1 = new Turma(1,2022,
				new Aluno(20, 1234, "Vitor"),new Aluno(20, 12345, "Leticia"),new Aluno(20, 123, "Vinicius"),
				new Aluno(20, 123455, "João"),new Aluno(20, 1234, "Caren"));
		Turma turma2 = new Turma(1,2023,
				new Aluno(20, 1234, "Cassio"),new Aluno(20, 12345, "Cleiton"),new Aluno(20, 123, "Juvenal"),
				new Aluno(20, 123455, "Gilmara"),new Aluno(20, 1234, "Josival"));
		List<Turma> turmas = new ArrayList<Turma>();
		
		turmas.add(turma1);
		turmas.add(turma2);
		
		JSONObject json = Turma.turmasToJson(turmas);
		
		 try {
		      ServerSocket servidor = new ServerSocket(8000);
		      System.out.println("Servidor ouvindo a porta 8000");
		      while(true) {
		    	  
		        // o método accept() bloqueia a execução até que
		        // o servidor receba um pedido de conexão
		    	  
		        Socket cliente = servidor.accept();
		        System.out.println("Cliente conectado: " + cliente.getInetAddress().getHostAddress());
		        PrintWriter saida = new PrintWriter(cliente.getOutputStream(),true);
		        saida.flush();
		        saida.println(json.toJSONString());
		        
		        String retornoCliente = readMessage(cliente);
		        JSONObject jsonCliente = (JSONObject)JSONValue.parse(retornoCliente);
		        
		        System.out.println(jsonCliente.toJSONString());
		        
		        
		        saida.close();
		        cliente.close();
		      }
		    }
		    catch(Exception e) {
		       System.out.println("Erro: " + e.getMessage());
		    }
		

		
		
	}
	
	public static String readMessage(Socket cliente) {
		try(BufferedReader buffer = new BufferedReader(new InputStreamReader(cliente.getInputStream()))) {
			
			StringBuilder builder = new StringBuilder();
			String linha;
			
	        while ((linha = buffer.readLine()) != null) {
	            builder.append(linha);
	        }

			return builder.toString();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			
			e.printStackTrace();
			return null;
		}
			
		
	}

}
