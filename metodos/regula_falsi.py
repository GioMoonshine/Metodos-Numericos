# from .utilidades import evaluar_funcion, verificar_cambio_signo

def metodo_regula_falsi(funcion_str, a, b, tolerancia=1e-10, max_iter=1000):
    """
    Método de Regula Falsi (Falsa Posición) para encontrar raíces
    
    Parámetros:
    - funcion_str: función como string (usar 'x' como variable)
    - a, b: intervalo inicial [a, b]
    - tolerancia: tolerancia para el criterio de parada
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - raiz: aproximación de la raíz
    - iteraciones: número de iteraciones realizadas
    - historial: lista con las aproximaciones en cada iteración
    - error: mensaje de error si existe
    """
    from .utilidades import evaluar_funcion, verificar_cambio_signo
    
    # Verificar cambio de signo
    try:
        tiene_cambio, fa, fb = verificar_cambio_signo(funcion_str, a, b)
        if not tiene_cambio:
            return None, 0, [], "Error: La función debe tener signos opuestos en los extremos del intervalo"
    except Exception as e:
        return None, 0, [], str(e)
    
    historial = []
    c_anterior = a
    
    for i in range(max_iter):
        # Calcular punto de intersección de la recta secante
        c = b - (fb * (b - a)) / (fb - fa)
        fc = evaluar_funcion(funcion_str, c)
        
        historial.append(c)
        
        # Verificar convergencia
        if abs(fc) < tolerancia or abs(c - c_anterior) < tolerancia:
            return c, i + 1, historial, None
        
        # Actualizar intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        c_anterior = c
    
    return c, max_iter, historial, "Advertencia: Se alcanzó el máximo de iteraciones"
