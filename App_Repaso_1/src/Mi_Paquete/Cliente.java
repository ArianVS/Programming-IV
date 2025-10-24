
package Mi_Paquete;

import java.util.List;

public class Cliente {
    private String id;
    private String nombre;
    private String pwd;
    private int tipo_usu;

    public Cliente() {
        this.id = null;
        this.nombre = null;
        this.pwd = null;
        this.tipo_usu = 0;
    }    
    
    public Cliente(String id, String nombre, String pwd, int tipo_usu) {
        this.id = id;
        this.nombre = nombre;
        this.pwd = pwd;
        this.tipo_usu = tipo_usu;
    }
    
    // Métodos Getters
    public String getId() { return id; }
    public String getNombre() { return nombre; }
    public String getPwd() { return pwd; }
    public int getTipo_usu() { return tipo_usu; }

    // Métodos Setters
    public void setId(String id) { this.id = id; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public void setPwd(String pwd) { this.pwd = pwd; }
    
    public void consultar(List<Cliente> Clientes, String clnt) {        
        for (Cliente cliente : Clientes) {
            if(cliente.getId().equals(clnt)){
                System.out.println(cliente.toString());
            }
        } 
    }

    public void actualizar(String pwd) {
        this.pwd = pwd;
    }
 
    public void listar(List<Cliente> Clientes) {
        // Verificar si la lista está vacía
        if (Clientes == null || Clientes.isEmpty()) {
            System.out.println("No hay clientes para mostrar.");
            return;
        }

        // Encabezado
        System.out.println("------------------------------------------------");
        System.out.println("                  LISTADO DE CLIENTES                 ");
        System.out.println("------------------------------------------------");
        System.out.printf("%-15s %-50s", "ID", "NOMBRE");
        System.out.print("\n"); 
        System.out.println("------------------------------------------------");

        // Mostrar cada cliente
        for (Cliente cliente : Clientes) {
            System.out.printf("%-15s %-50s", 
                              cliente.getId(), 
                              cliente.getNombre());
            System.out.println("\n"); 
        }

        System.out.println("------------------------------------------------");
        System.out.println("Total de Clientes: " + Clientes.size());
        System.out.println("------------------------------------------------");
    }
    
    public boolean autenticarse(String id, String pwd, List<Cliente> Clientes) {
        // Validación básica de parámetros
        if (id == null || pwd == null || id.isEmpty() || pwd.isEmpty()) {
            return false;
        }

        // Buscar el cliente en la lista
        for (Cliente cliente : Clientes) {
            if (cliente.getId().equals(id) && cliente.getPwd().equals(pwd)) {
                return true; // Autenticación exitosa
            }
        }

        return false; // No se encontró el cliente o la contraseña no coincide
    }
    
    @Override
    public String toString() {
        return "CLIENTE:  \nCédula: " + id + "\tNombre: " + nombre;
    }
}
