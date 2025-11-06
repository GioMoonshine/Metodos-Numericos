def metodo_fixed_point(funcion_str, x0, tolerancia=1e-10, max_iter=1000):
    """
    Método de Punto Fijo para encontrar raíces
    
    Encuentra x tal que x = g(x), donde g(x) debe ser reformulada por el usuario
    Para resolver f(x) = 0, se debe reformular como x = g(x)
    
    Parámetros:
    - funcion_str: función g(x) como string (reformulación de f(x)=0 como x=g(x))
    - x0: aproximación inicial
    - tolerancia: tolerancia para el criterio de parada
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - historial: lista con las aproximaciones en cada iteración
    - error: mensaje de error si existe
    """
    from .utilidades import evaluar_funcion
    
    historial = []
    x = x0
    
    for i in range(max_iter):
        try:
            x_nuevo = evaluar_funcion(funcion_str, x)
            historial.append(x_nuevo)
            
            # Verificar convergencia
            if abs(x_nuevo - x) < tolerancia:
                return x_nuevo, i + 1, historial, None
            
            # Verificar divergencia
            if abs(x_nuevo) > 1e10:
                return None, i + 1, historial, "Error: El método diverge. Intente con otra función g(x) o valor inicial"
            
            x = x_nuevo
            
        except Exception as e:
            return None, i + 1, historial, f"Error durante la iteración: {e}"
    
    return x, max_iter, historial, "Advertencia: Se alcanzó el máximo de iteraciones"
