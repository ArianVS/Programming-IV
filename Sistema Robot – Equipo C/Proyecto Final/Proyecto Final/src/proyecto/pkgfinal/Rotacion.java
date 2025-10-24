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

public class Rotacion extends MDinamico {
    private Scanner scan = new Scanner(System.in);

    public Rotacion() {
        super(2, "Rotación", "Módulo de rotación por defecto", 0, 0, 0, 1);
        while (true) {
            try {
                System.out.println("Id asignado al módulo de rotación por default: " + this.id);

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
    public char[][] moverse(float[] movimiento, char[][] tablero, int posicionX, int posicionY) {
        // Verificar que el módulo y el robot estén encendidos
        if (!estaEncendido() || (robot != null && !robot.estaEncendido())) {
            System.out.println("No se puede mover: módulo o robot apagado.");
            return new char[][] {{'0'}};
        }

        try {
            // Sólo cambia orientación, no posición
            if (movimiento[1] == 0.0f) {
                tablero[posicionY][posicionX] = 'A'; // Mirando hacia arriba
            } else if (movimiento[1] == 90.0f) {
                tablero[posicionY][posicionX] = 'D'; // Mirando hacia la derecha
            } else if (movimiento[1] == -90.0f) {
                tablero[posicionY][posicionX] = 'I'; // Mirando hacia la izquierda
            } else if (movimiento[1] == 180.0f || movimiento[1] == -180.0f) {
                tablero[posicionY][posicionX] = 'B'; // Mirando hacia abajo
            } else if (movimiento[1] < 0.0f && movimiento[1] > -90.0f) {
                tablero[posicionY][posicionX] = '1'; // Arriba-izquierda
            } else if (movimiento[1] > 0.0f && movimiento[1] < 90.0f) {
                tablero[posicionY][posicionX] = '2'; // Arriba-derecha
            } else if (movimiento[1] < -90.0f && movimiento[1] > -180.0f) {
                tablero[posicionY][posicionX] = '3'; // Abajo-izquierda
            } else if (movimiento[1] > 90.0f && movimiento[1] < 180.0f) {
                tablero[posicionY][posicionX] = '4'; // Abajo-derecha
            } else {
                System.out.println("Movimiento inválido (>180°), no se mueve.");
                return new char[][] {{'0'}};
            }
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Se salió del tablero entonces return 0");
            return new char[][] {{'0'}};
        }

        // La rotación es exitosa (no cambia posición), devolvemos 1
        return tablero;
    }
}
