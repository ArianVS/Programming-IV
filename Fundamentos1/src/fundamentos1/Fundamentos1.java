/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package fundamentos1;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author arian
 */
public class Fundamentos1 {
    

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
        
        // Se usa una instancia de la clase Scanner para leer todas las entradas
        Scanner entrada = new Scanner(System.in);
        // Variable para leer la opción del menú
        int opcion;
        do{   
            System.out.println("------------- EJERCICIOS FUNDAMENTOS DE JAVA ------------- \n");
            
            System.out.println("MENU:");
            System.out.println("1. EJERCICIO 1");
            System.out.println("2. EJERCICIO 2");
            System.out.println("3. EJERCICIO 3");
            System.out.println("4. EJERCICIO 5");
            System.out.println("5. EJERCICIO 5");
            System.out.println("6. EJERCICIO 6");
            System.out.println("7. EJERCICIO 7");
            System.out.println("8. EJERCICIO 8");
            System.out.println("9. EJERCICIO 9");
            System.out.println("10. SALIR");
            
            System.out.println("Digite el número del ejercico que desea ejecutar: ");
            opcion = entrada.nextInt();  // lee datos de tipo entero
            // Siempre que se lea una entrada se recomienda limpiar el buffer
            entrada.nextLine();
            System.out.println("---------------------------------------------------- ");
            System.out.println(" \n");
            
            // Condicional Switch: Presenta varias opciones de acciones dependiendo del valor de la variable opción
            switch (opcion){
                
                case 1 -> {
                    System.out.println("\tNumber\t\tSquare");
                    
                    for(int i = 1; i <= 5; i++){
                        System.out.print("\t"+i + "\t\t  " + Math.pow(i, 2) + "\n");
                    }
                    
                    System.out.println("Presione cualquier tecla para continuar: ");
                    entrada.next();
                    break;
                }
                
                case 2 -> {
                     ArrayList Lista1 = new ArrayList() ;
                     Lista1.add(1);
                     Lista1.add(2);
                     Lista1.add(3);
                     Lista1.add(4);
                     Lista1.add(5);
                    
                    
                    Invertir_Lista(Lista1);
                    
                    System.out.println("Presione cualquier tecla para continuar: ");
                    entrada.next();
                    break;
                    
                }

                
                case 3 -> {
                    
                }
                
                case 4 -> {
                    
                }
                
                case 5 -> {
                    
                }
                
                case 6 -> {
                    
                }
                
                case 7 -> {
                    
                }
                
                case 8 -> {
                    
                }
                
                case 9 -> {
                    
                }
                
                case 10 -> {
                    //-------- SALIR -------
                    // Esperar salida
                    System.out.print("\nPresione cualquier tecla y luego Enter para salir...");
                    entrada.nextLine();
                }
                
                default -> {
                    System.out.println("OPCIÓN NO VÁLIDA");
                    System.out.println(" \n");
                }
                
            } // Fin switch
            
        }while(opcion != 12); // Fin Do-While
        // Forma recomendada para terminar la aplicación (más simple)
        System.exit(0); // Terminación exitosa
        //System.exit(1); // Terminación con error
        
        // Forma equivalente para terminar la aplicación
        //Runtime.getRuntime().exit(0);
        
    }  // Fin main()  

}
