/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author Juan Felipe Ocampo G
 */
public abstract class MDinamico extends Modulo {
    private int Nmotores;

    public MDinamico(int id, String referencia, String descripcion, int largo, int ancho, int profundidad, int Nmotores) {
        super(id, referencia, descripcion, largo, ancho, profundidad);
        this.Nmotores = Nmotores;
    }

    public int getNmotores() {
        return Nmotores;
    }

    public void setNmotores(int Nmotores) {
        this.Nmotores = Nmotores;
    }

    // Movimiento: retorna 1 si éxito, 0 si sale del tablero o falla
    public abstract char[][] moverse(float[] movimiento, char[][] tablero, int posicionX, int posicionY);
    // En moverse: posicion 0 para movimiento recto y 1 para grados de rotación
}

