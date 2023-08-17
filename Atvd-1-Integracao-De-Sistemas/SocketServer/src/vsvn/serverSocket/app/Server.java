package vsvn.serverSocket.app;

import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

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
		Turma turma2 = new Turma(1,2022,
				new Aluno(20, 1234, "Cassio"),new Aluno(20, 12345, "Cleiton"),new Aluno(20, 123, "Juvenal"),
				new Aluno(20, 123455, "Gilmara"),new Aluno(20, 1234, "Josival"));
		StringBuilder builder = new StringBuilder();
		builder.append(turma1).append(turma2);
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
		        saida.println(builder.toString());
		        
		        
		        saida.close();
		        cliente.close();
		      }
		    }
		    catch(Exception e) {
		       System.out.println("Erro: " + e.getMessage());
		    }
		

		//List<Turma> turmas = new ArrayList();
		
		//turma
		
		
		
	}

}
