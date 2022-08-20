/* -------------------------------------------------------------- */
/* Programa: Cliente                                              */
/* Autor: Sergio Teixeira de Carvalho                             */
/* Linguagem Utilizada: Java (JDK 1.1)                            */
/*                                                                */
/* Funcoes:                                                       */
/*      - permite estabelecimento de uma conexao TCP com          */
/*      a porta 80 (default) de um host fornecido;                */
/*      - pede como entrada uma Mensagem                          */
/*                                                                */
/* Uso: $ java ClienteSimples NomeDoHost Mensagem [porta]         */
/*                                                                */
/* -------------------------------------------------------------- */

import java.io.*;       //Package de classes para manipulacao de E/S
import java.net.*;      //Package de classes para manipulacao de Sockets, IP, etc
import java.util.Scanner;

public class ClienteSimples {
    public static void main (String[] args) throws IOException {
    
        /* ---declaracao dos objetos utilizados--- */
        
        final int portaDefault = 5000;    //Definicao da porta default
        
        String nomeHost = null;         //Nome do host para conexao
        int porta = portaDefault;       //Porta para conexao
        
        Socket sock = null;     //Declaracao de objeto da classe Socket 
        
        PrintWriter saida = null;       //Fluxo de saida
        BufferedReader entrada = null;//Fluxo de entrada
        String linhaResposta = null;  //Linha de resposta do host
        
        
        /* ---tratamento dos argumentos--- */
        
        if ((args.length == 1) || (args.length == 2)){
            nomeHost = args[0];     //Host e' 1o. argumento
            if (args.length == 2) {porta = Integer.parseInt(args[1]);}
            //Porta fornecida como argumento sobrepoe porta default
        }
        else {  //Fornecimento erroneo dos argumentos
            System.out.println("\n\nUso Correto: ClienteSimples NomeDoHost [porta]\n\n");
            System.exit(1);
        }
        
        try {
            sock = new Socket(nomeHost, porta);  
            //Objeto sock criado atraves do construtor Socket
            //adequado a uma conexao TCP confiavel (stream).
            //Corresponde as instrucoes socket() e connect() 
            
            saida = new PrintWriter(sock.getOutputStream(), true);
            //Prepara saida para envio posterior da PDU
            
            entrada = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            //Prepara entrada para recepcao de mensagens do host
        }
        catch(UnknownHostException e) {
            System.err.println("\n\nHost nao encontrado!\n");
            System.out.println("\nUso: ClienteSimples NomeDoHost [porta]\n\n");
            System.exit(1);
        }
        catch(java.io.IOException e) {
            System.err.println("\n\nConexao com Host nao pode ser estabelecida.\n");
            System.out.println("\nUso: ClienteSimples NomeDoHost [porta]\n\n");
            System.exit(1); 
        }
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Nome: ");
        String name = scanner.nextLine().strip();

        if (name.length() > 0) {
            System.out.println("\nNome inválido\n\n");
            System.exit(1);
        }
        
        System.out.println("Sexo (o/operador ou p/programador): ");
        String sex = scanner.nextLine().strip();
        
        if (!sex.equalsIgnoreCase("m") || !sex.equalsIgnoreCase("f")) {
            System.out.println("\nSexo inválido\n\n");
            System.exit(1);
        }
        
        System.out.println("Idade: ");
        Integer salary = scanner.nextInt();
        
        if (salary <= 0) {
            System.out.println("\nIdade inválida\n\n");
            System.exit(1);
        }
        
        scanner.close();
        
        String json = "{\"name\": \""+name+"\", \"sex\": \""+sex+"\", \"age\": "+salary.toString()+"}";
        
        saida.println(json);

        linhaResposta = entrada.readLine();
        while (linhaResposta != null) {
            System.out.println(linhaResposta);
            linhaResposta = entrada.readLine();
        }

        sock.close();
    }
}
