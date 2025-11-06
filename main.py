import sys
import os

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from metodos.biseccion import metodo_biseccion
from metodos.regula_falsi import metodo_regula_falsi
from metodos.utilidades import mostrar_resultados

# Diccionario de métodos disponibles
METODOS_DISPONIBLES = {
    1: {
        'nombre': 'Bisección',
        'funcion': metodo_biseccion,
        'requiere_intervalo': True
    },
    2: {
        'nombre': 'Regula Falsi (Falsa Posición)',
        'funcion': metodo_regula_falsi,
        'requiere_intervalo': True
    }
}

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "-" * 60)
    print("SELECCIONE EL MÉTODO:")
    print("-" * 60)
    for key, metodo in METODOS_DISPONIBLES.items():
        print(f"{key}. Método de {metodo['nombre']}")
    print("-" * 60)

def solicitar_datos(requiere_intervalo=True):
    """
    Solicita los datos del problema al usuario
    
    Parámetros:
    - requiere_intervalo: si el método requiere un intervalo [a, b]
    
    Retorna:
    - (funcion, a, b) si requiere_intervalo es True
    - (funcion,) si requiere_intervalo es False
    """
    print("\n" + "-" * 60)
    print("Ingrese los datos del problema:")
    print("-" * 60)
    
    # Solicitar función
    print("\nFunción f(x) = 0")
    print("Use 'x' como variable. Ejemplos:")
    print("  • x**3 - x - 2")
    print("  • exp(x) - 3*x")
    print("  • sin(x) - x/2")
    funcion = input("\nIngrese f(x): ").strip()
    
    if requiere_intervalo:
        # Solicitar intervalo
        print("\nIntervalo inicial [a, b]:")
        try:
            a = float(input("  a = "))
            b = float(input("  b = "))
            return funcion, a, b
        except ValueError:
            raise ValueError("Los valores del intervalo deben ser numéricos")
    
    return (funcion,)

def main():
    """Función principal del programa"""
    print("=" * 60)
    print("MÉTODOS PARA RAÍCES DE ECUACIONES NO LINEALES")
    print("=" * 60)
    
    continuar = True
    
    while continuar:
        mostrar_menu()
        
        # Seleccionar método
        try:
            opcion = int(input("\nIngrese su opción: "))
            if opcion not in METODOS_DISPONIBLES:
                print("\n❌ Error: Opción no válida")
                respuesta = input("\n¿Desea intentar nuevamente? (s/n): ").strip().lower()
                continuar = respuesta == 's'
                continue
        except ValueError:
            print("\n❌ Error: Debe ingresar un número")
            respuesta = input("\n¿Desea intentar nuevamente? (s/n): ").strip().lower()
            continuar = respuesta == 's'
            continue
        
        metodo_seleccionado = METODOS_DISPONIBLES[opcion]
        
        # Solicitar datos
        try:
            datos = solicitar_datos(metodo_seleccionado['requiere_intervalo'])
        except ValueError as e:
            print(f"\n❌ Error: {e}")
            respuesta = input("\n¿Desea intentar nuevamente? (s/n): ").strip().lower()
            continuar = respuesta == 's'
            continue
        
        # Ejecutar método
        print("\n" + "=" * 60)
        print(f"EJECUTANDO MÉTODO DE {metodo_seleccionado['nombre'].upper()}...")
        print("=" * 60)
        
        if metodo_seleccionado['requiere_intervalo']:
            funcion, a, b = datos
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion, a, b)
        else:
            funcion = datos[0]
            # Para futuros métodos que no requieran intervalo
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion)
        
        # Mostrar resultados
        mostrar_resultados(raiz, iteraciones, historial, funcion, error)
        
        # Preguntar si desea continuar
        print("\n" + "=" * 60)
        respuesta = input("¿Desea resolver otra ecuación? (s/n): ").strip().lower()
        continuar = respuesta == 's'
    
    print("\n" + "=" * 60)
    print("Programa finalizado. ¡Hasta pronto!")
    print("=" * 60)

if __name__ == "__main__":
    main()