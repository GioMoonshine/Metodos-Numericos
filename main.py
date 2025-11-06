import sys
import os

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from metodos.bisection import metodo_bisection
from metodos.regula_falsi import metodo_regula_falsi
from metodos.fixed_point import metodo_fixed_point
from metodos.newton_raphson import metodo_newton_raphson
from metodos.secante import metodo_secante
from metodos.brent import metodo_brent
from metodos.utilidades import mostrar_resultados

# Diccionario de métodos disponibles
METODOS_DISPONIBLES = {
    1: {
        'nombre': 'Bisección',
        'funcion': metodo_bisection,
        'tipo': 'intervalo',
        'categoria': 'cerrado'
    },
    2: {
        'nombre': 'Regula Falsi (Falsa Posición)',
        'funcion': metodo_regula_falsi,
        'tipo': 'intervalo',
        'categoria': 'cerrado'
    },
    3: {
        'nombre': 'Fixed Point (Punto Fijo)',
        'funcion': metodo_fixed_point,
        'tipo': 'punto_simple',
        'categoria': 'abierto'
    },
    4: {
        'nombre': 'Newton-Raphson',
        'funcion': metodo_newton_raphson,
        'tipo': 'newton',
        'categoria': 'abierto'
    },
    5: {
        'nombre': 'Secante',
        'funcion': metodo_secante,
        'tipo': 'dos_puntos',
        'categoria': 'abierto'
    },
    6: {
        'nombre': 'Brent (Híbrido)',
        'funcion': metodo_brent,
        'tipo': 'intervalo',
        'categoria': 'hibrido'
    }
}

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "-" * 60)
    print("SELECCIONE EL MÉTODO:")
    print("-" * 60)

    # Métodos cerrados
    print("\n🔒 MÉTODOS CERRADOS (requieren intervalo [a,b]):")
    print("-" * 60)
    for key, metodo in METODOS_DISPONIBLES.items():
        if metodo['categoria'] == 'cerrado':
            print(f"{key}. Método de {metodo['nombre']}")
    
    # Métodos abiertos
    print("\n🔓 MÉTODOS ABIERTOS (requieren valor(es) inicial(es)):")
    print("-" * 60)
    for key, metodo in METODOS_DISPONIBLES.items():
        if metodo['categoria'] == 'abierto':
            print(f"{key}. Método de {metodo['nombre']}")
    
    # Métodos híbridos
    print("\n⚡ MÉTODOS HÍBRIDOS:")
    print("-" * 60)
    for key, metodo in METODOS_DISPONIBLES.items():
        if metodo['categoria'] == 'hibrido':
            print(f"{key}. Algoritmo de {metodo['nombre']}")
    
    print("=" * 60)

def solicitar_datos_intervalo():
    """Solicita función e intervalo [a, b]"""
    print("\n" + "-" * 60)
    print("Ingrese los datos del problema:")
    print("-" * 60)
    
    print("\nFunción f(x) = 0")
    print("Use 'x' como variable. Ejemplos:")
    print("  • x**3 - x - 2")
    print("  • exp(x) - 3*x")
    print("  • sin(x) - x/2")
    funcion = input("\nIngrese f(x): ").strip()
    
    print("\nIntervalo inicial [a, b]:")
    try:
        a = float(input("  a = "))
        b = float(input("  b = "))
        return funcion, a, b
    except ValueError:
        raise ValueError("Los valores del intervalo deben ser numéricos")

def solicitar_datos_punto_simple():
    """Solicita función y un punto inicial"""
    print("\n" + "-" * 60)
    print("Ingrese los datos del problema:")
    print("-" * 60)
    
    print("\nFunción g(x) para punto fijo: x = g(x)")
    print("NOTA: Debe reformular f(x)=0 como x=g(x)")
    print("Ejemplos:")
    print("  • Para f(x) = x**2 - 5, use g(x) = sqrt(5)")
    print("  • Para f(x) = exp(x) - 3*x, use g(x) = exp(x)/3")
    funcion = input("\nIngrese g(x): ").strip()
    
    try:
        x0 = float(input("\nValor inicial x0: "))
        return funcion, x0
    except ValueError:
        raise ValueError("El valor inicial debe ser numérico")

def solicitar_datos_newton():
    """Solicita función, derivada opcional y punto inicial"""
    print("\n" + "-" * 60)
    print("Ingrese los datos del problema:")
    print("-" * 60)
    
    print("\nFunción f(x) = 0")
    print("Use 'x' como variable. Ejemplos:")
    print("  • x**3 - x - 2")
    print("  • exp(x) - 3*x")
    funcion = input("\nIngrese f(x): ").strip()
    
    print("\nDerivada f'(x) (opcional - presione Enter para cálculo numérico):")
    derivada = input("Ingrese f'(x): ").strip()
    if not derivada:
        derivada = None
    
    try:
        x0 = float(input("\nValor inicial x0: "))
        return funcion, x0, derivada
    except ValueError:
        raise ValueError("El valor inicial debe ser numérico")

def solicitar_datos_dos_puntos():
    """Solicita función y dos puntos iniciales"""
    print("\n" + "-" * 60)
    print("Ingrese los datos del problema:")
    print("-" * 60)
    
    print("\nFunción f(x) = 0")
    print("Use 'x' como variable. Ejemplos:")
    print("  • x**3 - x - 2")
    print("  • exp(x) - 3*x")
    funcion = input("\nIngrese f(x): ").strip()
    
    try:
        x0 = float(input("\nPrimer valor inicial x0: "))
        x1 = float(input("Segundo valor inicial x1: "))
        return funcion, x0, x1
    except ValueError:
        raise ValueError("Los valores iniciales deben ser numéricos")

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
        
        # Solicitar datos según el tipo de método
        try:
            if metodo_seleccionado['tipo'] == 'intervalo':
                funcion, a, b = solicitar_datos_intervalo()
            elif metodo_seleccionado['tipo'] == 'punto_simple':
                funcion, x0 = solicitar_datos_punto_simple()
            elif metodo_seleccionado['tipo'] == 'newton':
                funcion, x0, derivada = solicitar_datos_newton()
            elif metodo_seleccionado['tipo'] == 'dos_puntos':
                funcion, x0, x1 = solicitar_datos_dos_puntos()
        except ValueError as e:
            print(f"\n❌ Error: {e}")
            respuesta = input("\n¿Desea intentar nuevamente? (s/n): ").strip().lower()
            continuar = respuesta == 's'
            continue
        
        # Ejecutar método
        print("\n" + "=" * 60)
        print(f"EJECUTANDO MÉTODO DE {metodo_seleccionado['nombre'].upper()}...")
        print("=" * 60)
        
        if metodo_seleccionado['tipo'] == 'intervalo':
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion, a, b)
        elif metodo_seleccionado['tipo'] == 'punto_simple':
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion, x0)
        elif metodo_seleccionado['tipo'] == 'newton':
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion, x0, derivada)
        elif metodo_seleccionado['tipo'] == 'dos_puntos':
            raiz, iteraciones, historial, error = metodo_seleccionado['funcion'](funcion, x0, x1)
               
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