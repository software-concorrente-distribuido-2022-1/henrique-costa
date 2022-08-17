public class Deposito {
    private int items = 0;
    private int capacidade = 5;
    private boolean podeRetirar = false;
    private boolean podeColocar = true;
    
    public synchronized int retirar() {

        if (!podeRetirar) {
            System.out.println("[ESPERA] Consumidor esperando para retirar...\n");
            try {
                wait();
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }
        }

        if (items > 0) {

            items--;
            System.out.println("[RETIRADA] Caixa retirada: Sobram "+items+" caixas");

            podeColocar = true;

        }

        if (items == 0) {
            podeRetirar = false;
        }

        System.out.println("[FINAL] Consumidor terminou de retirar. podeRetirar = "+podeRetirar+"; podeColocar = "+podeColocar+'\n');

        notify();
        return 0;

    }

    public synchronized int colocar () {

        if (!podeColocar) {
            System.out.println("[ESPERA] Produtor esperando para colocar...\n");
            try {
                wait();
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }
        }

        if (items < capacidade) {

            items++;
            System.out.println("[ARMAZENADA] Caixa armazenada: Passaram a ser "+items+" caixas");

            podeRetirar = true;

        }

        if (items == capacidade) {
            podeColocar = false;
        }

        System.out.println("[FINAL] Produtor terminou de colocar. podeRetirar = "+podeRetirar+"; podeColocar = "+podeColocar+'\n');

        notify();
        return 0;

    }

    public static void main(String[] args) {

        Deposito dep = new Deposito();
        Produtor prod = new Produtor(dep, 2);
        Consumidor cons = new Consumidor(dep, 1);
        Produtor prod1 = new Produtor(dep, 1);
        Consumidor cons1 = new Consumidor(dep, 5);

        prod.start();
        cons.start();
        prod1.start();
        cons1.start();

    }

}

public class Produtor extends Thread implements Runnable {

    private Deposito dep;
    private int tempo;

    public Produtor(Deposito d, int t){
        this.dep = d;
        this.tempo = t;
    }

    public void run() {

        while (true) {

            try {
                Thread.sleep(tempo*1000);
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }

            dep.colocar();

        }

    }

}

public class Consumidor extends Thread implements Runnable {

    private Deposito dep;
    private int tempo;

    public Consumidor(Deposito d, int t){
        this.dep = d;
        this.tempo = t;
    }

    public void run() {

        while (true) {

            try {
                Thread.sleep(tempo*1000);
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }

            dep.retirar();

        }

    }

}