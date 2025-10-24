
package ensambladospropagaciónoperaciones;

import java.util.ArrayList;
import java.util.List;

// Interfaz común para los Componentes y el Ensamblado
interface ParteEnsamblado {
    void Operacion();   // Método abstracto: No tiene implementación
}

// Clase Componente que implementa la interfaz
class Componente implements ParteEnsamblado {
    private String AtributoC1;

    public Componente(String AtrC1) {
        this.AtributoC1 = AtrC1;
    }

    @Override
    public void Operacion() {
        System.out.println("Operación del Componente: " + AtributoC1);
    }
}

// Clase Ensamblado que implementa la interfaz y propaga la operación
class Ensamblado implements ParteEnsamblado {
    private String AtributoE1;
    private List<Componente> Componentes = new ArrayList<>();

    public Ensamblado(String AtrE1) {
        this.AtributoE1 = AtrE1;
    }

    public void AgregarComponente(Componente Comp) {
        Componentes.add(Comp);
    }

    @Override
    public void Operacion() {
        System.out.println("Operación del Ensamblado: " + AtributoE1);
        
        // Propagar la operación a todos los componentes
        for (Componente Compo : Componentes) {
            Compo.Operacion();   // Operación del Componente
        }
    }
}

// Programa Principal
public class EnsambladosPropagaciónOperaciones {
    public static void main(String[] args) {
        // Crear componentes individuales
        Componente C1 = new Componente("c1");
        Componente C2 = new Componente("c2");
        
        // Crear un ensamblado y agregar componentes
        Ensamblado E1 = new Ensamblado("e1");
        E1.AgregarComponente(C1);
        E1.AgregarComponente(C2);
        
        // Ejecutar la operación (se propaga a los componentes)
        System.out.println("Operaciones propagadas desde el Ensamblado a los Componentes: ");
        E1.Operacion();
    }
}










