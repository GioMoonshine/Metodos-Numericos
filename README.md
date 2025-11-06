# Métodos Numéricos
Tarea de Electivo de especialidad - Métodos Numéricos.

===========================================================================

CÓMO USAR:
----------
1. Asegúrese de tener Python 3 y NumPy instalados
2. Ejecute el archivo principal: python main.py
3. Seleccione el método deseado
4. Ingrese la función y los datos requeridos
5. Visualice los resultados
----------

MÉTODOS DISPONIBLES:
--------------------
MÉTODOS CERRADOS (requieren intervalo [a, b]):
   1. Bisección
      - Divide el intervalo por la mitad
      - Muy robusto pero puede ser lento
      - Requiere cambio de signo en [a, b]

   2. Regula Falsi (Falsa Posición)
      - Usa interpolación lineal
      - Generalmente más rápido que bisección
      - Requiere cambio de signo en [a, b]

MÉTODOS ABIERTOS (requieren valor(es) inicial(es)):
   3. Fixed Point (Punto Fijo)
      - Requiere reformular f(x)=0 como x=g(x)
      - Convergencia depende de |g'(x)| < 1
      - Un solo valor inicial

   4. Newton-Raphson
      - Usa la derivada de la función
      - Convergencia cuadrática (muy rápido)
      - Puede calcular derivada numéricamente
      - Sensible al valor inicial

   5. Secante
      - Similar a Newton pero sin derivada
      - Usa dos valores iniciales
      - Buenos resultados en la mayoría de casos

MÉTODOS HÍBRIDOS:
   6. Brent
      - Combina bisección, secante e interpolación cuadrática
      - Uno de los más robustos y eficientes
      - Requiere intervalo [a, b] con cambio de signo
--------------------

EJEMPLOS DE USO:
----------------
Ejemplo 1: Bisección
   Función: x**3 - x - 2
   Intervalo: a = 1, b = 2
   Resultado: x ≈ 1.5213797068

Ejemplo 2: Newton-Raphson
   Función: x**2 - 2
   Derivada: 2*x (o dejar en blanco para cálculo automático)
   Valor inicial: x0 = 1
   Resultado: x ≈ 1.4142135624 (√2)

Ejemplo 3: Fixed Point
   Para resolver x**2 - 5 = 0:
   Reformular como: x = sqrt(5)
   Función g(x): sqrt(5)
   Valor inicial: x0 = 2
   Resultado: x ≈ 2.2360679775 (√5)

Ejemplo 4: Secante
   Función: exp(x) - 3*x
   Valores iniciales: x0 = 0, x1 = 1
   Resultado: x ≈ 0.6190612867
----------------

FUNCIONES MATEMÁTICAS DISPONIBLES:
-----------------------------------
- Operaciones: +, -, *, /, ** (potencia)
- Trigonométricas: sin(), cos(), tan()
- Exponencial/Logaritmo: exp(), log()
- Raíz cuadrada: sqrt()
- Valor absoluto: abs()
- Constantes: pi, e
-----------------------------------

TOLERANCIA Y MÁXIMO DE ITERACIONES:
------------------------------------
Por defecto:
- Tolerancia: 1e-10
- Máximo de iteraciones: 1000

Estos valores están definidos en cada método y pueden modificarse si es necesario.
------------------------------------

CONSEJOS PARA CADA MÉTODO:
---------------------------
Bisección:
- Asegúrese de que f(a) y f(b) tengan signos opuestos
- Use cuando necesite garantía de convergencia

Regula Falsi:
- Similar a bisección pero más rápido
- Buena primera opción para métodos cerrados

Fixed Point:
- La reformulación x = g(x) es crucial
- Para f(x) = 0, puede usar: x = x + α·f(x) con α pequeño
- Si diverge, intente otra reformulación

Newton-Raphson:
- Excelente convergencia si el valor inicial está cerca de la raíz
- Si no conoce la derivada, déjela en blanco
- Si diverge, cambie el valor inicial

Secante:
- Buenos resultados sin necesitar derivada
- Los dos valores iniciales deben estar razonablemente cerca de la raíz

Brent:
- Método más robusto disponible
- Use cuando otros métodos fallen
- Combina robustez y eficiencia
---------------------------

SOLUCIÓN DE PROBLEMAS:
----------------------
Error: "La función debe tener signos opuestos"
- Verifique que f(a) y f(b) tengan signos diferentes
- Pruebe otro intervalo o use un método abierto

Error: "El método diverge"
- Cambie el(los) valor(es) inicial(es)
- Intente con un método más robusto (Brent, Bisección)

Error: "Derivada cercana a cero"
- El método de Newton encontró un punto plano
- Cambie el valor inicial

Error: "División por cero"
- Valores muy cercanos en método de Secante
- Use valores iniciales más separados

Advertencia: "Se alcanzó el máximo de iteraciones"
- La función puede no tener raíz en la región
- Aumente max_iter o cambie parámetros
----------------------

INFORMACIÓN TÉCNICA:
--------------------
Criterios de convergencia:
- |f(x)| < tolerancia
- |x_nuevo - x_anterior| < tolerancia
- |b - a| < tolerancia (métodos de intervalo)

Detección de divergencia:
- |x| > 1e10 (valor muy grande)
- Derivada o denominador cercano a cero

Cálculo de derivada numérica:
- Método: Diferencias centradas
- Fórmula: f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
- h = 1e-8 (tamaño del paso)
--------------------

===========================================================================
