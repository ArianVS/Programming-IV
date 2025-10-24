/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author valentina
 */

public class Actuacion extends MEstatico {
    protected int N_actuadores;

    public Actuacion(int id, String referencia, String descripcion, int largo, int ancho, int profundidad, int N_actuadores) {
        super(id, referencia, descripcion, largo, ancho, profundidad);
        this.N_actuadores = N_actuadores;
    }

    public int realizar_accion(){
        return 0;
    }
}
