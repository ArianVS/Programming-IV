/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author arian
 */
public class Empresa {
    public String nit;
    public String nombre;
    public String direccion;
    public String cedulaGerente;

    public Empresa(String nit, String nombre, String direccion) {
        this.nit = nit;
        this.nombre = nombre;
        this.direccion = direccion;
    }

    public void contrata_a(String cedula) {
        this.cedulaGerente = cedula;
    }
}
