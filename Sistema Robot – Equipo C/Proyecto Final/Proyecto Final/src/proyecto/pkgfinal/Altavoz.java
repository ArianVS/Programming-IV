/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author valentina
 */
public class Altavoz extends Actuacion {
    
    public Altavoz(int id, String referencia, String descripcion,int largo, int ancho, int profundidad, int N_actuadores) {
        super(id, referencia, descripcion, largo, ancho, profundidad, 1);
    }
    
    public void emitirSonido(String tipoSonido) {
        System.out.println("Altavoz emitiendo sonido: " + tipoSonido);
    }

    @Override
    public int realizar_accion() {
        System.out.println("Emitiendo sonido desde el altavoz.");
        return 1;
    }
}
