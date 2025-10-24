/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto.pkgfinal;

/**
 *
 * @author arian
 */
import java.util.ArrayList;
import java.util.List;

public class Robot {
    private String serie;
    private String alias;
    private String descripcion;
    private int estado = 0; // 0 = apagado, 1 = encendido

    private List<Modulo> modulos;

    public Robot(String serie, String alias, String descripcion) {
        this.serie = serie;
        this.alias = alias;
        this.descripcion = descripcion;
        this.modulos = new ArrayList<>();
        
        modulos.add(new Extension());
        modulos.add(new Rotacion());
        modulos.add(new Helicoidal());
        modulos.add(new Camara(3, "3", "3", 3, 3, 3, new Sensor_Proximidad(4, "4", "4", 4, 4, 4, 4), new Altavoz(5, "5", "5", 5, 5, 5, 5) ) );
    }
    

    public void agregarModulo(Modulo modulo) {
        modulo.setRobot(this);
        modulos.add(modulo);
    }

    public void encender() {
        estado = 1;
        System.out.println("Robot " + alias + " encendido.");
        for (Modulo m : modulos) {
            m.encender();
        }
    }

    public void apagar(){
        estado = 0;
        System.out.println("Robot " + alias + " apagado.");
        for (Modulo m : modulos) {
            m.apagar();
        }
    }

    public boolean estaEncendido() {
        return estado == 1;
    }

