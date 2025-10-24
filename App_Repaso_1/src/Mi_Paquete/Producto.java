
package Mi_Paquete;

import java.util.List;

public class Producto {
    private int id;
    private String nombre;
    private String descripcion;
    private int precio;    
    // Asociación: Producto * pertenece_a 1 Categoría
    private int categoria;

    public Producto() {
        this.id = 0;
        this.nombre = null;
        this.descripcion = null;
        this.precio = 0;
        this.categoria = 0;
    }    
    
    public Producto(int id, String nombre, String descripcion, int precio, int cat) {
        this.id = id;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.precio = precio;
        this.categoria = cat;
    }
    
    // Métodos Getters
    public int getId() { return id; }
    public String getNombre() { return nombre; }
    public String getDescripcion() { return descripcion; }
    public int getPrecio() { return precio; }
    public int getCategoria() { return categoria; }

    // Métodos Setters
    public void setId(int id) { this.id = id; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
    public void setPrecio(int precio) { this.precio = precio; }
    public void setCategoria(int categoria) { this.categoria = categoria; }
    
    public void consultar(List<Producto> Productos, List<Categoria> Categorias, int cod_prod) {
        String cat=null;
        for (Producto producto : Productos) {
            if(producto.getId() == cod_prod){
                for (Categoria categoria : Categorias) {
                    if(categoria.getId() == producto.getCategoria()){
                        cat = categoria.getNombre();
                        break;
                    }
                }
                System.out.println("Código: " + producto.getId() + "\tNombre: " + producto.getNombre() + "\tDescripción: " + producto.getDescripcion() + "\tPrecio: $" + producto.getPrecio() + "\tCategoría: " + cat);
            }
        } 
    }

    public void actualizar(int precio) {
        this.precio = precio;
    }
 
    public void listar(List<Producto> Productos, List<Categoria> Categorias) {
        // Verificar si la lista está vacía
        if (Productos == null || Productos.isEmpty()) {
            System.out.println("No hay productos para mostrar.");
            return;
        }

        // Encabezado
        System.out.println("------------------------------------------------------------------------------------------");
        System.out.println("                                  LISTADO DE PRODUCTOS                  ");
        System.out.println("------------------------------------------------------------------------------------------");
        System.out.printf("%-15s %-30s %-30s %-15s", "CÓDIGO", "PRODUCTO", "DESCRIPCIÓN", "PRECIO");
        System.out.print("\n"); 
        System.out.println("------------------------------------------------------------------------------------------");

        // Mostrar cada producto por categoría        
        for(Categoria categoria : Categorias) {
            System.out.println(categoria.getNombre());
            //System.out.println("\n");
            for(Producto producto : Productos) {
               if(producto.getCategoria() == categoria.getId()){                   
                   System.out.printf("%-15s %-30s %-30s %-15s", 
                              producto.getId(), 
                              producto.getNombre(),
                              producto.getDescripcion(),
                              producto.getPrecio());
                   System.out.print("\n");
               }
           } 
        }
    }
    
    @Override
    public String toString() {
        return "Código: " + id + "\tNombre: " + nombre + "\tDescripción: " + descripcion + "\tPrecio: $" + precio + "\tCategoría: " + categoria;
    }
}
