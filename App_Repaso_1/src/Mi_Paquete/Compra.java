
package Mi_Paquete;

import java.util.List;

public class Compra {
    private int id;
    // Asociación: Cliente 1 realiza_a * Compra
    private String cliente;
    private String fecha_compra;
    private int valor_compra;
    

    public Compra() {
        this.id = 0;
        this.cliente = null;
        this.fecha_compra = null;
        this.valor_compra = 0;        
    }    
    
    // Constructor que permite representar la operación realizar_compra()
    public Compra(int id, String cliente, String f_compra) {
        this.id = id;
        this.cliente = cliente;
        this.fecha_compra = f_compra;
        this.valor_compra = 0;        
    }
    
    // Métodos Getters
    public int getId() { return id; }
    public String getCliente() { return cliente; }
    public String getFecha_compra() { return fecha_compra; }
    public int getValor_compra() { return valor_compra; }
    

    // Métodos Setters
    public void setId(int id) { this.id = id; }
    public void setCliente(String cliente) { this.cliente = cliente; }
    public void setFecha_compra(String f_compra) { this.fecha_compra = f_compra; }
    public void setValor_compra(int v_compra) { this.valor_compra = v_compra; }
    
    public void calcular_valor_compra(List<Linea_Compra> Linea_Compras){        
        for (Linea_Compra linea_compra : Linea_Compras) {
            if(linea_compra.getCompra() == this.id){
                this.valor_compra = this.valor_compra + linea_compra.getPrecio();
            }
        }    
    }
    
    public void consultar_factura(List<Compra> Compras, int cod_cmp) {
        for (Compra compra : Compras) {
            if(compra.getId() == cod_cmp){
                System.out.println(compra.toString());
                break;
            }
        }
    }
    
    public void listar(List<Compra> Compras) {
        System.out.println("---------------------------------------------------------------------------------------------------------------");
        System.out.println("                                                     LISTADO DE COMPRAS                  ");
        System.out.println("---------------------------------------------------------------------------------------------------------------");

        for (Compra compra : Compras) {
                System.out.println(compra.toString());
        }
    }
    
    public void listar_compras_cliente(List<Compra> Compras, String cod_clnt) {
        for (Compra compra : Compras) {
            if(compra.getCliente().equals(cod_clnt)){
                System.out.println(compra.toString());
            }
        }
    }
    
    @Override
    public String toString() {
        return "Factura No. " + id + "\tCliente: " + cliente + "\tValor Total de la Compra: $" + valor_compra + "\tFecha de Compra: " + fecha_compra;
    }
}