    public String getAlias() {
        return alias;
    }
    
    
    public int[] actualizarPosicion(char[][] tablero) {
    char[] direcciones = {'A', 'B', 'I', 'D', '1', '2', '3', '4'};

    for (int y = 0; y < tablero.length; y++) {
        for (int x = 0; x < tablero[0].length; x++) {
            for (char direccion : direcciones) {
                if (tablero[y][x] == direccion) {
                    return new int[] { y, x }; // Devuelve [posicionY, posicionX]
                }
            }
        }
    }

    return new int[] { -1, -1 }; // No se encontró ninguna dirección
}
    
    
    public void resolver(int robotX, int robotY, int banderaX, int banderaY, char[][] tablero){
        Extension extension = (Extension)modulos.get(0);
        Rotacion rotacion = (Rotacion)modulos.get(1);
        Helicoidal helicoidal = (Helicoidal)modulos.get(2);
        Camara camara = (Camara)modulos.get(3);
        
        while(true){
            System.out.println("bandera X/Y: "+ banderaY + " " + banderaX);
            System.out.println("robot X/Y: "+ robotY + " " + robotX);
            
            char[][] nuevoTablero = camara.manejarObstaculo(tablero, robotX, robotY, tablero[robotY][robotX]);
            char estado = nuevoTablero[0][0];
            System.out.println("Cosa encontrada en el nuevo tabler: " + estado);
            
            if(robotY == banderaY && robotX == banderaX){
                System.out.println("Legaste a la meta");
                break;
            }
            else if(banderaY < robotY){
                System.out.println("direccion del robot: " + tablero[robotY][robotX]);
                tablero = rotacion.moverse(new float[]{0, 0}, tablero, robotX, robotY);//lo pone para arriba
                int[]nuevaPosicion = actualizarPosicion(tablero);
                robotY = nuevaPosicion[0];
                robotX = nuevaPosicion[1];
                nuevoTablero = camara.manejarObstaculo(tablero, robotX, robotY, tablero[robotY][robotX]);
                estado = nuevoTablero[0][0];
                
                if(estado == 'n' || estado == '@'){
                    tablero = extension.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                    nuevaPosicion = actualizarPosicion(tablero);
                    robotY = nuevaPosicion[0];
                    robotX = nuevaPosicion[1];
                }
                else if(estado == 'X'){
                    if(banderaX >= robotX){ //se mueve para la derecha hasta que pueda seguir yendo hacia arriba
                        tablero = helicoidal.moverse(new float[]{1, 90}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY -1][robotX] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                    
                    if(banderaX <= robotX){//se mueve a la izquierda hasta que pueda seguir para arribaq1
                        tablero = helicoidal.moverse(new float[]{1, -90}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY -1][robotX] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    } 
                }
                else{tablero = nuevoTablero;}
            }
            
            
            if(banderaY > robotY){
                tablero = rotacion.moverse(new float[]{0, 180}, tablero, robotX, robotY);//lo pone boca a bajo
                int[]nuevaPosicion = actualizarPosicion(tablero);
                robotY = nuevaPosicion[0];
                robotX = nuevaPosicion[1];
                nuevoTablero = camara.manejarObstaculo(tablero, robotX, robotY, tablero[robotY][robotX]);
                estado = nuevoTablero[0][0];
                
                if(estado == 'n' || estado == '@'){
                    tablero = extension.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                    nuevaPosicion = actualizarPosicion(tablero);
                    robotY = nuevaPosicion[0];
                    robotX = nuevaPosicion[1];
                }
                else if(estado == 'X'){
                    if(banderaX >= robotX){ //se mueve para la derecha hasta que pueda seguir yendo hacia abajo
                        tablero = helicoidal.moverse(new float[]{1, 90}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY +1][robotX] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 180}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                    
                    if(banderaX <= robotX){//se mueve a la izquierda hasta que pueda seguir para arribaq1
                        tablero = helicoidal.moverse(new float[]{1, -90}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY +1][robotX] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 180}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                }
                else{tablero = nuevoTablero;}
                
            }
            
            
            if(banderaX > robotX){
                tablero = rotacion.moverse(new float[]{0, 90}, tablero, robotX, robotY);//lo pone hacia la derecha
                int[]nuevaPosicion = actualizarPosicion(tablero);
                robotY = nuevaPosicion[0];
                robotX = nuevaPosicion[1];
                nuevoTablero = camara.manejarObstaculo(tablero, robotX, robotY, tablero[robotY][robotX]);
                estado = nuevoTablero[0][0];
                
                if(estado == 'n' || estado == '@'){
                    tablero = extension.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                    nuevaPosicion = actualizarPosicion(tablero);
                    robotY = nuevaPosicion[0];
                    robotX = nuevaPosicion[1];
                }
                else if(estado == 'X'){
                    if(banderaY >= robotY){ //se mueve para abajo hasta que pueda seguir yendo hacia la derecha
                        tablero = helicoidal.moverse(new float[]{1, 180}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY][robotX +1] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 90}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                    
                    if(banderaY <= robotY){//se mueve arriba hasta que pueda seguir para la derecha
                        tablero = helicoidal.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY][robotX +1] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, 90}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                }
                else{tablero = nuevoTablero;}

            }
            
            
            if(banderaX < robotX){
                tablero = rotacion.moverse(new float[]{0, -90}, tablero, robotX, robotY);//lo pone hacia la izquierda
                int[]nuevaPosicion = actualizarPosicion(tablero);
                robotY = nuevaPosicion[0];
                robotX = nuevaPosicion[1];
                nuevoTablero = camara.manejarObstaculo(tablero, robotX, robotY, tablero[robotY][robotX]);
                estado = nuevoTablero[0][0];
                
                if(estado == 'n' || estado == '@'){
                    tablero = extension.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                    nuevaPosicion = actualizarPosicion(tablero);
                    robotY = nuevaPosicion[0];
                    robotX = nuevaPosicion[1];
                }
                else if(estado == 'X'){
                    if(banderaY >= robotY){ //se mueve para abajo hasta que pueda seguir yendo hacia la izquierda
                        tablero = helicoidal.moverse(new float[]{1, 180}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY][robotX -1] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, -90}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                    
                    if(banderaY <= robotY){//se mueve arriba hasta que pueda seguir para la derecha
                        tablero = helicoidal.moverse(new float[]{1, 0}, tablero, robotX, robotY);
                        nuevaPosicion = actualizarPosicion(tablero);
                        robotY = nuevaPosicion[0];
                        robotX = nuevaPosicion[1];

                        if(tablero[robotY][robotX -1] == ' '){
                            tablero = helicoidal.moverse(new float[]{1, -90}, tablero, robotX, robotY);
                            nuevaPosicion = actualizarPosicion(tablero);
                            robotY = nuevaPosicion[0];
                            robotX = nuevaPosicion[1];
                        }
                    }
                }
                else{tablero = nuevoTablero;}

            }

            
        }
    }
}