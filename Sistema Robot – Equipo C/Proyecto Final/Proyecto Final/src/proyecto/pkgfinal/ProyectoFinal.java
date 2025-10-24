/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author Juan Felipe Ocampo G
 * @author Arian Valencia
 * @author Valentina
 */
import java.util.Random;
import java.util.Scanner;

public class ProyectoFinal{

    public static void main(String[] args) {
        final int SIZE = 10;
        char[][] tablero = new char[SIZE][SIZE];
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        // 1. Inicializar tablero vacío (espacios en blanco)
        for (int y = 0; y < SIZE; y++) {
            for (int x = 0; x < SIZE; x++) {
                tablero[y][x] = ' ';
            }
        }

        // 2. Agregar obstáculos comunes ('X') y mascotas ('M')
        int numObstaculosComunes = 15;
        int numMascotas = 5;

        // Colocar 'X'
        int colocados = 0;
        while (colocados < numObstaculosComunes) {
            int x = random.nextInt(SIZE);
            int y = random.nextInt(SIZE);
            if (tablero[y][x] == ' ') {
                tablero[y][x] = 'X';
                colocados++;
            }
        }

        // Colocar 'M'
        colocados = 0;
        while (colocados < numMascotas) {
            int x = random.nextInt(SIZE);
            int y = random.nextInt(SIZE);
            if (tablero[y][x] == ' ') {
                tablero[y][x] = 'M';
                colocados++;
            }
        }

        // 3. Colocar robot en posición aleatoria vacía con orientación inicial 'A' (arriba)
        int robotX, robotY;
        do {
            robotX = random.nextInt(SIZE);
            robotY = random.nextInt(SIZE);
        } while (tablero[robotY][robotX] != ' ');

        tablero[robotY][robotX] = 'A'; // Robot mirando hacia arriba

        // 4. Instanciar Robot y Usuario
        Robot robot = new Robot("RX-HEXA-01", "RoboFinal", "Robot para proyecto final");
        Usuario usuario = new Usuario(1, "Operador", "Admin", robot);

        // 5. Crear SistemaControl (vacío) y SistemaComunicacion, luego vincularlos
        SistemaControl control = new SistemaControl();              // Ahora existe este constructor vacío
        SistemaComunicacion comunicacion = new SistemaComunicacion(control);
        comunicacion.setUsuario(usuario);
        usuario.setSistemaComunicacion(comunicacion);

        // 6. Mostrar tablero inicial
        System.out.println("Tablero inicial (10x10):");
        imprimirTablero(tablero);

        // 7. Pedir al usuario coordenadas de destino para el robot
        System.out.println("Ingrese la coordenada de destino para el robot (valores entre 0 y 9):");
        int destX, destY;
        while (true) {
            System.out.print("X (0-9): ");
            destX = scanner.nextInt();
            System.out.print("Y (0-9): ");
            destY = scanner.nextInt();
            if (destX >= 0 && destX < SIZE && destY >= 0 && destY < SIZE) {
                break;
            }
            System.out.println("Coordenadas fuera de rango. Intente de nuevo.");
        }

        // 8. Usuario envía la coordenada destino
        robot.encender();
        usuario.enviar_mensaje(destX, destY, robotX, robotY, tablero);
        tablero[destY][destX] = '@' ;

        
        // 9. Confirmación y fin
        System.out.println("Coordenada destino enviada: (" + destX + ", " + destY + ")");
        robot.resolver(robotX, robotY, destX, destY, tablero);
        System.out.println("Fin del programa.");
    }

    private static void imprimirTablero(char[][] tablero){
        int SIZE = tablero.length;
        // Imprimir índices de columnas
        System.out.print("   ");
        for (int x = 0; x < SIZE; x++) {
            System.out.print(x + " ");
        }
        System.out.println();

        // Imprimir filas con índice
        for (int y = 0; y < SIZE; y++) {
            System.out.print(y + " |");
            for (int x = 0; x < SIZE; x++) {
                System.out.print(tablero[y][x] + " ");
            }
            System.out.println();
        }
    }
}
