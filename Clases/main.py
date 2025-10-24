from ClaseA import Empresa
from ClaseB import Gerente

def main():
    # Crear una instancia de la clase Empresa
    empresa = Empresa("123456789", "Mi Empresa", "Calle Falsa 123")
    
    # Crear una instancia de la clase Gerente
    gerente = Gerente("987654321", "Juan Perez", "555-1234")
    
    # Contratar al gerente en la empresa
    empresa.contrata_a(gerente.ced)
    
    # Imprimir información de la empresa y el gerente
    print(f"Empresa: {empresa.nombre}, ced del gerente contratado: {empresa.ced}")

if __name__ == "__main__":
    main()