public class TesteContador {
    
    public static void main(String args[]) {

        Contador thread1 = new Contador("Thread1");
        Contador thread2 = new Contador("Thread2");

        thread1.start();
        thread2.start();

    }

}

public class Contador extends Thread implements Runnable {

    private String nome;

    public Contador(String nome) {
        this.nome = nome;
    }

    public void run() {
        for (int i = 0; i < 11; i++) {
            System.out.println(this.nome + " - " + i);
        }
    }

}