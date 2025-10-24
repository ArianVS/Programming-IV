/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author valentina
 */

public abstract class Percepcion extends MEstatico {
    protected int N_Sensores;
    protected Camara camara;

    public void setCamara(Camara camara) {
        this.camara = camara;
    }


    public Percepcion(int id, String referencia, String descripcion, int largo, int ancho, int profundidad, int N_Sensores) {
        super(id, referencia, descripcion, largo, ancho, profundidad);
        this.N_Sensores = N_Sensores;
    }

    public abstract int procesarDatos(Object objeto);
    public abstract Object captarInformacion(char[][] tablero, int x, int y, char direccion);
    
    public void analizarEntorno(char[][] tablero, int x, int y, char direccion) {
        Object datos = captarInformacion(tablero, x, y, direccion);
        int resultado = procesarDatos(datos);

        if (resultado == 1 && this instanceof Sensor_Proximidad && camara != null) {
            char contenido = (char) datos;
            //String tipo = camara.identificarObstaculo(contenido);
            //((Sensor_Proximidad) this).procesarIdentificacion(tipo);
            //mientras reviso que hacer
        }
    }

    
}

 