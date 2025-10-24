/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;
import java.util.Random;

/**
 *
 * @author valentina
 */
public class Camara extends Percepcion {
    private Sensor_Proximidad sensorProximidad;
    private Altavoz altavoz;
    private Random random;

    public Camara(int id, String referencia, String descripcion, int largo, int ancho, int profundidad, Sensor_Proximidad sensor, Altavoz altavoz) {
        super(id, referencia, descripcion, largo, ancho, profundidad, 1);
        this.sensorProximidad = sensor;
        this.altavoz = altavoz;
        this.random = new Random();
    }

    @Override
    public Object captarInformacion(char[][] tablero, int x, int y, char direccion) {
        return null; 
    }

    @Override
    public int procesarDatos(Object datos) {
        return 0;
    }


    public char[][] manejarObstaculo(char[][] tablero, int robotX, int robotY, char direccion) {
        char frente = (char) sensorProximidad.captarInformacion(tablero, robotX, robotY, direccion);

        if (frente == 'M') {
            altavoz.emitirSonido("Sonido ahuyentador");
            tablero = reubicarMascota(tablero, robotX, robotY, direccion);
        } 
        else if (frente == 'X') {
            return new char[][]{{'X'}};
        }
        else if (frente == ' ' || frente == '@'){
            return new char[][]{{'n'}};
        }
        
        return tablero;
    }
    
    private char[][] reubicarMascota(char[][] tablero, int robotX, int robotY, char direccion) {
        
        int[] posMascota = calcularPosicionFrente(robotX, robotY, direccion);
        tablero[posMascota[1]][posMascota[0]] = ' ';
        
        int nuevaX, nuevaY;
        do {
            nuevaX = random.nextInt(tablero[0].length);
            nuevaY = random.nextInt(tablero.length);
        } while (!esPosicionValida(tablero, robotX, robotY, nuevaX, nuevaY));
        
        tablero[nuevaY][nuevaX] = 'M';
        System.out.println("Mascota reubicada en (" + nuevaX + "," + nuevaY + ")");
        
        return tablero;
    }


    private boolean esPosicionValida(char[][] tablero, int robotX, int robotY, int x, int y) {
        // No debe estar en la posición del robot
        if (x == robotX && y == robotY) return false;
        
        // No debe estar alrededor del robot (frente, atrás, izquierda, derecha)
        if ((Math.abs(x - robotX) <= 1 && Math.abs(y - robotY) <= 1)) return false;
        
        // La celda debe estar libre
        return tablero[y][x] == ' ';
    }

    private int[] calcularPosicionFrente(int x, int y, char direccion) {
        switch (direccion) {
            case 'A': return new int[]{x, y-1};
            case 'B': return new int[]{x, y+1};
            case 'I': return new int[]{x-1, y};
            case 'D': return new int[]{x+1, y};
            default: return new int[]{x, y};
        }
    }

}

