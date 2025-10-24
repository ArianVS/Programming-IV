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

public class Helicoidal extends MDinamico {
    private Scanner scan = new Scanner(System.in);

    public Helicoidal() {
        super(3, "Helicoidal", "Módulo helicoidal por defecto", 0, 0, 0, 2);
        while (true) {
            try {
                System.out.println("Id asignado al módulo helicoidal por default: " + this.id);

                System.out.println("Ingrese Largo, Ancho y profundidad separado por comas: ");
                String medidas = scan.nextLine();
                String[] dividido = medidas.split(",");
                this.largo = Integer.parseInt(dividido[0].trim());
                this.ancho = Integer.parseInt(dividido[1].trim());
                this.profundidad = Integer.parseInt(dividido[2].trim());

                System.out.println("Ingrese la referencia del módulo: ");
                this.referencia = scan.nextLine();

                System.out.println("Ingrese la descripción del módulo: ");
                this.descripcion = scan.nextLine();

                break;
            } catch (Exception e) {
                System.out.println("\nÚltimo valor introducido incorrectamente, intente de nuevo.");
            }
        }
    }

    @Override
    public int moverse(float[] movimiento, char[][] tablero, int posicionX, int posicionY) {
        // Verificar estado
        if (!estaEncendido() || (robot != null && !robot.estaEncendido())) {
            System.out.println("No se puede mover: módulo o robot apagado.");
            return 0;
        }

        try {
            // Obtener orientación actual y girar según movimiento[1]
            char robotChar = tablero[posicionY][posicionX];

            if (movimiento[1] == 0.0f) {
                tablero[posicionY][posicionX] = 'A'; // Arriba
                robotChar = 'A';
            } else if (movimiento[1] == 90.0f) {
                tablero[posicionY][posicionX] = 'D'; // Derecha
                robotChar = 'D';
            } else if (movimiento[1] == -90.0f) {
                tablero[posicionY][posicionX] = 'I'; // Izquierda
                robotChar = 'I';
            } else if (movimiento[1] == 180.0f || movimiento[1] == -180.0f) {
                tablero[posicionY][posicionX] = 'B'; // Abajo
                robotChar = 'B';
            } else if (movimiento[1] < 0.0f && movimiento[1] > -90.0f) {
                tablero[posicionY][posicionX] = '1'; // Arriba-izquierda
                robotChar = '1';
            } else if (movimiento[1] > 0.0f && movimiento[1] < 90.0f) {
                tablero[posicionY][posicionX] = '2'; // Arriba-derecha
                robotChar = '2';
            } else if (movimiento[1] < -90.0f && movimiento[1] > -180.0f) {
                tablero[posicionY][posicionX] = '3'; // Abajo-izquierda
                robotChar = '3';
            } else if (movimiento[1] > 90.0f && movimiento[1] < 180.0f) {
                tablero[posicionY][posicionX] = '4'; // Abajo-derecha
                robotChar = '4';
            } else {
                System.out.println("Movimiento inválido (>180°), no se mueve.");
                return 0;
            }

            // Calcular nueva posición según robotChar y pasos (movimiento[0])
            int pasos = (int) movimiento[0];
            int nuevaX = posicionX;
            int nuevaY = posicionY;

            switch (robotChar) {
                case 'A':
                    nuevaY -= pasos;
                    break;
                case 'B':
                    nuevaY += pasos;
                    break;
                case 'D':
                    nuevaX += pasos;
                    break;
                case 'I':
                    nuevaX -= pasos;
                    break;
                case '1':
                    nuevaY -= pasos;
                    nuevaX -= pasos;
                    break;
                case '2':
                    nuevaY -= pasos;
                    nuevaX += pasos;
                    break;
                case '3':
                    nuevaY += pasos;
                    nuevaX -= pasos;
                    break;
                case '4':
                    nuevaY += pasos;
                    nuevaX += pasos;
                    break;
                default:
                    System.out.println("Dirección no válida.");
                    return 0;
            }

            // Validar límites del tablero
            if (nuevaX < 0 || nuevaX >= tablero[0].length || nuevaY < 0 || nuevaY >= tablero.length) {
                System.out.println("Se salió del tablero entonces return 0");
                return 0;
            }

            // Mover robot en el tablero
            tablero[nuevaY][nuevaX] = robotChar;
            tablero[posicionY][posicionX] = ' ';
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Se salió del tablero entonces return 0");
            return 0;
        }

        return 1;
    }
}
