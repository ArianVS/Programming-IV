/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author arian
 */
public class Usuario {
    private int id;
    private String alias;
    private String tipo;

    private Robot robot;
    private SistemaComunicacion sistemaComunicacion;

    public Usuario(int id, String alias, String tipo, Robot robot) {
        this.id = id;
        this.alias = alias;
        this.tipo = tipo;
        this.robot = robot;
    }

    public void setSistemaComunicacion(SistemaComunicacion sistemaComunicacion) {
        this.sistemaComunicacion = sistemaComunicacion;
    }

    public String[] enviar_mensaje(int x, int y) {
        if (x < 0 || x >= 10 || y < 0 || y >= 10) {
            System.out.println("Coordenadas fuera de los límites de la matriz 10x10.");
            return new String[]{};
        }
        String[] coordenadas = {x + "," + y};
        System.out.println("Usuario " + alias + " envía coordenada: " + coordenadas[0]);
        if (sistemaComunicacion != null) {
            sistemaComunicacion.recibir_mensaje(coordenadas);
        }
        return coordenadas;
    }

    public void recibir_mensaje(String[] mensajes) {
        System.out.println("Usuario " + alias + " recibió los siguientes mensajes:");
        for (String msg : mensajes) {
            System.out.println("> " + msg);
        }
    }

    public void enciendeA() {
        System.out.println("Usuario " + alias + " enciende al robot.");
        robot.encender();
    }

    public void apagaA() {
        System.out.println("Usuario " + alias + " apaga al robot.");
        robot.apagar();
    }
}