import numpy as np
import warnings
warnings.filterwarnings('ignore')

def evaluar_funcion(funcion_str, x):
    """
    Evalúa la función en un punto x
    
    Parámetros:
    - funcion_str: función como string (usar 'x' como variable)
    - x: valor donde evaluar la función
    
    Retorna:
    - Valor de la función en x
    """
    try:
        return eval(funcion_str, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, 
                                   "tan": np.tan, "exp": np.exp, "log": np.log, 
                                   "sqrt": np.sqrt, "pi": np.pi, "e": np.e})
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")

def verificar_cambio_signo(funcion_str, a, b):
    """
    Verifica que la función tenga cambio de signo en [a, b]
    
    Parámetros:
    - funcion_str: función como string
    - a, b: extremos del intervalo
    
    Retorna:
    - (True, fa, fb) si hay cambio de signo
    - (False, None, None) si no hay cambio de signo
    """
    try:
        fa = evaluar_funcion(funcion_str, a)
        fb = evaluar_funcion(funcion_str, b)
        
        if fa * fb > 0:
            return False, None, None
        return True, fa, fb
    except Exception as e:
        raise ValueError(f"Error al verificar cambio de signo: {e}")

def mostrar_resultados(raiz, iteraciones, historial, funcion_str, error=None):
    """
    Muestra los resultados del método numérico
    
    Parámetros:
    - raiz: aproximación de la raíz encontrada
    - iteraciones: número de iteraciones realizadas
    - historial: lista con las aproximaciones
    - funcion_str: función evaluada
    - error: mensaje de error si existe
    """
    print("\n" + "-" * 60)
    print("RESULTADOS")
    print("-" * 60)
    
    if error and raiz is None:
        print(f"\n❌ {error}")
    else:
        print(f"\n✓ Raíz encontrada: x = {raiz:.10f}")
        print(f"✓ Valor de f(x): {evaluar_funcion(funcion_str, raiz):.2e}")
        print(f"✓ Iteraciones: {iteraciones}")
        
        if error:
            print(f"\n⚠ {error}")
        
        # Mostrar historial de aproximaciones
        print(f"\n{'Iteración':<12} {'Aproximación (x)':<20}")
        print("-" * 35)
        for i, aprox in enumerate(historial, 1):
            print(f"{i:<12} {aprox:.10f}")
