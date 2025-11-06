def metodo_secante(funcion_str, x0, x1, tolerancia=1e-10, max_iter=1000):
    """
    Método de la Secante para encontrar raíces
    
    Parámetros:
    - funcion_str: función f(x) como string
    - x0, x1: dos aproximaciones iniciales
    - tolerancia: tolerancia para el criterio de parada
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - historial: lista con las aproximaciones en cada iteración
    - error: mensaje de error si existe
    """
    from .utilidades import evaluar_funcion
    
    historial = [x0, x1]
    
    try:
        fx0 = evaluar_funcion(funcion_str, x0)
        fx1 = evaluar_funcion(funcion_str, x1)
    except Exception as e:
        return None, 0, historial, f"Error al evaluar función inicial: {e}"
    
    for i in range(max_iter):
        try:
            # Verificar que no haya división por cero
            if abs(fx1 - fx0) < 1e-12:
                return None, i + 1, historial, "Error: División por cero. Los valores de función son muy cercanos"
            
            # Calcular nueva aproximación
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            fx2 = evaluar_funcion(funcion_str, x2)
            
            historial.append(x2)
            
            # Verificar convergencia
            if abs(x2 - x1) < tolerancia or abs(fx2) < tolerancia:
                return x2, i + 1, historial, None
            
            # Verificar divergencia
            if abs(x2) > 1e10:
                return None, i + 1, historial, "Error: El método diverge. Intente con otros valores iniciales"
            
            # Actualizar valores
            x0, fx0 = x1, fx1
            x1, fx1 = x2, fx2
            
        except Exception as e:
            return None, i + 1, historial, f"Error durante la iteración: {e}"
    
    return x1, max_iter, historial, "Advertencia: Se alcanzó el máximo de iteraciones"
