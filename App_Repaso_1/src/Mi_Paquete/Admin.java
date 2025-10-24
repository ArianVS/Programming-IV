
package Mi_Paquete;

import java.util.List;

public class Admin {
    private String id;
    private String nombre;
    private String pwd;
    private int tipo_usu;

    public Admin() {
        this.id = null;
        this.nombre = null;
        this.pwd = null;
        this.tipo_usu = 0;
    }    
    
    public Admin(String id, String nombre, String pwd, int tipo_usu) {
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
    
    public void consultar() {
        System.out.println(this.toString());
    }

    public void actualizar(String pwd) {
        this.pwd = pwd;
    }
    
    public void listar(List<Admin> Admins) {
        // Verificar si la lista está vacía
        if (Admins == null || Admins.isEmpty()) {
            System.out.println("No hay clientes para mostrar.");
            return;
        }

        // Encabezado
        System.out.println("------------------------------------------------");
        System.out.println("    LISTADO DE ADMINISTRADORES                 ");
        System.out.println("------------------------------------------------");
        System.out.printf("%-15s %-50s", "ID", "NOMBRE");
        System.out.print("\n"); 
        System.out.println("------------------------------------------------");

        // Mostrar cada cliente
        for (Admin admin : Admins) {
            System.out.printf("%-15s %-50s", 
                              admin.getId(), 
                              admin.getNombre());
            System.out.println("\n"); 
        }

        System.out.println("------------------------------------------------");
        System.out.println("Total de usuarios Admin: " + Admins.size());
        System.out.println("------------------------------------------------");
    }
   
    public boolean autenticarse(String id, String pwd, List<Admin> Admins) {
        // Validación básica de parámetros
        if (id == null || pwd == null || id.isEmpty() || pwd.isEmpty()) {
            return false;
        }

        // Buscar el admin en la lista
        for (Admin admin : Admins) {
            if (admin.getId().equals(id) && admin.getPwd().equals(pwd)) {
                return true; // Autenticación exitosa
            }
        }

        return false; // No se encontró el cliente o la contraseña no coincide
    }
    
    @Override
    public String toString() {
        return "ADMIN:  \nCédula: " + id + "\tNombre: " + nombre;
    }  
}
