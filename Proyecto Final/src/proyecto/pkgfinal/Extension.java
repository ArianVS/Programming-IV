/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;
import java.util.Scanner;

/**
 *
 * @author Juan Felipe Ocampo G
 */

public class Extension extends MDinamico {
    Scanner scan = new Scanner(System.in);

    public Extension() {
        super(1, "Extensión", "Módulo de extensión por defecto", 0, 0, 0, 1);
        while (true) {
            try {
                System.out.println("Id asignado al módulo de extensión por default: " + this.id);
                System.out.println("Ingrese Largo, Ancho y profundidad separado por comas: ");
                String medidas = scan.nextLine();
                String[] dividido = medidas.split(",");
                this.largo = Integer.parseInt(dividido[0].trim());
                this.ancho = Integer.parseInt(dividido[1].trim());
                this.profundidad = Integer.parseInt(dividido[2].trim());

                System.out.println("Ingrese la referencia del módulo: ");
                this.referencia = scan.nextLine();

                System.out.println("Ingrese la descripcion del módulo: ");
                this.descripcion = scan.nextLine();

                break;
            } catch (Exception Error) {
                System.out.println("\nUltimo valor introducido incorrectamente, intente de nuevo");
            }
        }
    }

    @Override
    public int moverse(float[] movimiento, char[][] tablero, int posicionX, int posicionY) {
        if (!estaEncendido() || (robot != null && !robot.estaEncendido())) {
            System.out.println("No se puede mover: módulo o robot apagado.");
            return 0;
        }
        try {
            char robotChar = tablero[posicionY][posicionX];

            int pasos = (int) movimiento[0];
            int nuevaX = posicionX;
            int nuevaY = posicionY;

            switch (robotChar) {
                case 'A': // arriba
                    nuevaY -= pasos;
                    break;
                case 'B': // abajo
                    nuevaY += pasos;
                    break;
                case 'D': // derecha
                    nuevaX += pasos;
                    break;
                case 'I': // izquierda
                    nuevaX -= pasos;
                    break;
                case '1': // arriba-izquierda
                    nuevaY -= pasos;
                    nuevaX -= pasos;
                    break;
                case '2': // arriba-derecha
                    nuevaY -= pasos;
                    nuevaX += pasos;
                    break;
                case '3': // abajo-izquierda
                    nuevaY += pasos;
                    nuevaX -= pasos;
                    break;
                case '4': // abajo-derecha
                    nuevaY += pasos;
                    nuevaX += pasos;
                    break;
                default:
                    System.out.println("Dirección no válida.");
                    return 0;
            }

            if (nuevaX < 0 || nuevaX >= tablero[0].length || nuevaY < 0 || nuevaY >= tablero.length) {
                System.out.println("Se salió del tablero entonces return 0");
                return 0;
            }

            tablero[nuevaY][nuevaX] = robotChar;
            tablero[posicionY][posicionX] = ' ';

        } catch (ArrayIndexOutOfBoundsException Error) {
            System.out.println("Se salió del tablero entonces return 0");
            return 0;
        }
        return 1;
    }
}