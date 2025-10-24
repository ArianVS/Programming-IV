
package Mi_Paquete;

import java.util.List;

public class Categoria {
    private int id;
    private String nombre;    
    // Asociación:  Categoria Padre 1 contiene_a * Categoria 
    private int cat_padre;

    public Categoria() {
        this.id = 0;
        this.nombre = null;
        this.cat_padre = 0;
    }    
    
    public Categoria(int id, String nombre, int padre) {
        this.id = id;
        this.nombre = nombre;
        this.cat_padre = padre;
    }
    
    // Métodos Getters
    public int getId() { return id; }
    public String getNombre() { return nombre; }
    public int getCat_padre() { return cat_padre; }

    // Métodos Setters
    public void setId(int id) { this.id = id; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public void setCat_padre(int padre) { this.cat_padre = padre; }
    
    public void consultar() {
        System.out.println(this.toString());
    }

    public void actualizar(String nombre) {
        this.nombre = nombre;
    }
 
    public void listar(List<Categoria> Categorias) {
        // Verificar si la lista está vacía
        if (Categorias == null || Categorias.isEmpty()) {
            System.out.println("No hay categorías para mostrar.");
            return;
        }

        // Encabezado
        System.out.println("-------------------------------------------------------------------------");
        System.out.println("                  LISTADO DE CATEGORÍAS                  ");
        System.out.println("-------------------------------------------------------------------------");
        System.out.printf("%-15s %-30s %-30s", "CÓDIGO", "CATEGORÍA", "CATEGORÍA PADRE");
        System.out.print("\n"); 
        System.out.println("-------------------------------------------------------------------------");

        // Mostrar cada categoría
        for (Categoria categoria : Categorias) {
            System.out.printf("%-15s %-30s %-30s", 
                              categoria.getId(), 
                              categoria.getNombre(),
                              categoria.getCat_padre());
            System.out.println("\n"); 
        }
    }
    
    @Override
    public String toString() {
        return "Código: " + id + "\tNombre: " + nombre + "\tPadre: " + cat_padre;
    }
}

