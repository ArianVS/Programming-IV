
package Mi_Paquete;

import java.util.List;

public class Linea_Compra {
    // Asociación: Producto 1 está_referenciado_en * Linea_Compra
    private int producto;
    // Asociación: Compra 1 contiene_a * Linea_Compra
    private int compra;
    private int precio;

    public Linea_Compra() {
        this.producto = 0;
        this.compra = 0;
        this.precio = 0;
    }    
    
    // Constructor que permite representar la operación agregar_producto()
    public Linea_Compra(int producto, int compra, int precio) {
        this.producto = producto;
        this.compra = compra;
        this.precio = precio;
    }
    
    // Métodos Getters
    public int getProducto() { return producto; }
    public int getCompra() { return compra; }
    public int getPrecio() { return precio; }

    // Métodos Setters
    public void setProducto(int producto) { this.producto = producto; }
    public void setCompra(int compra) { this.compra = compra; }
    public void setPrecio(int precio) { this.precio = precio; }
  
    public void consultar(List<Linea_Compra> Linea_Compras, int compra) {
        for (Linea_Compra linea_compra : Linea_Compras) {
            if(linea_compra.getCompra()== compra){
                System.out.println(linea_compra.toString());
            }
        }
    }
 
    @Override
    public String toString() {
        return "Producto: " + producto + "\tCód. Compra: " + compra + "\tPrecio: $" + precio;
    }
}
