
import Mi_Paquete.Cliente;
import Mi_Paquete.Admin;
import Mi_Paquete.Producto;
import Mi_Paquete.Categoria;
import Mi_Paquete.Compra;
import Mi_Paquete.Linea_Compra;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App_Repaso_1 { 

    // Función para tomar la fecha actual con el formato "dd/MM/yyyy HH:mm:ss" en tipo String
    public static String fecha_hora_actual() {
        LocalDateTime ahora = LocalDateTime.now();    // Toma la fecha actual del sistema
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");    // Indica el formato de fecha deseado
        String fechaFormateada = ahora.format(formatter);    // Convierte la fecha de tipo Date a String
        return fechaFormateada;
    }
    
    // Programa Principal
    public static void main(String[] args) {
       
        Scanner entrada = new Scanner(System.in);   // Para leer todas las entradas         
        int opcion=0, band=0, t_usu=0, opc=0, cod=0, cat_p=0, pp=0, categ=0, cdp=0;
        String c=null, n=null, p=null, usu=null, pwd=null, d=null, passwd=null;
        boolean acceso;
        char cp;
        
        List<Admin> Admins = new ArrayList<>(); 
        Admins.add(new Admin("root", "root", "123", 1));   //Existe el admin "root" por defecto 
        List<Cliente> Clientes = new ArrayList<>(); 
        List<Categoria> Categorias = new ArrayList<>();
        List<Producto> Productos = new ArrayList<>();
        List<Compra> Compras = new ArrayList<>();
        List<Linea_Compra> Linea_Compras = new ArrayList<>();        
        
        Admin AdminAuth = new Admin();
        Cliente ClienteAuth = new Cliente();
        Admin admin = new Admin();
        Cliente cliente = new Cliente();
        Categoria categoria = new Categoria();
        Producto producto = new Producto();        
        Compra compra = new Compra(); 
        Linea_Compra linea_compra = new Linea_Compra();
        
        try {            
            /********************** BIENVENIDA ***********************/
            System.out.println("¡BIENVENIDOS A NUESTRA TIENDA!\n\n");
            
            // MENÚ PRINCIPAL
            do{
                System.out.println("Qué quieres hacer hoy?\n");
                System.out.println("\t1. Ver sus productos!");
                System.out.println("\t2. Soy Nuevo! Quiero registrarme para comprar");
                System.out.println("\t3. Ingresar");
                System.out.println("\t4. Salir");

                System.out.print("\nElige tu opción: ");
                opcion = entrada.nextInt();
                entrada.nextLine();   // Para limpiar el buffer en entradas numéricas

                switch (opcion) {
                    case 1:
                        /**************** LISTADO DE PRODUCTOS ***************/
                        System.out.println("\n");                        
                        producto.listar(Productos, Categorias);

                        Thread.sleep(500);
                        System.out.println("\n");
                        break;
                        
                    case 2:
                        /************* REGISTRO DE NUEVO CLIENTE *************/
                        c=null; 
                        n=null; 
                        p=null;

                        System.out.println("\n");
                        System.out.println("Hola! Nos encanta que quieras hacer parte de nuestra familia...");
                        System.out.println("Por favor regálanos tus datos para registrarte en nuestro sistema.\n");
                        System.out.print("Cédula: ");
                        c = entrada.nextLine();
                        System.out.print("Nombre completo: ");
                        n = entrada.nextLine();
                        System.out.print("Contraseña: ");
                        p = entrada.nextLine();
                        System.out.println("\n");
                        
                        // Registro
                        Clientes.add(new Cliente(c, n, p, 2));
                        
                        // Verificación del registro
                        for (Cliente clnt : Clientes) {
                            if(clnt.getId().equals(c)){
                                clnt.consultar(Clientes, c);
                                System.out.println("has sido registrado con éxito! ");
                                System.out.println("\n");
                                System.out.println("Recuerda que tu cédula será tu USUARIO. \nAhora puedes ingresar y disfrutar de nuestros servicios ¡Bienvenido!");
                            }
                        }  
                        
                        Thread.sleep(500);
                        System.out.println("\n");
                        break;
                        
                    case 3:
                        /************************** LOGIN *************************/
                        band = 0;
                        do{
                            System.out.print("\n");
                            System.out.println("LOGIN");
                            System.out.print("Usuario (Id): ");
                            usu = entrada.nextLine();
                            System.out.print("Password: ");
                            pwd = entrada.nextLine();
                            System.out.print("Tipo de Usuario ( Admin -> 1 / Cliente -> 2 ): ");
                            t_usu = entrada.nextInt();
                            entrada.nextLine();

                            if(t_usu == 1 || t_usu == 2){
                                band = 0;
                                System.out.print("\n");
                            }
                            else{  // Si ingresan otro valor de tipo de usuario no existente
                                band = 1;
                                System.out.print("\n");
                            }                
                        }while(band == 1);

                        if(t_usu == 1){
                            // Autenticación del ADMIN
                            acceso = AdminAuth.autenticarse(usu, pwd, Admins);
                            
                            if(acceso){
                                System.out.println("Acceso Autorizado al Administrador "+ usu + "...");
                                Thread.sleep(500);
                                System.out.println("\n");

                                for (Admin adm : Admins) {
                                    if (adm.getId().equals(usu)) {
                                        AdminAuth = adm;
                                    }
                                }                 
                                /************************ MENÚ ADMIN **************************/
                                do {
                                        System.out.println("\n--------------------------------------------------------");
                                        System.out.println("              MENÚ DEL ADMINISTRADOR                  ");      
                                        System.out.println("--------------------------------------------------------\n");
                                        System.out.println("GESTIÓN DE CLIENTES");   
                                        System.out.println("\t1. Listado de clientes");   
                                        System.out.println("\t2. Consultar cliente");    
                                        System.out.println("GESTIÓN DE CATEGORÍAS DE PRODUCTOS");  
                                        System.out.println("\t3. Crear una nueva categoría");   
                                        System.out.println("\t4. Listado de categorías");    
                                        System.out.println("GESTIÓN DE PRODUCTOS");   
                                        System.out.println("\t5. Crear un nuevo producto");    
                                        System.out.println("\t6. Listado de productos");   
                                        System.out.println("\t7. Consultar producto");   
                                        System.out.println("GESTIÓN DE COMPRAS");   
                                        System.out.println("\t8. Listado de compras");   
                                        System.out.println("\t9. Listado de compras de un cliente");  
                                        System.out.println("GESTIÓN DEL ADMIN");    
                                        System.out.println("\t10. Actualizar contraseña");   
                                        System.out.println("\t11. Crear un nuevo usuario ADMIN");   
                                        System.out.println("\t12. Listar usuarios ADMIN");   
                                        System.out.println("13. SALIR\n");   

                                        System.out.print("Elige una opción: ");
                                        opc = entrada.nextInt();
                                        entrada.nextLine();

                                        switch (opc) {
                                            case 1:
                                                // Listado de Clientes
                                                System.out.println("\n");
                                                cliente.listar(Clientes);

                                                Thread.sleep(500);
                                                System.out.println("\n"); 
                                                break;
                                                
                                            case 2:
                                                // Consultar Cliente
                                                c = null;
                                                
                                                System.out.println("\n");
                                                System.out.print("Ingresa la cédula (usuario) del cliente que deseas consultar: ");
                                                c = entrada.nextLine();
                                                
                                                System.out.println("\n");
                                                cliente.consultar(Clientes, c);

                                                Thread.sleep(500);
                                                System.out.println("\n");                                    
                                                break;
                                                
                                            case 3:
                                                // Crear una nueva categoría
                                                cod=0; 
                                                n=null;
                                                cat_p=0;
                                                band=0;
                                                
                                                System.out.println("\n");
                                                System.out.println("Estas creando una nueva categoría");
                                                System.out.println("Por favor ingresa los datos.\n");
                                                System.out.print("Código: ");
                                                cod = entrada.nextInt();
                                                entrada.nextLine();
                                                System.out.print("Nombre: ");
                                                n = entrada.nextLine();
                                                System.out.println("\n");
                                                
                                                System.out.print("Esta categoría pertenece a otra? s/n  ");
                                                cp = entrada.nextLine().charAt(0);
                                                
                                                if(cp == 's'){  // Es subcategoría
                                                    System.out.println("\nElige una de las siguientes categorías como su categoría padre.");
                                                    System.out.println("\n");
                                                    categoria.listar(Categorias);                                                    
                                                    
                                                    do{
                                                        System.out.println("\n");
                                                        System.out.print("Padre: ");
                                                        cat_p = entrada.nextInt();
                                                        entrada.nextLine();
                                                        System.out.println("\n");

                                                        for (Categoria cat : Categorias) {
                                                            if(cat.getId() == cat_p){
                                                                band = 1;
                                                            }
                                                        }
                                                        if (band == 0){
                                                            System.out.println("\nCategoría inexistente. Por favor ingresa otro valor.");
                                                        }
                                                    }while(band == 0);
                                                }
                                                else{  // No es subcategoría
                                                    cat_p = 0;
                                                }

                                                // Creación
                                                Categorias.add(new Categoria(cod, n, cat_p));

                                                // Verificación de la Creación
                                                for (Categoria cat : Categorias) {
                                                    if(cat.getId() == cod){
                                                        cat.consultar();
                                                        System.out.println("\nLa categoría ha sido creada con éxito.");
                                                    }
                                                }

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 4:
                                                // Listado de categorías
                                                System.out.println("\n");                                                
                                                categoria.listar(Categorias);
                                                
                                                System.out.println("\n");
                                                System.out.println("-------------------------------------------------------------------------");
                                                System.out.println("Total de Categorías: " + Categorias.size());
                                                System.out.println("-------------------------------------------------------------------------");

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 5:
                                                // Crear un nuevo producto
                                                cod=0;                                                 
                                                n=null;
                                                d=null;
                                                pp=0;
                                                categ=0;
                                                band=0;
                                                
                                                System.out.println("\n");
                                                System.out.println("Estas creando un nuevo producto");
                                                System.out.println("Por favor ingresa los datos.\n");
                                                System.out.print("Código: ");
                                                cod = entrada.nextInt();
                                                entrada.nextLine();
                                                System.out.print("Nombre: ");
                                                n = entrada.nextLine();
                                                System.out.print("Descripción: ");
                                                d = entrada.nextLine();
                                                System.out.print("Precio: ");
                                                pp = entrada.nextInt();
                                                entrada.nextLine();
                                                System.out.println("\n");                                                
                                                    
                                                System.out.println("\nElige una de las siguientes categorías para el producto.");

                                                System.out.println("\n");                                                
                                                categoria.listar(Categorias);

                                                do{
                                                    System.out.println("\n");
                                                    System.out.print("Categoría: ");
                                                    categ = entrada.nextInt();
                                                    entrada.nextLine();
                                                    System.out.println("\n");

                                                    for (Categoria cat : Categorias) {
                                                        if(cat.getId() == categ){
                                                            band = 1;
                                                        }
                                                    }
                                                    
                                                    if (band == 0){
                                                        System.out.println("\nCategoría inexistente. Por favor ingresa otro valor.");
                                                    }
                                                }while(band == 0);

                                                // Creación
                                                Productos.add(new Producto(cod, n, d, pp, categ));

                                                // Verificación de la Creación
                                                for (Producto prod : Productos) {
                                                    if(prod.getId() == cod){
                                                        prod.consultar(Productos, Categorias, cod);
                                                        System.out.println("\nEl producto ha sido creado con éxito.");
                                                    }
                                                }

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 6:
                                                // Listado de productos
                                                System.out.println("\n");
                                                producto.listar(Productos, Categorias);
                                                
                                                System.out.println("\n");
                                                System.out.println("------------------------------------------------------------------------------------------");
                                                System.out.println("Total de Productos: " + Productos.size());
                                                System.out.println("------------------------------------------------------------------------------------------");
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 7:
                                                // Consultar producto
                                                cod = 0;
                                                
                                                System.out.println("\n");
                                                System.out.print("Ingresa el código del producto que deseas consultar: ");
                                                cod = entrada.nextInt();
                                                entrada.nextLine();
                                                
                                                System.out.println("\n");
                                                producto.consultar(Productos, Categorias, cod);

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 8:                                                
                                                // Listado de compras
                                                System.out.println("\n");                                                
                                                compra.listar(Compras);
                                                
                                                System.out.println("\n");
                                                System.out.println("---------------------------------------------------------------------------------------------------------------");
                                                System.out.println("Total de Compras: " + Compras.size());
                                                System.out.println("---------------------------------------------------------------------------------------------------------------");

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 9:
                                                // Listado de compras de un cliente
                                                c = null;
                                                
                                                System.out.println("\n");
                                                System.out.print("Ingresa la cédula del cliente que deseas consultar: ");
                                                c = entrada.nextLine();
                                                
                                                System.out.println("\n"); 
                                                System.out.println("---------------------------------------------------------------------------------------------------------------");
                                                System.out.println("                            LISTADO DE COMPRAS DEL CLIENTE " + c);
                                                System.out.println("---------------------------------------------------------------------------------------------------------------");
                                                
                                                compra.listar_compras_cliente(Compras, c);
                                 
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 10:
                                                // Actualizar contraseña
                                                System.out.println("\n");
                                                System.out.print("Escribe la nueva contraseña: ");
                                                passwd = entrada.nextLine();
                                                
                                                AdminAuth.actualizar(passwd);
                                                
                                                System.out.println("\nSu Contraseña ha sido actualizada");
                                                System.out.println("Su nueva contraseña es: " + AdminAuth.getPwd());
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 11:
                                                // Crear un nuevo usuario ADMIN
                                                c=null; 
                                                n=null; 
                                                p=null;
                        
                                                System.out.println("\n");
                                                System.out.println("Vas a crear un nuevo usuario ADMIN.");
                                                System.out.println("Por favor ingresa sus datos.\n");
                                                System.out.print("Cédula: ");
                                                c = entrada.nextLine();
                                                System.out.print("Nombre completo: ");
                                                n = entrada.nextLine();
                                                System.out.print("Contraseña: ");
                                                p = entrada.nextLine();
                                                System.out.println("\n");

                                                // Creación
                                                Admins.add(new Admin(c, n, p, 1));

                                                // Verificación de la creación
                                                for (Admin adm : Admins) {
                                                    if(adm.getId().equals(c)){
                                                        adm.consultar();
                                                        System.out.println("ha sido registrado con éxito! ");
                                                        System.out.println("Recuerdale que su cédula será su USUARIO.");
                                                    }
                                                }

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 12:
                                                // Listar usuarios ADMIN
                                                System.out.println("\n"); 
                                                admin.listar(Admins);
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 13:
                                                // SALIR
                                                System.out.println("\n");
                                                System.out.println("Saliendo del Módulo del ADMIN...");
                                                Thread.sleep(500);
                                                break;
                                                
                                            default:
                                                // Opción no válida
                                                System.out.println("\n");
                                                System.out.println("Opción NO válida. Por favor Intente de nuevo.");
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                        }
                                    } while (opc != 13);  
                            }  
                            else{
                                //System.out.println("\n");
                                System.out.println("Sus datos no coinciden. Acceso NO Autorizado...");
                                Thread.sleep(500);
                                System.out.println("\n");
                                break;
                            }
                        }  // Fin Opciones Admin
                        else{
                            
                            acceso = ClienteAuth.autenticarse(usu, pwd, Clientes);
                            
                            if(acceso){
                                System.out.println("Acceso Autorizado al Cliente "+ usu + "...");
                                Thread.sleep(500);
                                System.out.println("\n");

                                for (Cliente clnt : Clientes) {
                                    if (clnt.getId().equals(usu)) {
                                        ClienteAuth = clnt;
                                    }
                                }

                                /************************ MENÚ CLIENTE **************************/
                                do {
                                        System.out.println("\n--------------------------------------------------------");
                                        System.out.println("                          MENÚ     ");
                                        System.out.println("--------------------------------------------------------\n");
                                        System.out.println("NUESTROS PRODUCTOS");    
                                        System.out.println("\t1. Listado de productos");    
                                        System.out.println("\t2. Consulta un producto");    
                                        System.out.println("COMPRAS");
                                        System.out.println("\t3. Realizar una compra");
                                        System.out.println("\t4. Consultar mi factura");
                                        System.out.println("\t5. Mis compras");
                                        System.out.println("GESTIÓN DEL CLIENTE");    
                                        System.out.println("\t6. Actualizar mi contraseña");    
                                        System.out.println("7. SALIR\n");    

                                        System.out.print("Elige una opción: ");
                                        opc = entrada.nextInt();
                                        entrada.nextLine();

                                        switch (opc) {
                                            case 1:
                                                // Listado de productos
                                                System.out.println("\n");                                                
                                                producto.listar(Productos, Categorias);

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 2:
                                                // Consultar producto
                                                cod = 0;
                                                
                                                System.out.println("\n");
                                                System.out.print("Ingresa el código del producto que deseas consultar: ");
                                                cod = entrada.nextInt();
                                                entrada.nextLine();
                                                
                                                System.out.println("\n");
                                                producto.consultar(Productos, Categorias, cod);

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 3:
                                                // Realizar compra
                                                cod = 0;
                                                cdp = 0;
                                                cod = Compras.size() + 1;
                                                
                                                Compra CompraAct = new Compra(cod, ClienteAuth.getId(), fecha_hora_actual());
                                                Compras.add(CompraAct);      
                                                
                                                System.out.println("\n");
                                                System.out.println("Elige los productos que deseas comprar ingresando su código. Aquí tienes nuestro listado de productos.");
                                                
                                                // Listado de productos
                                                System.out.println("\n");
                                                producto.listar(Productos, Categorias);
                                                System.out.println("\n\n");
                                                
                                                System.out.println("Ingresa el código del producto que deseas incluir en tu compra. ");
                                                System.out.println("Cuando termines de incluir los productos que deseas digita 0. ");
                                                System.out.println("\n");
                                                
                                                do{
                                                    band = 0;                                                    
                                                    System.out.print("Producto: ");
                                                    cdp = entrada.nextInt();
                                                    entrada.nextLine();
                                                    
                                                    if(cdp != 0){    // Si desea añadir un producto
                                                        for (Producto prod : Productos) {
                                                            if(prod.getId() == cdp){
                                                                Linea_Compras.add(new Linea_Compra(cdp, cod, prod.getPrecio()));
                                                                band = 1;
                                                                break;
                                                            }
                                                        }

                                                        if (band == 0){
                                                            System.out.println("\nProducto inexistente. Por favor ingrese otro valor.");
                                                        }
                                                    }
                                                    
                                                }while(cdp != 0);    
                                                
                                                System.out.println("\nFactura No. " + CompraAct.getId());
                                                CompraAct.calcular_valor_compra(Linea_Compras);
                                                System.out.println("\nEl valor total de tu compra es: $" + CompraAct.getValor_compra());                                                

                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 4:
                                                // Consultar factura
                                                cod = 0;                                               
                                                
                                                System.out.println("\n");
                                                System.out.print("Ingresa el código de la factura que deseas consultar: ");
                                                cod = entrada.nextInt();
                                                entrada.nextLine();
                                                
                                                System.out.println("\n");
                                                compra.consultar_factura(Compras, cod);      // Mejorar que muestre también el nombre del cliente
                                                System.out.println("Productos: ");
                                                linea_compra.consultar(Linea_Compras, cod);      // Mejorar que muestre también el nombre del producto y no muestre el código de la compra                                          
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 5:
                                                // Mis compras
                                                System.out.println("\n");
                                                System.out.println("--------------------------------------------------------------------------------");
                                                System.out.println("                     MIS FACTURAS                  ");
                                                System.out.println("--------------------------------------------------------------------------------");
                                                                                                
                                                compra.listar_compras_cliente(Compras, ClienteAuth.getId());
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 6:
                                                // Actualizar contraseña
                                                System.out.println("\n");
                                                System.out.print("Escribe la nueva contraseña: ");
                                                passwd = entrada.nextLine();
                                                
                                                ClienteAuth.actualizar(passwd);
                                                
                                                System.out.println("\nSu Contraseña ha sido actualizada");
                                                System.out.println("Su nueva contraseña es: " + ClienteAuth.getPwd());
                                                
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                                break;
                                                
                                            case 7:
                                                // SALIR
                                                System.out.println("\n");
                                                System.out.println("Saliendo del Módulo del CLIENTE...");
                                                Thread.sleep(500);
                                                break;
                                                
                                            default:
                                                // Opción no válida
                                                System.out.println("\n");
                                                System.out.println("Opción NO válida. Por favor Intenta de nuevo.");
                                                Thread.sleep(500);
                                                System.out.println("\n");
                                        }
                                    } while (opc != 7);
                            }
                            else{
                                System.out.println("\n\n");
                                System.out.println("\nSus datos no coinciden. Acceso NO Autorizado...");
                                Thread.sleep(500);
                                System.out.println("\n\n");
                            }
                        } // Fin Opciones Cliente
                        
                        Thread.sleep(500);
                        System.out.println("\n");
                        break;
                        
                    case 4:
                        /************************** SALIR *************************/
                        System.out.println("\n");
                        System.out.println("¡GRACIAS POR VISITARNOS!");
                        System.out.println("Te esperamos en una próxima ocasión.");
                        System.out.println("\nSaliendo de la Aplicación...");
                        Thread.sleep(500);
                        System.out.println("\n");
                        break;
                        
                    default:
                        /******************* OPCIÓN INVÁLIDA *******************/
                        System.out.println("\n");
                        System.out.println("Opción NO Válida. Por favor intenta de nuevo.");
                        Thread.sleep(500);
                        System.out.println("\n");
                }
            }while(opcion != 4);     
            
        } catch (InterruptedException e) {  
            System.err.println("Error en la espera: " + e.getMessage());
        } finally {                        
            System.exit(0);            
        }  // Fin try/catch/finally
            
    } // Fin main()  
}


















//            // Agregar elementos:
//            Clientes.add(new Cliente("001", "Juan Pérez", "",0));
//            Clientes.add(new Cliente("002", "Ana Gómez", "",0));
//
//            // Recorrer la lista:
//            for (Cliente cliente : Clientes) {
//                System.out.println(cliente.getId() + ": " + cliente.getNombre());
//            }