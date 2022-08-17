public class ExecutaThread {
    
    public static void main(String args[]) {
        ThreadSimples simples = new ThreadSimples();
        simples.start();
    }

}

public class ThreadSimples extends Thread {

    public void run() {
        System.out.println("Hello from a thread!");
    }

}