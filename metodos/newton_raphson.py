def metodo_newton_raphson(funcion_str, x0, derivada_str=None, tolerancia=1e-10, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar raíces
    
    Parámetros:
    - funcion_str: función f(x) como string
    - x0: aproximación inicial
    - derivada_str: derivada f'(x) como string (opcional, se calcula numéricamente si no se proporciona)
    - tolerancia: tolerancia para el criterio de parada
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - historial: lista con las aproximaciones en cada iteración
    - error: mensaje de error si existe
    """
    from .utilidades import evaluar_funcion, derivada_numerica
    
    historial = []
    x = x0
    
    for i in range(max_iter):
        try:
            fx = evaluar_funcion(funcion_str, x)
            
            # Calcular derivada
            if derivada_str:
                fpx = evaluar_funcion(derivada_str, x)
            else:
                fpx = derivada_numerica(funcion_str, x)
            
            # Verificar que la derivada no sea cero
            if abs(fpx) < 1e-12:
                return None, i + 1, historial, "Error: Derivada cercana a cero. El método no puede continuar"
            
            # Calcular nueva aproximación
            x_nuevo = x - fx / fpx
            historial.append(x_nuevo)
            
            # Verificar convergencia
            if abs(x_nuevo - x) < tolerancia or abs(fx) < tolerancia:
                return x_nuevo, i + 1, historial, None
            
            # Verificar divergencia
            if abs(x_nuevo) > 1e10:
                return None, i + 1, historial, "Error: El método diverge. Intente con otro valor inicial"
            
            x = x_nuevo
            
        except Exception as e:
            return None, i + 1, historial, f"Error durante la iteración: {e}"
    
    return x, max_iter, historial, "Advertencia: Se alcanzó el máximo de iteraciones"
