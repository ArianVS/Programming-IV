/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author arian
 */
public class SistemaComunicacion {
    private SistemaControl sistemaControl;
    private Usuario usuario;

    public SistemaComunicacion(SistemaControl sistemaControl) {
        this.sistemaControl = sistemaControl;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public void recibir_mensaje(String[] mensajes, String robot, tablero) {
        System.out.println("SistemaComunicacion recibió " + mensajes.length + " mensaje(s).");
        for (String mensaje : mensajes) {
            sistemaControl.interpretar_mensaje(mensaje, robot);
        }
    }

    public String[] enviar_mensaje() {
        String[] respuestas = {"Acción completada", "Sin errores detectados"};
        System.out.println("SistemaComunicacion: enviando respuesta...");
        if (usuario != null) {
            usuario.recibir_mensaje(respuestas);
        } else {
            System.out.println("No hay usuario conectado para recibir la respuesta.");
        }
        return respuestas;
    }

    public void recibirMensajeDesdeUsuario(String mensaje, String robot) {
        recibir_mensaje(new String[]{mensaje}, robot);
    }
}
