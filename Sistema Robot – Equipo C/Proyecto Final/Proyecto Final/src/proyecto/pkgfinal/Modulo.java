/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;
/**
 *
 * @author Juan Felipe Ocampo G
 */
public abstract class Modulo {
    protected int id;
    protected int largo, ancho, profundidad;
    protected String referencia, descripcion;
    protected int estado = 0; // 0 = apagado, 1 = encendido

    protected SistemaControl sisControl;
    protected SistemaComunicacion sisComunicacion;
    protected Robot robot; // Dependencia al robot padre

    public Modulo(int id, String referencia, String descripcion, int largo, int ancho, int profundidad) {
        this.id = id;
        this.referencia = referencia;
        this.descripcion = descripcion;
        this.largo = largo;
        this.ancho = ancho;
        this.profundidad = profundidad;

        this.sisControl = new SistemaControl(this);
        this.sisComunicacion = new SistemaComunicacion(sisControl);
    }

    public void setRobot(Robot robot) {
        this.robot = robot;
    }

    public void encender() {
        estado = 1;
        System.out.println("Módulo " + referencia + " encendido.");
    }

    public void apagar() {
        estado = 0;
        System.out.println("Módulo " + referencia + " apagado.");
    }

    public boolean estaEncendido() {
        return estado == 1;
    }

    public boolean enviar_respuesta_accion(){
        if (!estaEncendido()) {
            System.out.println("Módulo " + referencia + " está apagado. No puede enviar respuesta.");
            return false;
        }
        return sisControl.enviar_respuesta_accion();
    }

    public String[] gestionar_solucion(int codigoError) {
        if (!estaEncendido()) {
            System.out.println("Módulo " + referencia + " está apagado. No puede gestionar solución.");
            return new String[]{"Módulo apagado. No se puede gestionar solución."};
        }
        return sisControl.gestionar_solucion(codigoError);
    }
    
    protected static void imprimirTablero(char[][] tablero) {
        int SIZE = tablero.length;
        // Imprimir índices de columnas
        System.out.print("   ");
        for (int x = 0; x < SIZE; x++) {
            System.out.print(x + " ");
        }
        System.out.println();

        // Imprimir filas con índice
        for (int y = 0; y < SIZE; y++) {
            System.out.print(y + " |");
            for (int x = 0; x < SIZE; x++) {
                System.out.print(tablero[y][x] + " ");
            }
            System.out.println();
        }
    }
}