/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author valentina
 */
// Clase Sensor que agrega Camara y SensorProximidad
public class Sensor {
    private int id;
    private String tipo;
    private String descripcion;

    // Agregación
    private Camara camara;
    private Sensor_Proximidad sensorProximidad;

    public Sensor(int id, String tipo, String descripcion, Camara camara, Sensor_Proximidad sensorProximidad) {
        this.id = id;
        this.tipo = tipo;
        this.descripcion = descripcion;
        this.camara = camara;
        this.sensorProximidad = sensorProximidad;
    }

    public Object captarInformacion(char[][] tablero, int x, int y, char direccion) {
        Object infoProx = sensorProximidad.captarInformacion(tablero, x, y, direccion);
        return " Proximidad: " + infoProx;
    }

}



