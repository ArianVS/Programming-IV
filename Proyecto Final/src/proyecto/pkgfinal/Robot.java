/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author arian
 */
import java.util.ArrayList;
import java.util.List;

public class Robot {
    private String serie;
    private String alias;
    private String descripcion;
    private int estado = 0; // 0 = apagado, 1 = encendido

    private List<Modulo> modulos;

    public Robot(String serie, String alias, String descripcion) {
        this.serie = serie;
        this.alias = alias;
        this.descripcion = descripcion;
        this.modulos = new ArrayList<>();
    }

    public void agregarModulo(Modulo modulo) {
        modulo.setRobot(this);
        modulos.add(modulo);
    }

    public void encender() {
        estado = 1;
        System.out.println("Robot " + alias + " encendido.");
        for (Modulo m : modulos) {
            m.encender();
        }
    }

    public void apagar() {
        estado = 0;
        System.out.println("Robot " + alias + " apagado.");
        for (Modulo m : modulos) {
            m.apagar();
        }
    }

    public boolean estaEncendido() {
        return estado == 1;
    }

    public String getAlias() {
        return alias;
    }
}