import java.util.Arrays;

public class Orden {
    private final int idOrden;
    private Computadora computadora[]; // Arreglo de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadoras;

    // Constructor vacío
    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
    }

    // Método para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora) {
        if (this.contadorComputadoras < Orden.MAX_COMPUTADORAS) {
            this.computadora[this.contadorComputadoras++] = computadora;
        } else {
            System.out.println("No se pueden agregar más computadoras a la orden.");
        }
    }

    public void mostrarOrden() {
        System.out.println("Orden ID: " + this.idOrden);
        System.out.println("Computadoras en la orden:");
        for (int i = 0; i < this.contadorComputadoras; i++) {
            System.out.println(this.computadora[i]);
        }
    }

    public int getIdOrden() {
        return idOrden;
    }

    public Computadora[] getComputadora() {
        return computadora;
    }

    public void setComputadora(Computadora[] computadora) {
        this.computadora = computadora;
    }

    public static int getContadorOrdenes() {
        return contadorOrdenes;
    }

    public static void setContadorOrdenes(int contadorOrdenes) {
        Orden.contadorOrdenes = contadorOrdenes;
    }

    public static int getMaxComputadoras() {
        return MAX_COMPUTADORAS;
    }

    public int getContadorComputadoras() {
        return contadorComputadoras;
    }

    public void setContadorComputadoras(int contadorComputadoras) {
        this.contadorComputadoras = contadorComputadoras;
    }

    @Override
    public String toString() {
        return "Orden [idOrden=" + idOrden + ", computadora=" + Arrays.toString(computadora) + ", contadorComputadoras="
                + contadorComputadoras + "]";
    }


    
}