def metodo_brent(funcion_str, a, b, tolerancia=1e-10, max_iter=1000):
    """
    Algoritmo de Brent para encontrar raíces
    
    Combina bisección, secante e interpolación cuadrática inversa
    Es uno de los métodos más robustos y eficientes
    
    Parámetros:
    - funcion_str: función f(x) como string
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
    
    # Asegurar que |f(a)| >= |f(b)|
    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    
    c = a
    fc = fa
    mflag = True
    historial = []
    
    for i in range(max_iter):
        try:
            # Calcular s usando diferentes métodos
            if fa != fc and fb != fc:
                # Interpolación cuadrática inversa
                s = (a * fb * fc) / ((fa - fb) * (fa - fc)) + \
                    (b * fa * fc) / ((fb - fa) * (fb - fc)) + \
                    (c * fa * fb) / ((fc - fa) * (fc - fb))
            else:
                # Método de la secante
                s = b - fb * (b - a) / (fb - fa)
            
            # Condiciones para aceptar s
            temp1 = (3 * a + b) / 4
            cond1 = not ((s > min(temp1, b) and s < max(temp1, b)))
            cond2 = mflag and abs(s - b) >= abs(b - c) / 2
            cond3 = not mflag and abs(s - b) >= abs(c - d) / 2
            cond4 = mflag and abs(b - c) < tolerancia
            cond5 = not mflag and abs(c - d) < tolerancia
            
            # Si no se cumplen las condiciones, usar bisección
            if cond1 or cond2 or cond3 or cond4 or cond5:
                s = (a + b) / 2
                mflag = True
            else:
                mflag = False
            
            fs = evaluar_funcion(funcion_str, s)
            historial.append(s)
            
            # Verificar convergencia
            if abs(fs) < tolerancia or abs(b - a) < tolerancia:
                return s, i + 1, historial, None
            
            d = c
            c = b
            fc = fb
            
            # Actualizar intervalo
            if fa * fs < 0:
                b = s
                fb = fs
            else:
                a = s
                fa = fs
            
            # Asegurar que |f(a)| >= |f(b)|
            if abs(fa) < abs(fb):
                a, b = b, a
                fa, fb = fb, fa
                
        except Exception as e:
            return None, i + 1, historial, f"Error durante la iteración: {e}"
    
    return s, max_iter, historial, "Advertencia: Se alcanzó el máximo de iteraciones"
