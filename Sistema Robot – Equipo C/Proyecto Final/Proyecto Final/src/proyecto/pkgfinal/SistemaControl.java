/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author arian
 */
public class SistemaControl {

    private Modulo modulo;
    private SistemaComunicacion sistemaComunicacion;
    private SistemaControl destinoAccion;

    // Constructor vacío (sin dependencia de Modulo)
    public SistemaControl() {
        this.modulo = null;
        this.sistemaComunicacion = null;
        this.destinoAccion = null;
    }

    // Constructor que recibe un Modulo (para uso normal en los módulos)
    public SistemaControl(Modulo modulo) {
        this.modulo = modulo;
        this.sistemaComunicacion = null;
        this.destinoAccion = null;
    }

    public void setModulo(Modulo modulo) {
        this.modulo = modulo;
    }

    public void setSistemaComunicacion(SistemaComunicacion sistemaComunicacion) {
        this.sistemaComunicacion = sistemaComunicacion;
    }

    public void setDestinoAccion(SistemaControl destinoAccion) {
        this.destinoAccion = destinoAccion;
    }

    public boolean enviar_respuesta_accion(){
        if (modulo != null && !modulo.estaEncendido()) {
            System.out.println("SistemaControl: módulo apagado. No se puede enviar respuesta.");
            return false;
        }
        System.out.println("SistemaControl: Enviando respuesta.");
        if (sistemaComunicacion != null) {
            sistemaComunicacion.enviar_mensaje();
            return true;
        }
        return false;
    }
    

    public String[] gestionar_solucion(int codigoError) {
        if (modulo != null && !modulo.estaEncendido()) {
            return new String[]{"Módulo apagado. No se puede gestionar solución."};
        }
        String[] soluciones = {
            "Reintentar operación para código: " + codigoError,
            "Notificar al operador del módulo"
        };
        System.out.println("SistemaControl: Gestionando solución para error " + codigoError);
        return soluciones;
    }

    public void interpretar_mensaje(String mensaje, String robot) {
        if (modulo != null && !modulo.estaEncendido()) {
            System.out.println("SistemaControl: módulo apagado. No puede interpretar mensaje.");
            return;
        }
        System.out.println("SistemaControl interpreta mensaje: " + mensaje);
        enviar_respuesta_accion();
    }
}
