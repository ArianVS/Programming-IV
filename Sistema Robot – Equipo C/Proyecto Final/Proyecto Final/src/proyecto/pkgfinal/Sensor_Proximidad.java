/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author valentina
 */
public class Sensor_Proximidad extends Percepcion {
    
    public Sensor_Proximidad(int id, String referencia, String descripcion,int largo, int ancho, int profundidad, int distanciaMaxima) {
        super(id, referencia, descripcion, largo, ancho, profundidad, 1);
    }

    @Override  
    public Object captarInformacion(char[][] tablero, int x, int y, char direccion){
        System.out.println("Captando información de proximidad...");

        int nuevoX = x;
        int nuevoY = y;

        // Determinar la dirección y calcular la nueva posición
        switch (direccion) {
            case 'A': nuevoY -= 1; break;             // Arriba
            case 'B': nuevoY += 1; break;             // Abajo
            case 'I': nuevoX -= 1; break;             // Izquierda
            case 'D': nuevoX += 1; break;             // Derecha
            case '1': nuevoY -= 1; nuevoX -= 1; break; // Diagonal arriba izquierda
            case '2': nuevoY -= 1; nuevoX += 1; break; // Diagonal arriba derecha
            case '3': nuevoY += 1; nuevoX -= 1; break; // Diagonal abajo izquierda
            case '4': nuevoY += 1; nuevoX += 1; break; // Diagonal abajo derecha
            default:
                System.out.println("Direccion invalida: " + direccion);
                return 'X';
        }

        // Verificar que la nueva posición esté dentro de los límites
        if (nuevoY < 0 || nuevoY >= tablero.length || nuevoX < 0 || nuevoX >= tablero[0].length) {
            return 'X'; // Fuera del tablero
        }

        // Retornar el carácter en la posición deseada
        return tablero[nuevoY][nuevoX];
    }

    
    @Override
    public int procesarDatos(Object datos) {
        if (datos == null) {
            System.out.println("No hay datos de proximidad para procesar");
            return -1;
        }
    
        char contenido = (char) datos;
        System.out.println("Procesando datos de proximidad...");
        
        if (contenido == 'X' || contenido == 'M') {
            System.out.println("Obstáculo detectado");
            return 1;
        }
        
        return 0; // No hay obstáculo
    }
    
    public void procesarIdentificacion(String tipo) {
        System.out.println("Identificación del obstáculo: " + tipo);
        if ("Mascota".equals(tipo)) {
            System.out.println("¡Atención! Hay una mascota en la ruta.");
        } else {
            System.out.println("Obstáculo genérico detectado.");
        }
    }


    //Calcula la posición frontal según la dirección
    private int[] PosicionFrente(int x, int y, char direccion) {
        switch (direccion) {
            case 'A': return new int[]{x, y-1}; // Arriba
            case 'B': return new int[]{x, y+1}; // Abajo
            case 'I': return new int[]{x-1, y}; // Izquierda
            case 'D': return new int[]{x+1, y}; // Derecha
            default: return new int[]{x, y};    // Posición actual
        }
    }
    
}

