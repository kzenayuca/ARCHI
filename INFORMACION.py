ENCYCLOPEDIA_DATA = {
    "  Electrónica digital y circuitos lógicos": {
        "title": "Electronica Digital y Circuitos Logicos",
        "content": (
            "[SUBTITLE]ALGEBRA DE BOOLE:[/SUBTITLE]\n"
            "El álgebra de Boole es un sistema matemático que se utiliza para representar y manipular expresiones lógicas. "
            "Fue desarrollado por George Boole en el siglo XIX y es fundamental para el diseño de circuitos digitales. "
            "En el álgebra de Boole, las variables pueden tomar dos valores: verdadero (1) o falso (0). "
            "Las operaciones básicas son AND (conjunción), OR (disyunción) y NOT (negación). "
            "Estas operaciones se pueden combinar para formar expresiones más complejas. "
            "Este es el fundamento matemático para el diseño de circuitos digitales. Define operaciones lógicas con variables binarias (0 y 1).\n\n "
            
            "[SUBTITLE]Postulados básicos:[/SUBTITLE]\n"
            "• [BOLD]Postulado 1:[/BOLD] Si A ≠ 0, entonces A = 1; Si A ≠ 1, entonces A = 0\n"
            "• [BOLD]Postulado 2:[/BOLD] 0 · 0 = 0, 1 + 1 = 1\n"
            "• [BOLD]Postulado 3:[/BOLD] 1 · 1 = 1, 0 + 0 = 0\n"
            "• [BOLD]Postulado 4:[/BOLD] Si A = 0, entonces Ā = 1; Si A = 1, entonces Ā = 0\n"
            "• [BOLD]Postulado 5:[/BOLD] 0 + 1 = 1 + 0 = 1\n"
            "• [BOLD]Postulado 6:[/BOLD] 1 · 0 = 0 · 1 = 0\n\n"
            "[SUBTITLE]Leyes Fundamentales del Álgebra de Boole:[/SUBTITLE]\n"
            "• [BOLD]Ley Conmutativa:[/BOLD]\n"
            "  - A + B = B + A (suma)\n"
            "  - A · B = B · A (producto)\n\n"
            "• [BOLD]Ley Asociativa:[/BOLD]\n"
            "  - (A + B) + C = A + (B + C)\n"
            "  - (A · B) · C = A · (B · C)\n\n"
            "• [BOLD]Ley Distributiva:[/BOLD]\n"
            "  - A · (B + C) = (A · B) + (A · C)\n"
            "  - A + (B · C) = (A + B) · (A + C)\n\n"
            "• [BOLD]Leyes de Identidad:[/BOLD]\n"
            "  - A + 0 = A\n"
            "  - A · 1 = A\n\n"
            "• [BOLD]Leyes de Complemento:[/BOLD]\n"
            "  - A + Ā = 1\n"
            "  - A · Ā = 0\n\n"
            "• [BOLD]Leyes de Idempotencia:[/BOLD]\n"
            "  - A + A = A\n"
            "  - A · A = A\n\n"
            "• [BOLD]Leyes de Absorción:[/BOLD]\n"
            "  - A + (A · B) = A\n"
            "  - A · (A + B) = A\n\n"
            "• [BOLD]Leyes de De Morgan:[/BOLD]\n"
            "  - (A + B)‾ = Ā · B̄\n"
            "  - (A · B)‾ = Ā + B̄\n\n"
            "[SUBTITLE]Teoremas clave:[/SUBTITLE]\n"
            "- [BOLD]De Morgan:[/BOLD] (A+B)' = A'·B'; (A·B)' = A' + B'.\n"
            "- [BOLD]Absorción:[/BOLD] A + A·B = A; A·(A+B) = A.\n"
            "[SUBTITLE]Aplicaciones:[/SUBTITLE]\n"
            "- Diseño de circuitos digitales (compuertas lógicas).\n"
            "- Simplificación de expresiones lógicas.\n"
            "- Análisis de circuitos lógicos. \n\n"

            "[SUBTITLE]COMPUERTAS LÓGICAS BÁSICAS Y LOS CIRCUITOS LÓGICOS:[/SUBTITLE]\n"
            "Los circuitos lógicos son la base fundamental de todos los sistemas digitales modernos. "
            "Estos circuitos procesan información mediante señales binarias (0 y 1) y realizan operaciones lógicas "
            "basadas en el álgebra de Boole. Constituyen los bloques de construcción esenciales para procesadores, "
            "memorias, controladores y cualquier dispositivo digital.\n"
            "Las compuertas lógicas son circuitos electrónicos que implementan las operaciones del álgebra de Boole. "
            "Cada compuerta realiza una función lógica específica con una o más entradas y una salida.\n\n"

            "[SUBTITLE]1. COMPUERTA AND (Y):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-and.jpeg]\n"
            "• [BOLD]Función:[/BOLD] Realiza la multiplicación lógica\n"
            "• [BOLD]Símbolo:[/BOLD] Forma de D con entrada plana\n"
            "• [BOLD]Operación:[/BOLD] Y = A · B\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 0\n"
            "  0 | 1 | 0\n"
            "  1 | 0 | 0\n"
            "  1 | 1 | 1\n"
            "• [BOLD]Características:[/BOLD] La salida es 1 solo cuando TODAS las entradas son 1\n"
            "• [BOLD]Aplicaciones:[/BOLD] Habilitación de señales, multiplicación binaria, filtros digitales\n"
            "• [BOLD]Implementación:[/BOLD] Transistores en serie (lógica TTL) o CMOS\n\n"

            "[SUBTITLE]2. COMPUERTA OR (O):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-or.jpeg]\n"
            "• [BOLD]Función:[/BOLD] Realiza la suma lógica\n"
            "• [BOLD]Símbolo:[/BOLD] Forma curva cóncava\n"
            "• [BOLD]Operación:[/BOLD] Y = A + B\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 0\n"
            "  0 | 1 | 1\n"
            "  1 | 0 | 1\n"
            "  1 | 1 | 1\n"
            "• [BOLD]Características:[/BOLD] La salida es 1 cuando AL MENOS una entrada es 1\n"
            "• [BOLD]Aplicaciones:[/BOLD] Combinación de señales, alarmas, sistemas de seguridad\n"
            "• [BOLD]Implementación:[/BOLD] Transistores en paralelo\n\n"

            "[SUBTITLE]3. COMPUERTA NOT (INVERSOR):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-not.jpeg]\n"
            "• [BOLD]Función:[/BOLD] Realiza la negación lógica\n"
            "• [BOLD]Símbolo:[/BOLD] Triángulo con círculo pequeño en la salida\n"
            "• [BOLD]Operación:[/BOLD] Y = Ā\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | Y\n"
            "  0 | 1\n"
            "  1 | 0\n"
            "• [BOLD]Características:[/BOLD] La salida es el complemento de la entrada\n"
            "• [BOLD]Aplicaciones:[/BOLD] Inversión de señales, creación de señales complementarias\n"
            "• [BOLD]Implementación:[/BOLD] Transistor único con resistencia de pull-up\n\n"

            "[SUBTITLE]COMPUERTAS LÓGICAS DERIVADAS:[/SUBTITLE]\n"
            "Estas compuertas se forman combinando las compuertas básicas:\n\n"

            "[SUBTITLE]4. COMPUERTA NAND (NO-Y):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-nand.jpeg]\n"
            "• [BOLD]Función:[/BOLD] AND seguida de NOT\n"
            "• [BOLD] Símbolo:[/BOLD] Compuerta AND con círculo en la salida\n"
            "• [BOLD]Operación:[/BOLD] Y = (A · B)‾ = Ā + B̄\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 1\n"
            "  0 | 1 | 1\n"
            "  1 | 0 | 1\n"
            "  1 | 1 | 0\n"
            "• [BOLD]Características:[/BOLD] Salida 0 solo cuando todas las entradas son 1\n"
            "• [BOLD]Importancia:[/BOLD] Compuerta universal (puede implementar cualquier función lógica)\n"
            "• [BOLD]Aplicaciones:[/BOLD] Construcción de otros tipos de compuertas, memorias\n\n"

            "[SUBTITLE]5. COMPUERTA NOR (NO-O):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-nor.jpeg]\n"
            "• [BOLD]Función:[/BOLD] OR seguida de NOT\n"
            "• [BOLD]Símbolo:[/BOLD] Compuerta OR con círculo en la salida\n"
            "• [BOLD]Operación:[/BOLD] Y = (A + B)‾ = Ā · B̄\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 1\n"
            "  0 | 1 | 0\n"
            "  1 | 0 | 0\n"
            "  1 | 1 | 0\n"
            "• [BOLD]Características:[/BOLD] Salida 1 solo cuando todas las entradas son 0\n"
            "• [BOLD]Importancia:[/BOLD] También es compuerta universal\n\n"

            "[SUBTITLE]6. COMPUERTA XOR (OR EXCLUSIVO):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-xor.jpeg]\n"
            "• [BOLD]Función:[/BOLD] OR exclusivo\n"
            "• [BOLD]Símbolo:[/BOLD] Compuerta OR con línea curva adicional en la entrada\n"
            "• [BOLD]Operación:[/BOLD] Y = A ⊕ B = A·B̄ + Ā·B\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 0\n"
            "  0 | 1 | 1\n"
            "  1 | 0 | 1\n"
            "  1 | 1 | 0\n"
            "• [BOLD]Características:[/BOLD] Salida 1 cuando las entradas son diferentes\n"
            "• [BOLD]Aplicaciones:[/BOLD] Sumadores binarios, detectores de paridad, comparadores\n\n"

            "[SUBTITLE]7. COMPUERTA XNOR (NOR EXCLUSIVO):[/SUBTITLE]\n"
            "\n[IMAGE:Imagenes/compuerta-xnor.jpeg]\n"
            "• [BOLD]Función:[/BOLD] XOR seguida de NOT\n"
            "• [BOLD]Símbolo:[/BOLD] XOR con círculo en la salida\n"
            "• [BOLD]Operación:[/BOLD] Y = (A ⊕ B)‾ = A·B + Ā·B̄\n"
            "• [BOLD]Tabla de Verdad:[/BOLD]\n"
            "  A | B | Y\n"
            "  0 | 0 | 1\n"
            "  0 | 1 | 0\n"
            "  1 | 0 | 0\n"
            "  1 | 1 | 1\n"
            "• [BOLD]Características:[/BOLD] Salida 1 cuando las entradas son iguales\n"
            "• [BOLD]Aplicaciones:[/BOLD] Comparadores de igualdad, codificadores\n\n"

            "[SUBTITLE]CIRCUITOS LÓGICOS COMBINACIONALES:[/SUBTITLE]\n"
            "Los circuitos combinacionales son aquellos donde las salidas dependen únicamente "
            "del estado actual de las entradas, sin memoria de estados previos.\n\n"

            "  [SUBTITLE]Características de los Circuitos Combinacionales:[/SUBTITLE]\n"
            "• No tienen elementos de memoria (sin realimentación)\n"
            "• Las salidas cambian inmediatamente cuando cambian las entradas\n"
            "• Se describen completamente mediante tablas de verdad\n"
            "• Se analizan usando álgebra de Boole\n"
            "• Tiempo de propagación finito pero sin estados internos\n\n"

            "[SUBTITLE]Proceso de Diseño de Circuitos Combinacionales:[/SUBTITLE]\n"
            "1. Definición del problema y especificación de entradas/salidas\n"
            "2. Construcción de la tabla de verdad\n"
            "3. Obtención de las expresiones booleanas (suma de productos o producto de sumas)\n"
            "4. Simplificación de las expresiones (mapas de Karnaugh, método algebraico)\n"
            "5. Implementación del circuito con compuertas lógicas\n"
            "6. Verificación y optimización\n\n"

            "[SUBTITLE]Simplificación con Mapas de Karnaugh\n[/SUBTITLE]"
            "\n"
            "\n[IMAGE:Imagenes/mapa-de-karnaugh.jpeg]\n"
            "\n"
            "[BOLD]Método gráfico para minimizar funciones lógicas.[/BOLD] "
            "Pasos: "
            "1. Construir una tabla con celdas agrupadas en potencias de 2 (1, 2, 4, 8). \n"
            "2. Agrupar '1's adyacentes (horizontal o vertical, sin diagonales). \n"
            "3. Eliminar variables que cambian dentro del grupo. \n"
            "[BOLD]Ejemplo:[/BOLD] F(A,B,C) = Σ(0, 2, 4, 5, 6) → Grupos: A'C' + AB'. \n"
            "[BOLD]Ventajas:[/BOLD] \n"
            "- Visual y rápida.\n "   
            "- Reduce errores humanos.\n "
            "- Útil para funciones con hasta 6 variables. \n\n"

            "[SUBTITLE]MULTIPLEXORES (MUX) y DEMULTIPLEXORES (DEMUX)[/SUBTITLE]\n"
            "[BOLD]Multiplexor (MUX): Selecciona una de varias entradas usando líneas de control. \n"
            "- Ejemplo: MUX 4:1 usa 2 bits de control (S0, S1) para elegir entre 4 entradas (D0-D3).\n " 
            "- Aplicación: Transmisión de datos en buses.\n " +
            "[BOLD]Demultiplexor (DEMUX):[/BOLD] Distribuye una entrada a una de varias salidas.\n " 
            "- Ejemplo: DEMUX 1:4 envía la entrada a Y0-Y3 según S0-S1. \n" 
            "- Usado en decodificación de direcciones de memoria.\n\n "
            "\n"
            "[IMAGE:Imagenes/mux-y-demux.jpeg]"
            "\n"
            "[SUBTITLE]Decodificador BCD a 7 Segmentos[/SUBTITLE] \n"
            "Convierte un número BCD (4 bits) en señales para display de 7 segmentos. \n"
            "\n[IMAGE:Imagenes/decodificador-bcd-a-7-segmentos.jpeg]\n"
            "[BOLD]Funcionamiento:[/BOLD] \n"
            "- Cada segmento (a-g) se activa según combinaciones BCD (ejemplo: '5' → a=0, b=1, c=1, d=1, e=0, f=1, g=1). \n"
            "- Circuito típico: IC 7447 (decodificador BCD a 7 segmentos con salidas activas en bajo).\n "
            "[BOLD]Ejemplo práctico:[/BOLD] Calculadoras y relojes digitales. \n\n"

            "[SUBTITLE]ALU Básica (Unidad Aritmético-Lógica)[/SUBTITLE]\n"
            "Componente central de la CPU para operaciones aritméticas y lógicas. "
            "[BOLD]Componentes:[/BOLD] "
            "- Sumador completo: Realiza sumas binarias con acarreo (usado en operaciones ADD).\n "
            "- Comparador: Determina si A > B, A < B, o A = B (usando XOR y AND). \n"
            "- Circuito lógico: Implementa AND, OR, NOT, etc.\n "
            "[BOLD]Ejemplo:[/BOLD] ALU de 4 bits (SN74181) puede sumar, restar, AND, OR, etc. \n\n"

            "[SUBTITLE]Flip-Flops (Biestables)[/SUBTITLE]\n"
            "Dispositivos secuenciales que almacenan 1 bit. Requieren señal de reloj (CLK). "
            "[BOLD]Tipos:[/BOLD] "
            "- SR (Set-Reset): S=1 pone Q=1; R=1 pone Q=0; S=R=1 prohibido.\n "
            "- D (Data): Almacena el valor de D en el flanco de CLK.\n "
            "- JK: Mejora del SR; J=K=1 invierte el estado.\n "
            "- T (Toggle): Cambia de estado si T=1 en el flanco de CLK.\n "
            "[BOLD]Aplicación:[/BOLD] Registros, contadores, y memoria caché. \n\n"

            "\n[IMAGE:Imagenes/ff-sr-negativo.jpeg]\n"
            "\n[IMAGE:Imagenes/ff-sr-positivo.jpeg]\n"
            "\n[IMAGE:Imagenes/ff-jk-negativo.jpeg]\n"
            "\n[IMAGE:Imagenes/ff-jk-positivo.jpeg]\n"

            "[SUBTITLE]REGISTROS[/SUBTITLE]\n"
            "Son pequeñas memorias dentro de la CPU para almacenar datos temporalmente. "
            "Un registro es un conjunto de flip-flops (bistables) que almacena un conjunto de bits."
            "Generalmente, los registros están contenidos dentro de la unidad central de procesamiento (CPU) o en dispositivos periféricos."
            "Se utilizan para almacenar datos temporalmente durante el procesamiento.\n"

            "[BOLD]Características:[/BOLD] "
            "- Tamaño: Varía según la arquitectura (ej. 8, 16, 32, 64 bits).\n "
            "- Velocidad: Acceso rápido comparado con memoria RAM.\n "
            "[BOLD]Tipos:[/BOLD]\n "
            "- Registros de propósito general(GPRs) : Usados para operaciones aritméticas y lógicas. Ejemplo: AX, BX, CX, DX en arquitecturas x86 "
            "- Registros de propósito específico: Usados para almacenar direcciones, datos de control y resultados de operaciones." +
            " Controlan el flujo de datos en la CPU. Ejemplo: PC (contador de programa), SP (pila), IR (registro de instrucción).\n "
            "Ejemplo: Registro de desplazamiento (Shift Register) para mover bits.\n "   
            "- Registros de datos: Almacenan información que va a ser procesada o ya fue procesada."
            "Ejemplo: Registro de datos en una ALU para almacenar resultados intermedios.\n "
            "- Registros de dirección: Almacenan direcciones de memoria para acceder a datos específicos."
            "Ejemplo: Registro de dirección de memoria (MAR) que contiene la dirección de la memoria que se va a leer o escribir.\n "
            "Ejemplo: Registro de desplazamiento (Shift Register) para mover bits.\n "
            "- Registros de estado / bandera: Indican el estado de la CPU (banderas como carry, zero, overflow). "
            "Ejemplo: Registro de estado (PSR) que contiene banderas de condición como C (carry), Z (zero), N (negative), V (overflow).\n "
            "Ejemplo: Registro de desplazamiento (Shift Register) para mover bits.\n\n "
            "[BOLD]Aplicaciones:[/BOLD]"
            "- Almacenamiento temporal de datos durante cálculos.\n "
            "- Transferencia de datos entre la CPU y otros componentes.\n "
            "- Implementación de instrucciones de la CPU y operaciones aritméticas y lógicas.\n "
            "- Control del flujo de ejecución de programas.\n\n "

            "[SUBTITLE]CONTADORES[/SUBTITLE]\n"
            "Circuitos que generan secuencias binarias en respuesta a pulsos de CLK. \n"
            "[BOLD]Tipos:[/BOLD]\n "
            "- Asíncrono (Ripple): Flip-flops no sincronizados (ejemplo: 74HC93). \n"
            "- Síncrono: Todos los FF cambian con el mismo CLK (más rápido y preciso). \n"
            "[BOLD]Aplicación:[/BOLD] Divisores de frecuencia, temporizadores.\n "
            "Ejemplo: Contador ascendente de 4 bits (0 a 15) con flip-flops JK.\n "
            "[BOLD]Contador descendente:[/BOLD] Similar, pero cuenta hacia abajo. \n"
            "Ejemplo: Contador descendente de 4 bits (15 a 0) con flip-flops JK.\n "
            "[BOLD]Contador de anillo:[/BOLD] Crea una secuencia cíclica (ejemplo: 74HC590).\n "
            "[BOLD]Contador Johnson:[/BOLD] Variante del contador de anillo con más eficiencia. \n\n"

            "[SUBTITLE]SRAM vs DRAM[/SUBTITLE]\n"
            "[BOLD]SRAM (Static RAM):[/BOLD]\n "
            "- Usa 6 transistores por bit (flip-flops). \n"
            "- Más rápida y cara (caché de CPU). \n"
            "- No requiere refresco. \n"
            "[BOLD]DRAM (Dynamic RAM):[/BOLD] \n"
            "- Usa 1 transistor + 1 capacitor por bit. \n"
            "- Más lenta, densa y barata (RAM principal). \n"
            "- Necesita refresco periódico. \n\n"

            "[SUBTITLE]ROM, PROM, EPROM, EEPROM[/SUBTITLE]\n"
            "ROM (Read-Only Memory): Programada en fábrica (ejemplo: BIOS antiguo).\n " 
            "Tipos de ROM:\n"
            "- ROM: No reprogramable, solo lectura. \n"
            "PROM (Programmable ROM): Programable una vez con fusibles. \n"
            "Tipos de PROM:\n"
            "- PROM: Programable una vez, no reprogramable. \n"
            "EPROM (Erasable Programmable ROM): Borrable con luz UV (ejemplo: BIOS actualizable).\n "
            "Tipos de EPROM:\n"
            "- EPROM: Borrable con luz UV, reprogramable. \n"   
            "EEPROM (Electrically Erasable PROM): Borrable eléctricamente (ejemplo: almacenamiento de configuración).\n "
            "Tipos de EEPROM:\n"
            "- EEPROM: Borrable eléctricamente, reprogramable. \n"
            "Flash: Variante de EEPROM para alta densidad (USB, SSDs). \n\n"

            "[SUBTITLE]Arquitecturas de Memoria[/SUBTITLE]\n"
            "[BOLD]Von Neumann:[/BOLD]\n "
            "- Tanto los datos como las instrucciones se almacenan en la misma memoria. \n"
            "- Usada en la mayoría de las computadoras modernas (ejemplo: PC, laptops).\n "
            "- Un solo bus se utiliza para transferir tanto datos como instrucciones entre la memoria y la unidad de procesamiento. \n"
            "- La arquitectura Von Neumann es más simple de implementar y, por lo tanto, generalmente más económica.'\n "
            "- Cuello de botella de memoria: El acceso secuencial a datos e instrucciones puede crear un cuello de botella, limitando el rendimiento. \n "
            "[BOLD]Ejemplo moderno:[/BOLD] RAM principal en PCs y laptops.\n\n "
            "[BOLD]Harvard:[/BOLD] \n"
            "- Usada en DSPs y microcontroladores (ejemplo: PIC). \n"
            "- Los datos y las instrucciones se almacenan en memorias separadas (memoria de datos y memoria de instrucciones). \n"
            "- Se utilizan buses de direcciones y de datos separados para acceder a las memorias de datos e instrucciones. \n"
            "- Permite acceder a datos e instrucciones simultáneamente, lo que puede resultar en un mayor rendimiento. \n"
            "- Mayor complejidad y costo: La arquitectura Harvard es más compleja de implementar y, por lo tanto, más costosa. \n"
            "[BOLD]Ejemplo moderno:[/BOLD] Microcontroladores como Arduino usan Harvard.\n"
        ),
        "url": "https://wayground.com/admin/assessment/6881a3a742ac6dbdf316bdab?source=lesson_share"
    },

    "  Sistemas numéricos": {
        "title": "Sistemas Numéricos",
        "content": (
            "En la tecnología digital se utilizan muchos sistemas numéricos. Los más comunes son los siguientes: "
            "decimal, binario, octal y hexadecimal. Siendo el sistema decimal el más conocido, de uso diario. "
            "Analicemos algunas de sus características para ayudarnos a comprender los demás sistemas numéricos.\n\n"
            "[IMAGE:Imagenes/sistemas-de-numeracion.jpeg]"
            "[SUBTITLE]Sistema Decimal:[/SUBTITLE]\n"
            "El sistema decimal se conoce también como sistema de base 10 ya que tiene 10 dígitos: 0 al 9. "
            "Es un sistema de valor posicional. Si usamos sólo dos lugares decimales, podemos contar hasta 10^2 = 100 números distintos (0 a 99). "
            "Con tres lugares, hasta 10^3 = 1000 (0 a 999). En general, con N dígitos podemos contar hasta 10^N - 1.\n\n"
            "[BOLD]Ventaja:[/BOLD] Intuitivo para humanos.\n\n" +
            "[BOLD]Ejemplo 1:[/BOLD] `345₁₀ = 3*10² + 4*10¹ + 5*10⁰`.\n" +
            "[BOLD]Ejemplo 2:[/BOLD] `12.34₁₀ = 1*10¹ + 2*10⁰ + 3*10⁻¹ + 4*10⁻²`.\n\n" +
            "[BOLD]Limitaciones en computación:[/BOLD]\n" +
            "- Ineficiente para hardware digital (requiere conversión a binario).\n\n"

            "\n[IMAGE:Imagenes/sistema-decimal.jpeg]\n"

            "[SUBTITLE]Sistema Binario:[/SUBTITLE]\n"
            "Solo hay dos símbolos: 0 y 1. Es de base 2, y aunque requiere más dígitos, puede representar cualquier cantidad. "
            "Lenguaje nativo de las computadoras y sistemas digitales. "
            "Un bit es un dígito binario. MSB (más significativo) está a la izquierda, LSB (menos significativo) a la derecha. "
            "Entonces, 4 bits a la izquierda del punto binario y 3 a la derecha representan partes enteras y fraccionarias.\n"
            "[BOLD]Ejemplo 1:[/BOLD] `1010₂ = 1*2³ + 0*2² + 1*2¹ + 0*2⁰ = 10₁₀`.\n" +
            "[BOLD]Ejemplo 2:[/BOLD] `110.101₂ = 1*2² + 1*2¹ + 0*2⁰ + 1*2⁻¹ + 0*2⁻² + 1*2⁻³ = 6.625₁₀`.\n\n"
            "[BOLD]Casos de Uso:[/BOLD]\n" +
            "- Máscaras de red (IPv4).\n" +
            "- Permisos en sistemas UNIX (chmod).\n\n"
            "\n[IMAGE:Imagenes/sistema-binario.jpeg]\n"

            "[SUBTITLE]Sistema Hexadecimal:[/SUBTITLE]\n"
            "Es un sistema de base 16. Usa dígitos del 0 al 9 y letras A a F, donde A=10 hasta F=15. "
            "Muy usado en informática porque cada dígito hexadecimal representa 4 bits binarios."
            "Relación con binario: 1 dígito hex = 4 bits.\n"
            "[BOLD]Ejemplo 1:[/BOLD] `1A3F₁₆ = 1*16³ + 10*16² + 3*16¹ + 15*16⁰ = 6719₁₀`.\n"
            "[BOLD]Ejemplo 2:[/BOLD] `A3F₁₆ = 10*16² + 3*16¹ + 15*16⁰ = 2623₁₀`.\n\n" +
            "[BOLD]Aplicaciones críticas:[/BOLD]\n" +
            "- Direcciones de memoria (`0xFFFF`).\n" +
            "- Representación de colores (HTML/CSS: `#FF5733`).\n\n"
            "\n[IMAGE:Imagenes/sistema-hexadecimal.jpeg]\n"
            
            "\n[IMAGE:Imagenes/sistema-octal.jpeg]\n"

            "[SUBTITLE]Binario a Decimal:[/SUBTITLE]\n" +
            "Sumar pesos de cada bit activo (1).\n" +
            "`1011₂ = 1*2³ + 0*2² + 1*2¹ + 1*2⁰ = 11₁₀`\n\n" +
            "[SUBTITLE]Decimal a Binario:[/SUBTITLE]\n" +
            "División sucesiva entre 2 y leer residuos en orden inverso.\n" +
            "`13₁₀ → 13/2=6 residuo 1 → 6/2=3 residuo 0 → ... = 1101₂`"

            "\n[IMAGE:Imagenes/conversion-binario-a-decimal.jpeg]\n"
            "\n[IMAGE:Imagenes/conversion-decimal-a-binario.jpeg]\n"

            "[SUBTITLE]Binario a Hexadecimal:[/SUBTITLE]\n" +
            "Agrupar bits de 4 en 4 (de derecha a izquierda).\n" +
            "`1100 1010₂ → CA₁₆`\n\n" +

            "\n[IMAGE:Imagenes/conversion-binario-a-hexadecimal.jpeg]\n"

            "[SUBTITLE]Hexadecimal a Binario:[/SUBTITLE]\n" +
            "Reemplazar cada dígito hex por sus 4 bits equivalentes.\n" +
            "`F3₁₆ → 1111 0011₂`\n\n"
            "[BOLD]Complemento a 1:[/BOLD]\n" +
            "Invertir todos los bits (`0101 → 1010`).\n" +
            "[BOLD]Complemento a 2:[/BOLD]\n" +
            "Complemento a 1 + 1 (`0101 → 1010 + 1 = 1011`).\n\n" +
            "[BOLD]Uso en números negativos:[/BOLD]\n" +
            "- Rango con 8 bits: -128 a +127 (Complemento a 2).\n" +
            "[BOLD]Ejemplo :[/BOLD]`-5₁₀ → 1111 1011₂` (8 bits).\n\n"

            "\n[IMAGE:Imagenes/conversion-hexadecimal-a-binario.jpeg]\n"


            "[SUBTITLE]Punto Flotante (IEEE 754)[/SUBTITLE]\n"
            "[BOLD]Estructura:[/BOLD]\n" +
            "- Signo: 1 bit (0=positivo, 1=negativo).\n" +
            "- Exponente: Sesgado (ej. 8 bits en precisión simple).\n" +
            "- Mantisa: Parte fraccionaria.\n\n" +
            "[BOLD]Ejemplo (32 bits):[/BOLD]\n" +
            "`0 10000010 10100000000000000000000`\n" +
            "- Signo: 0 (+)\n" +
            "- Exponente: 10000010₂ - 127 = 130 - 127 = 3\n" +
            "- Mantisa: 1.101₂ (implícito el 1)\n" +
            "- Valor: (-1)⁰ * 1.101₂ * 2³ = 1101₂ = 13₁₀\n\n"
            
            "\n[IMAGE:Imagenes/punto-flotante-ieee754.jpeg]\n"

            "[SUBTITLE]Operaciones Aritméticas en Binario:[/SUBTITLE]\n" +
            "[BOLD]Suma:[/BOLD]\n" +
            "[BOLD]Reglas:[/BOLD]\n" +
            "`0 + 0 = 0`, `0 + 1 = 1`, `1 + 1 = 10` (acarreo 1).\n" +
            "[BOLD]Ejemplo:[/BOLD]\n" +
            "```\n  1011₂ (11₁₀)\n+ 0110₂ (6₁₀)\n  -----\n 10001₂ (17₁₀)\n```\n\n" +
            "[BOLD]Resta (usando complemento a 2):[/BOLD]\n" +
            "`A - B = A + (-B)` donde `-B` es el complemento a 2 de B.\n" +
            "[BOLD]Ejemplo:[/BOLD] `7 - 5 = 7 + (-5)`\n" +
            "`-5₁₀ → 1011₂` (4 bits)\n" +
            "```\n  0111₂ (7₁₀)\n+ 1011₂ (-5₁₀)\n  -----\n  0010₂ (2₁₀) (ignorar acarreo)\n```\n\n" +
            "[BOLD]Multiplicación:[/BOLD]\n" +
            "[BOLD]Método:[/BOLD] Similar al decimal, pero más simple.\n" +
            "[BOLD]Pasos:[/BOLD]\n" +
            "1. Desplazamientos a la izquierda.\n" +
            "2. Sumas parciales.\n" +
            "[BOLD]Ejemplo:[/BOLD]\n" +
            "```\n    101₁₂ (5₁₀)\n  × 110₂ (6₁₀)\n    -----\n    000\n   101\n +101\n  -----\n 11110₂ (30₁₀)\n```\n" +
            "[BOLD]División:[/BOLD]\n" +
            "[BOLD]Método:[/BOLD] Similar al decimal, pero con restas sucesivas.\n" +
            "[BOLD]Algoritmo de Restauración:[/BOLD]\n" +
            "[BOLD]Pasos:[/BOLD]\n" +
            "1. Desplazar y comparar dividendo con divisor.\n" +
            "2. Restar si posible; restaurar si no.\n" +
            "[BOLD]Ejemplo:\n" +
            "`1101₂ (13₁₀) ÷ 0101₂ (5₁₀)`\n" +
            "```\nCociente: 0010₂ (2₁₀)\nResto: 0011₂ (3₁₀)\n```\n" +
            "[BOLD]Alternativa:[/BOLD] División no restauradora (más eficiente).\n\n"
        ),
        "url": "https://wayground.com/admin/assessment/6881a42712a64a936957c59a?source=lesson_share"
    },

    "  Sistemas digitales y sistemas analógicos": {
        "title": "Sistemas Digitales y Analógicos",
        "content": (
            "[SUBTITLE]Sistemas Digitales:[/SUBTITLE]\n"
            "Los sistemas digitales son combinaciones de dispositivos diseñados para manipular información lógica o cantidades físicas representadas en forma digital, donde las cantidades solo pueden tener valores discretos. "
            "Estos dispositivos generalmente son electrónicos, pero también pueden ser mecánicos, magnéticos o neumáticos. "
            "Los sistemas digitales más comunes incluyen computadoras, calculadoras digitales, equipos de audio y video digital, y el sistema telefónico (considerado el sistema digital más grande del mundo).\n\n"
            
            "\n[IMAGE:Imagenes/sistemas-digitales.jpeg] \n"

            "[SUBTITLE]Ventajas de los Sistemas Digitales:[/SUBTITLE]\n"
            "• Son más fáciles de diseñar debido a que utilizan circuitos de conmutación donde solo importa el intervalo (ALTO o BAJO) y no los valores exactos de voltaje o corriente\n"
            "• Facilitan el almacenamiento de información mediante dispositivos especiales que pueden almacenar miles de millones de bits en espacios físicos relativamente pequeños\n"
            "• Mantienen mejor la precisión y exactitud, ya que la información digitalizada no se deteriora durante el procesamiento\n"
            "• Permiten operaciones programables controladas por conjuntos de instrucciones almacenadas (programas)\n"
            "• Son más resistentes al ruido, ya que las fluctuaciones espurias no afectan significativamente mientras se pueda distinguir entre niveles ALTO y BAJO\n"
            "• Pueden fabricarse más circuitos en chips de CI debido a su menor complejidad relativa\n\n"

            "[SUBTITLE]Sistemas Analógicos:[/SUBTITLE]\n"
            "Los sistemas analógicos contienen dispositivos que manipulan cantidades físicas representadas en forma analógica, donde las cantidades pueden variar sobre un intervalo continuo de valores. "
            "Por ejemplo, la amplitud de señal de salida en un receptor de radio puede tener cualquier valor entre cero y su límite máximo. "
            "Sistemas analógicos comunes incluyen amplificadores de audio, equipos de grabación y reproducción de cintas magnéticas, e interruptores reguladores de luz.\n\n"
            
            "\n[IMAGE:Imagenes/sistemas-analogicos.jpeg] \n"

            "[SUBTITLE]Ventajas de los Sistemas Analógicos:[/SUBTITLE]\n"
            "• Pueden representar variaciones continuas de manera más natural y precisa\n"
            "• Son más simples en términos de diseño y construcción para ciertas aplicaciones\n"
            "• Pueden manejar señales de alta frecuencia sin necesidad de muestreo\n"
            "• En algunos casos, pueden ser más económicos que sus contrapartes digitales\n\n"

            "[SUBTITLE]Limitaciones de las Técnicas Digitales:[/SUBTITLE]\n"
            "• El mundo real es analógico: La mayoría de cantidades físicas (temperatura, presión, posición, velocidad, nivel de líquido, flujo) son analógicas por naturaleza\n"
            "• El procesamiento de señales digitales requiere tiempo adicional para las conversiones y cálculos\n\n"

            "[SUBTITLE]Proceso de Conversión Analógico-Digital:[/SUBTITLE]\n"
            "Para aprovechar las técnicas digitales con entradas y salidas analógicas se siguen cuatro pasos:\n"
            "1. Convertir la variable física en una señal eléctrica analógica (mediante sensores)\n"
            "2. Convertir la señal eléctrica analógica a forma digital (ADC)\n"
            "3. Procesar la información digital\n"
            "4. Convertir las salidas digitales nuevamente a forma analógica (DAC)\n\n"

            "[SUBTITLE]Aplicaciones Prácticas:[/SUBTITLE]\n"
            "Los sistemas híbridos combinan técnicas analógicas y digitales para beneficiarse de las ventajas de ambas. "
            "La tendencia general es digitalizar la señal lo más pronto posible y convertirla de nuevo en analógica lo más tarde posible. "
            "Ejemplos incluyen sistemas de control de temperatura de precisión, grabación de audio en CD, y sistemas automotrices con múltiples sensores.\n\n"

            "[SUBTITLE]Conversión A/D (Analógico-Digital):[/SUBTITLE]\n"
            "• Muestreo: Basado en el Teorema de Nyquist, determina la frecuencia mínima de muestreo necesaria\n"
            "• Cuantización: Define la resolución en bits del sistema digital\n"
            "• Tipos de ADC: Flash (más rápido), SAR (Successive Approximation Register), Delta-Sigma (alta precisión)\n\n"

            "[SUBTITLE]Conversión D/A (Digital-Analógico):[/SUBTITLE]\n"
            "• DAC R-2R: Utiliza redes de resistencias para conversión precisa\n"
            "• PWM (Modulación por Ancho de Pulso): Técnica eficiente para control de potencia\n\n"

            "[SUBTITLE]Interfaz de Señales:[/SUBTITLE]\n"
            "• Filtros Anti-Aliasing: Previenen la distorsión por frecuencias de muestreo inadecuadas\n"
            "• Amplificadores Operacionales: Componentes fundamentales para acondicionamiento de señales analógicas\n\n"
        ),
        "url" : "https://wayground.com/admin/assessment/6881a755e8faf12874df707a?source=lesson_share"
    },


    "  Microoperaciones y nivel RTL": {
        "title": "Microoperaciones y Nivel RTL (Register Transfer Level)",
        "content": (
            "El Nivel RTL (Register Transfer Level) es un nivel de abstracción en el diseño de sistemas digitales que describe el comportamiento de un sistema en términos de transferencias de datos entre registros y las operaciones realizadas sobre estos datos. "
            "Este nivel es fundamental para comprender el funcionamiento interno de los procesadores y sistemas digitales complejos, ya que proporciona una representación detallada de cómo se mueven y procesan los datos a nivel de hardware.\n\n"
            
            "[BOLD]En el nivel RTL[/BOLD], el comportamiento del sistema se describe mediante:\n"
            "• Registros que almacenan información temporal\n"
            "• Microoperaciones que manipulan los datos\n"
            "• Señales de control que coordinan las operaciones\n"
            "• Rutas de datos que conectan los componentes\n\n"

            "[SUBTITLE]REGISTROS:[/SUBTITLE]\n"
            "Los registros son elementos de almacenamiento temporal de alta velocidad que forman parte integral de la CPU. "
            "Están construidos con flip-flops y proporcionan acceso inmediato a los datos más frecuentemente utilizados. "
            "Los registros se clasifican según su función y propósito específico dentro del procesador.\n\n"

            "[SUBTITLE]Registros de Propósito General:[/SUBTITLE]\n"
            "Los registros de propósito general son ubicaciones de almacenamiento que pueden ser utilizadas por el programador para almacenar datos temporalmente durante la ejecución de programas. "
            "En arquitecturas x86, los principales registros de propósito general incluyen:\n\n"
            
            "• [BOLD]Registro AX (Acumulador): De 16 bits, dividido en AH (8 bits altos) y AL (8 bits bajos)[/BOLD]\n"
            "  - Utilizado principalmente para operaciones aritméticas y lógicas\n"
            "  - Registro destino por defecto para muchas operaciones\n"
            "  - Optimizado para operaciones de multiplicación y división\n"
            "  - En procesadores de 32 bits se extiende a EAX, y en 64 bits a RAX\n\n"

            "• [BOLD]Registro BX (Base): De 16 bits, dividido en BH y BL[/BOLD]\n"
            "  - Utilizado como registro base para direccionamiento\n"
            "  - Puede contener direcciones de memoria para acceso indirecto\n"
            "  - Útil para operaciones con arreglos y estructuras de datos\n"
            "  - Se extiende a EBX (32 bits) y RBX (64 bits)\n\n"

            "• [BOLD]Otros registros importantes:[/BOLD]\n"
            "  - CX (Contador): Utilizado para bucles y operaciones de conteo\n"
            "  - DX (Datos): Utilizado para operaciones de E/S y multiplicación extendida\n"
            "  - SP (Stack Pointer): Apunta al tope de la pila\n"
            "  - BP (Base Pointer): Utilizado para referenciar datos en la pila\n"
            "  - SI/DI (Source/Destination Index): Para operaciones con cadenas\n\n"


            "[SUBTITLE]Registros de Control:[/SUBTITLE]\n"
            "Los registros de control son elementos especializados que coordinan y controlan la operación del procesador. "
            "No son directamente accesibles por el programador pero son fundamentales para el funcionamiento del sistema:\n\n"

            "• [BOLD]PC (Program Counter/Instruction Pointer):[/BOLD]\n"
            "  - Contiene la dirección de memoria de la próxima instrucción a ejecutar\n"
            "  - Se incrementa automáticamente después de cada fetch de instrucción\n"
            "  - Puede ser modificado por instrucciones de salto (JMP, CALL, RET)\n"
            "  - Tamaño típico: 16, 32 o 64 bits según la arquitectura\n"
            "  - Esencial para el flujo secuencial de ejecución de programas\n\n"

            "• [BOLD] IR (Instruction Register):[/BOLD]\n"
            "  - Almacena la instrucción actualmente en proceso de decodificación y ejecución\n"
            "  - Recibe la instrucción desde la memoria durante la fase de fetch\n"
            "  - Proporciona los bits de la instrucción al decodificador\n"
            "  - Tamaño variable según la longitud de las instrucciones (8, 16, 32 bits típicamente)\n"
            "  - Mantiene la instrucción durante todo el ciclo de ejecución\n\n"

            "• [BOLD]MAR (Memory Address Register):[/BOLD]\n"
            "  - Contiene la dirección de memoria que se va a acceder\n"
            "  - Conectado al bus de direcciones del sistema\n"
            "  - Especifica la ubicación en memoria para operaciones de lectura/escritura\n"
            "  - Su tamaño determina el espacio de direccionamiento máximo\n"
            "  - Cargado desde PC para fetch de instrucciones o desde otros registros para acceso a datos\n\n"

            "• [BOLD]MBR/MDR (Memory Buffer Register/Memory Data Register):[/BOLD]\n"
            "  - Almacena temporalmente los datos leídos de o escritos a la memoria\n"
            "  - Actúa como buffer entre la CPU y el sistema de memoria\n"
            "  - Conectado al bus de datos del sistema\n"
            "  - Puede contener instrucciones durante el fetch o datos durante operaciones de carga/almacenamiento\n"
            "  - Su tamaño coincide con el ancho del bus de datos\n\n"

            "[SUBTITLE]MICROOPERACIONES:[/SUBTITLE]\n"
            "Las microoperaciones son operaciones elementales realizadas en los registros durante un ciclo de reloj. "
            "Estas operaciones constituyen los bloques básicos de construcción para implementar instrucciones más complejas. "
            "Se clasifican en cuatro categorías principales según el tipo de operación que realizan:\n\n"

            "[SUBTITLE]Microoperaciones de Transferencia:[/SUBTITLE]\n"
            "Las operaciones de transferencia mueven datos entre registros sin modificar su contenido. "
            "Son las microoperaciones más básicas y fundamentales:\n\n"
            
            "• [BOLD]MOV R1, R2:[/BOLD] Transfiere el contenido del registro R2 al registro R1\n"
            "  - Notación RTL: R1 ← R2\n"
            "  - El contenido de R2 permanece inalterado\n"
            "  - Ejemplo: MOV AX, BX (copia el contenido de BX a AX)\n"
            "  - Tiempo de ejecución: Generalmente un ciclo de reloj\n\n"

            "• [BOLD]Variaciones de transferencia:[/BOLD]\n"
            "  - MOV R1, #valor: Carga un valor inmediato en R1 (R1 ← valor)\n"
            "  - MOV R1, [dirección]: Carga desde memoria (R1 ← M[dirección])\n"
            "  - MOV [dirección], R1: Almacena en memoria (M[dirección] ← R1)\n"
            "  - XCHG R1, R2: Intercambio de contenidos (R1 ↔ R2)\n\n"

            "[SUBTITLE]Microoperaciones Aritméticas:[/SUBTITLE]\n"
            "Realizan operaciones matemáticas sobre los datos almacenados en registros. "
            "Utilizan la ALU (Unidad Aritmético-Lógica) del procesador:\n\n"

            "• [BOLD]ADD R1, R2: Suma aritmética[/BOLD]\n"
            "  - Notación RTL: R1 ← R1 + R2\n"
            "  - Afecta flags de estado (carry, overflow, zero, sign)\n"
            "  - Ejemplo: ADD AX, BX (AX = AX + BX)\n"
            "  - Puede generar carry para operaciones multi-precisión\n\n"

            "• [BOLD]SUB R1, R2: Resta aritmética[/BOLD]\n"
            "  - Notación RTL: R1 ← R1 - R2\n"
            "  - Implementada como suma con complemento a dos\n"
            "  - Afecta flag de carry (borrow) y overflow\n"
            "  - Ejemplo: SUB AX, BX (AX = AX - BX)\n\n"

            "• [BOLD]Otras operaciones aritméticas:[/BOLD]\n"
            "  - MUL R1, R2: Multiplicación (resultado en registros extendidos)\n"
            "  - DIV R1, R2: División (cociente y residuo)\n"
            "  - INC R1: Incremento (R1 ← R1 + 1)\n"
            "  - DEC R1: Decremento (R1 ← R1 - 1)\n"
            "  - NEG R1: Negación (complemento a dos)\n\n"

            "[SUBTITLE]Microoperaciones Lógicas:[/SUBTITLE]\n"
            "Realizan operaciones lógicas bit a bit sobre los datos. "
            "Son fundamentales para manipulación de bits y operaciones booleanas:\n\n"

            "• [BOLD]AND R1, R2: Operación AND lógica[/BOLD]\n"
            "  - Notación RTL: R1 ← R1 ∧ R2\n"
            "  - Resultado: 1 solo si ambos bits son 1\n"
            "  - Útil para enmascaramiento de bits\n"
            "  - Ejemplo: AND AX, 0FFh (conserva solo los 8 bits bajos)\n\n"

            "• [BOLD]OR R1, R2: Operación OR lógica[/BOLD]/n"
            "  - Notación RTL: R1 ← R1 ∨ R2\n"
            "  - Resultado: 0 solo si ambos bits son 0\n"
            "  - Útil para activar bits específicos\n"
            "  - Ejemplo: OR AX, 8000h (activa el bit más significativo)\n\n"

            "• [BOLD]NOT R1: Operación NOT lógica[/BOLD]\n"
            "  - Notación RTL: R1 ← R̄1\n"
            "  - Invierte todos los bits del registro\n"
            "  - Complemento a uno\n"
            "  - Ejemplo: NOT AX (todos los 0s se vuelven 1s y viceversa)\n\n"

            "• [BOLD]Otras operaciones lógicas:[/BOLD]\n"
            "  - XOR R1, R2: OR exclusivo (útil para comparaciones y cifrado)\n"
            "  - TEST R1, R2: AND sin modificar destino (solo afecta flags)\n"
            "  - CMP R1, R2: Comparación (resta sin modificar destino)\n\n"
            
            "[SUBTITLE]Microoperaciones de Desplazamiento:[/SUBTITLE]\n"
            "Mueven los bits dentro de un registro hacia la izquierda o derecha. "
            "Son fundamentales para operaciones de multiplicación/división por potencias de 2:\n\n"

            "• [BOLD]SHL R1, n:[/BOLD] Desplazamiento lógico a la izquierda\n"
            "  - Notación RTL: R1 ← R1 << n\n"
            "  - Desplaza n posiciones a la izquierda\n"
            "  - Rellena con 0s por la derecha\n"
            "  - Equivale a multiplicar por 2^n\n"
            "  - El bit más significativo va al flag de carry\n\n"

            "• [BOLD]SHR R1, n:[/BOLD] Desplazamiento lógico a la derecha\n"
            "  - Notación RTL: R1 ← R1 >> n\n"
            "  - Desplaza n posiciones a la derecha\n"
            "  - Rellena con 0s por la izquierda\n"
            "  - Equivale a dividir por 2^n (números sin signo)\n"
            "  - El bit menos significativo va al flag de carry\n\n"

            "• [BOLD]Variaciones de desplazamiento:[/BOLD]/n"
            "  - SAL/SAR: Desplazamiento aritmético (preserva signo)\n"
            "  - ROL/ROR: Rotación (los bits que salen regresan por el otro extremo)\n"
            "  - RCL/RCR: Rotación a través del carry\n\n"

            "[SUBTITLE]UNIDAD DE CONTROL:[/SUBTITLE]/n"
            "La Unidad de Control (CU) es el componente del procesador responsable de coordinar y controlar todas las operaciones. "
            "Interpreta las instrucciones y genera las señales de control necesarias para ejecutarlas. "
            "Determina cuándo y cómo se realizan las microoperaciones.\n\n"

            "[BOLD]Funciones principales de la Unidad de Control:\n[/BOLD]"
            "• Decodificación de instrucciones\n"
            "• Generación de señales de control\n"
            "• Secuenciamiento de microoperaciones\n"
            "• Manejo de interrupciones y excepciones\n"
            "• Control de acceso a memoria y E/S\n\n"

            "[SUBTITLE]Lógica Cableada vs Microprogramada:\n[/SUBTITLE]"
            "Existen dos enfoques principales para implementar la unidad de control:\n\n"

            "[BOLD]LÓGICA CABLEADA (Hardwired Control):[/BOLD]\n"
            "• [BOLD]Implementación:[/BOLD] Utiliza circuitos lógicos combinacionales y secuenciales\n"
            "• [BOLD]Características:[/BOLD]\n"
            "  - Circuitos diseñados específicamente para cada instrucción\n"
            "  - Utiliza decodificadores, multiplexores, y lógica combinacional\n"
            "  - Señales de control generadas directamente por hardware\n"
            "  - Diseño fijo una vez fabricado el procesador\n\n"
            "• [BOLD]Ventajas:[/BOLD]\n"
            "  - Mayor velocidad de ejecución\n"
            "  - Menor latencia en la generación de señales de control\n"
            "  - Menor complejidad en términos de niveles de abstracción\n"
            "  - Mejor rendimiento para conjuntos de instrucciones simples\n\n"
            "• [BOLD]Desventajas:[/BOLD]\n"
            "  - Difícil de modificar o expandir\n"
            "  - Complejidad de diseño aumenta exponencialmente con el número de instrucciones\n"
            "  - Mayor costo de desarrollo para procesadores complejos\n"
            "  - Debugging más complicado\n\n"

            "[BOLD]LÓGICA MICROPROGRAMADA (Microprogrammed Control):[/BOLD]\n"
            "• [BOLD]Implementación:[/BOLD] Utiliza una memoria de control (ROM) que contiene microprogramas\n"
            "• [BOLD]Características:[/BOLD]\n"
            "  - Cada instrucción se descompone en secuencias de microinstrucciones\n"
            "  - Las microinstrucciones se almacenan en memoria de control\n"
            "  - Un secuenciador de microinstrucciones controla la ejecución\n"
            "  - Utiliza un contador de microinstrucciones (μPC)\n\n"
            "• [BOLD]Ventajas:[/BOLD]\n"
            "  - Mayor flexibilidad para modificaciones\n"
            "  - Facilita la implementación de conjuntos de instrucciones complejos\n"
            "  - Más fácil de debuggear y verificar\n"
            "  - Permite corrección de errores mediante actualizaciones de firmware\n"
            "  - Diseño más sistemático y estructurado\n\n"
            "• [BOLD]Desventajas:[/BOLD]\n"
            "  - Mayor latencia debido a los accesos adicionales a memoria\n"
            "  - Consumo adicional de memoria para almacenar microprogramas\n"
            "  - Potencialmente más lento que la lógica cableada\n"
            "  - Mayor complejidad en el secuenciamiento\n\n"

            "[BOLD]Ejemplo de ejecución de una instrucción:[/BOLD] (Martínez Durá)\n"
            "Supongamos la instrucción `ADD R1, R2` (suma los valores de R1 y R2 y guarda el resultado en R1). Las microoperaciones implicadas podrían ser:"
            "El proceso sería el siguiente:\n\n"
            "1. `TEMP ← R1`\n"
            "2. `ALU ← TEMP + R2`\n"
            "3. `R1 ← ALU`\n"
            "Cada una de estas microoperaciones ocurre en un ciclo de reloj y es orquestada por señales de control.\n"
        ),
        "url" : "https://wayground.com/admin/assessment/6881aedc882c169778fbdd1a?source=lesson_share"
    },
    "  Arquitectura de computadores": {
        "title": "Arquitectura de Computadores",
        "content": (
            "La arquitectura de computadores es la disciplina que estudia el diseño y organización de los sistemas de cómputo, "
            "definiendo la estructura conceptual y funcional de las computadoras. Establece cómo se organizan y conectan "
            "los componentes de hardware para ejecutar programas de manera eficiente. La arquitectura determina las capacidades "
            "del sistema, su rendimiento, y la forma en que el software interactúa con el hardware.\n\n"

            "[SUBTITLE]EVOLUCIÓN HISTÓRICA:[/SUBTITLE]\n"
            "La arquitectura moderna de computadores se basa en conceptos desarrollados desde los años 1940:\n"
            "• [BOLD]ENIAC (1946):[/BOLD] Primera computadora electrónica de propósito general\n"
            "• [BOLD]Modelo von Neumann (1945):[/BOLD] Arquitectura fundamental que persiste hasta hoy\n"
            "• [BOLD]Transistor (1947):[/BOLD] Revolucionó la construcción de computadores\n"
            "• [BOLD]Circuitos integrados (1960s):[/BOLD] Permitieron miniaturización y mayor complejidad\n"
            "• [BOLD]Microprocesadores (1970s):[/BOLD] Intel 4004, inicio de la era personal\n"
            "• [BOLD]Arquitecturas modernas:[/BOLD] Múltiples núcleos, paralelismo, especialización\n\n"

            "[SUBTITLE]Estructura de Computadores:[/SUBTITLE]\n"
            "Para poder comprender cómo funciona un computador es necesario basarse en una organización jerárquica, donde cada nivel consta de componentes y de la interacción entre estos. Una posible clasificación de los niveles estructurales, ordenados de menor a mayor, sería:\n"
            "[BOLD]Nivel de componente:[/BOLD] Nivel más bajo de la jerarquía. Trata con las leyes de la física en estado sólido y la electrónica física. Mediante la introducción de átomos específicos para modificar las propiedades físicas del silicio y crear diodos y transistores, esenciales para desarrollar chips. Estos transistores constituyen el siguiente nivel.\n"
            "[BOLD]Nivel electrónico:[/BOLD] Compuesto de transistores, resistencias, condensadores y diodos que son usados para crear circuitos integrados (CIs). Se aplican leyes eléctricas y electŕonicas. En este nivel se construyen las compuertas lógicas a partir de los transistores.\n"
            "[BOLD]Nivel digital:[/BOLD] Es descrito mediante unos y ceros. Se compone de las compuertas loǵicas, biestables y modelos tanto combinacionales como secuenciales.\n"
            "[BOLD]Nivel RTL:[/BOLD] Este nivel se compone por los registros y la transferencia de datos mediante ellos. Los elementos típicos en este nivel de abstracción son los registros, para almacenar información binaria, y módulos combinacionales aritméticos, para realizar transformaciones básicas de los datos.\n"
            "[BOLD]Nivel PMS:[/BOLD] Es el nivel más alto en esta jerarquía. PMS significa Processor Memory Switch. Se compone por buses, memorias, procesadores y otros módulos de alto nivel. Los buses se utilizan para intercambiar información.\n"

            "[SUBTITLE]CPU (UNIDAD CENTRAL DE PROCESAMIENTO):[/SUBTITLE]\n"
            "La CPU es el cerebro del computador, responsable de ejecutar las instrucciones de los programas. "
            "Está compuesta por tres unidades funcionales principales que trabajan coordinadamente:\n\n"

            "[SUBTITLE]ALU (UNIDAD ARITMÉTICO-LÓGICA):[/SUBTITLE]\n"
            "La ALU es el componente que realiza todas las operaciones matemáticas y lógicas:\n\n"

            "• [BOLD]Operaciones Aritméticas:[/BOLD]\n"
            "  - Suma binaria con generación de carry\n"
            "  - Resta mediante complemento a dos\n"
            "  - Multiplicación (mediante sumas repetidas o algoritmos optimizados)\n"
            "  - División (mediante restas repetidas o algoritmos de división)\n"
            "  - Operaciones en punto flotante (IEEE 754)\n\n"

            "• [BOLD]Operaciones Lógicas:[/BOLD]\n"
            "  - AND, OR, XOR bit a bit\n"
            "  - NOT (complemento)\n"
            "  - Desplazamientos lógicos (SHL, SHR)\n"
            "  - Rotaciones (ROL, ROR)\n"
            "  - Comparaciones (mayor, menor, igual)\n\n"
            
            "• [BOLD]Componentes de la ALU:[/BOLD]\n"
            "  - Sumador binario (ripple-carry o carry-lookahead)\n"
            "  - Unidad de desplazamiento (barrel shifter)\n"
            "  - Unidad de punto flotante (FPU)\n"
            "  - Generador de flags de estado\n"
            "  - Multiplexores para selección de operaciones\n\n"
            
            "• [BOLD]Flags de Estado:[/BOLD]\n"
            "  - Zero Flag (Z): Resultado igual a cero\n"
            "  - Carry Flag (C): Acarreo en operaciones\n"
            "  - Overflow Flag (V): Desbordamiento aritmético\n"
            "  - Sign Flag (S): Signo del resultado\n"
            "  - Parity Flag (P): Paridad del resultado\n\n"

            "[SUBTITLE]UC (UNIDAD DE CONTROL):[/SUBTITLE]\n"
            "La UC coordina y controla todas las operaciones del procesador:\n\n"

            "• [BOLD]Funciones Principales:[/BOLD]\n"
            "  - Fetch: Obtener instrucciones de memoria\n"
            "  - Decode: Interpretar códigos de operación\n"
            "  - Execute: Coordinar ejecución de instrucciones\n"
            "  - Control de flujo del programa\n"
            "  - Generación de señales de control\n"
            "  - Manejo de interrupciones y excepciones\n\n"

            "• [BOLD]Componentes de la UC:[/BOLD]\n"
            "  - Contador de Programa (PC/IP)\n"
            "  - Registro de Instrucción (IR)\n"
            "  - Decodificador de instrucciones\n"
            "  - Secuenciador de microoperaciones\n"
            "  - Controlador de interrupciones\n\n"

            "• [BOLD]Tipos de Implementación:[/BOLD]\n"
            "  - Lógica Cableada: Circuitos dedicados, mayor velocidad\n"
            "  - Microprogramada: Firmware almacenado, mayor flexibilidad\n"
            "  - Híbrida: Combinación de ambos enfoques\n\n"

            "[SUBTITLE]REGISTROS DEL PROCESADOR:[/SUBTITLE]\n"
            "Los registros son elementos de almacenamiento de alta velocidad dentro de la CPU:\n\n"

            "• [BOLD]Registros de Propósito General:[/BOLD]\n"
            "  - AX/EAX/RAX: Acumulador para operaciones aritméticas\n"
            "  - BX/EBX/RBX: Base para direccionamiento\n"
            "  - CX/ECX/RCX: Contador para bucles\n"
            "  - DX/EDX/RDX: Datos para E/S y multiplicación extendida\n"
            "  - Utilizables por el programador\n"
            "  - Tamaño variable: 8, 16, 32, 64 bits\n\n"

            "• [BOLD]Registros de Índice y Punteros:[/BOLD]\n"
            "  - SP/ESP/RSP: Stack Pointer (puntero de pila)\n"
            "  - BP/EBP/RBP: Base Pointer (puntero base)\n"
            "  - SI/ESI/RSI: Source Index (índice fuente)\n"
            "  - DI/EDI/RDI: Destination Index (índice destino)\n\n"

            "• [BOLD]Registros de Segmento (x86):[/BOLD]\n"
            "  - CS: Code Segment (segmento de código)\n"
            "  - DS: Data Segment (segmento de datos)\n"
            "  - SS: Stack Segment (segmento de pila)\n"
            "  - ES, FS, GS: Segmentos extra\n\n"

            "• [BOLD]Registros de Control:[/BOLD]\n"
            "  - FLAGS/EFLAGS/RFLAGS: Estado del procesador\n"
            "  - IP/EIP/RIP: Instruction Pointer\n"
            "  - CR0, CR1, CR2, CR3: Registros de control del sistema\n\n"

            "[SUBTITLE]JERARQUÍA DE MEMORIA:[/SUBTITLE]\n"
            "La jerarquía de memoria es una organización estratificada que optimiza el balance entre "
            "velocidad, capacidad y costo. Se basa en el principio de localidad de referencia.\n\n"

            "[SUBTITLE]PRINCIPIOS DE LA JERARQUÍA:[/SUBTITLE]\n"
            "• Localidad Temporal: Los datos recientemente accedidos tienen mayor probabilidad de ser accedidos nuevamente\n"
            "• Localidad Espacial: Los datos cercanos a los accedidos tienen mayor probabilidad de ser accedidos\n"
            "• Compromiso Velocidad-Capacidad-Costo: Niveles más rápidos son más caros y pequeños\n\n"

            "[SUBTITLE]NIVELES DE LA JERARQUÍA (de más rápido a más lento):[/SUBTITLE]\n\n"

            "1. [BOLD]REGISTROS DEL PROCESADOR:[/BOLD]\n"
            "   • Velocidad: 0 ciclos de espera\n"
            "   • Capacidad: 32-128 registros (~1-4 KB)\n"
            "   • Tecnología: SRAM integrada en el procesador\n"
            "   • Control: Explícito por el compilador/programador\n\n"

            "2. [BOLD]CACHÉ DE NIVEL 1 (L1):[/BOLD]\n"
            "   • Velocidad: 1-2 ciclos de reloj\n"
            "   • Capacidad: 16-64 KB por núcleo\n"
            "   • División: I-Cache (instrucciones) y D-Cache (datos)\n"
            "   • Tecnología: SRAM de alta velocidad\n"
            "   • Asociatividad: Típicamente 2-8 vías\n"
            "   • Hit rate: 85-95%\n\n"

            "3. [BOLD]CACHÉ DE NIVEL 2 (L2):[/BOLD]\n"
            "   • Velocidad: 3-10 ciclos de reloj\n"
            "   • Capacidad: 256 KB - 2 MB por núcleo\n"
            "   • Caché unificada (instrucciones y datos)\n"
            "   • Mayor asociatividad que L1\n"
            "   • Hit rate: 75-90%\n\n"

            "4. [BOLD]CACHÉ DE NIVEL 3 (L3):[/BOLD]\n"
            "   • Velocidad: 10-30 ciclos de reloj\n"
            "   • Capacidad: 4-32 MB compartida\n"
            "   • Compartida entre múltiples núcleos\n"
            "   • Reduce tráfico a memoria principal\n"
            "   • Hit rate: 60-80%\n\n"

            "5. [BOLD]MEMORIA PRINCIPAL (RAM):[/BOLD]\n"
            "   • Velocidad: 100-300 ciclos de reloj\n"
            "   • Capacidad: 4-128 GB típicamente\n"
            "   • Tecnologías: DDR4, DDR5 SDRAM\n"
            "   • Volátil: Pierde contenido sin energía\n"
            "   • Acceso aleatorio uniforme\n\n"

            "[SUBTITLE]TIPOS DE RAM:[/SUBTITLE]\n"
            "• [BOLD]DRAM (Dynamic RAM):[/BOLD]\n"
            "  - Almacena datos en capacitores\n"
            "  - Requiere refresh periódico\n"
            "  - Mayor densidad, menor costo\n"
            "  - Tecnologías: SDRAM, DDR, DDR2, DDR3, DDR4, DDR5\n\n"

            "• [BOLD]SRAM (Static RAM):[/BOLD]\n"
            "  - Almacena datos en flip-flops\n"
            "  - No requiere refresh\n"
            "  - Mayor velocidad, mayor costo\n"
            "  - Utilizada en cachés\n\n"

            "6. [BOLD]ALMACENAMIENTO SECUNDARIO:[/BOLD]\n"
            "   • Velocidad: Millones de ciclos de reloj\n"
            "   • Capacidad: Terabytes\n"
            "   • No volátil: Conserva datos sin energía\n"
            "   • Tecnologías: HDD, SSD, NVMe\n\n"

            "[SUBTITLE]CARACTERÍSTICAS DE LOS DISPOSITIVOS DE ALMACENAMIENTO:[/SUBTITLE]\n\n"

            "[BOLD]HDD (Hard Disk Drive):[/BOLD]\n"
            "• Tecnología mecánica con discos magnéticos\n"
            "• Capacidad: 500 GB - 20 TB\n"
            "• Velocidad: 5400-15000 RPM\n"
            "• Tiempo de acceso: 5-15 ms\n"
            "• Costo por GB: Muy bajo\n"
            "• Durabilidad: Sensible a impactos\n\n"
            
            "[BOLD]SSD (Solid State Drive):[/BOLD]\n"
            "• Tecnología de memoria flash NAND\n"
            "• Capacidad: 120 GB - 8 TB\n"
            "• Tiempo de acceso: 0.1-0.2 ms\n"
            "• Sin partes móviles\n"
            "• Mayor velocidad de transferencia\n"
            "• Menor consumo energético\n\n"

            "[BOLD]NVMe (Non-Volatile Memory Express):[/BOLD]\n"
            "• Protocolo optimizado para SSDs\n"
            "• Interfaz PCIe directa\n"
            "• Menor latencia que SATA\n"
            "• Mayor paralelismo\n"
            "• Velocidades hasta 7 GB/s\n\n"

            "[BOLD]GESTIÓN DE CACHÉ:[/BOLD]\n"
            "• Políticas de Reemplazo:\n"
            "  - LRU (Least Recently Used)\n"
            "  - FIFO (First In, First Out)\n"
            "  - Random\n"
            "  - LFU (Least Frequently Used)\n\n"

            "• [BOLD]Políticas de Escritura:[/BOLD]\n"
            "  - Write-through: Escritura simultánea en caché y memoria\n"
            "  - Write-back: Escritura diferida hasta reemplazo\n"
            "  - Write-around: Escritura directa a memoria\n\n"

            "[SUBTITLE]BUS DEL SISTEMA:[/SUBTITLE]\n"
            "Los buses son conjuntos de líneas de comunicación que conectan los componentes del sistema. "
            "Permiten la transferencia de información entre CPU, memoria y dispositivos de E/S.\n\n"

            "[SUBTITLE]CLASIFICACIÓN DE BUSES:[/SUBTITLE]\n\n"

            "[BOLD]BUS DE DATOS:[/BOLD]\n"
            "• [BOLD]Función:[/BOLD] Transporta información entre componentes\n"
            "• [BOLD]Características:[/BOLD]\n"
            "  - Bidireccional: Los datos fluyen en ambas direcciones\n"
            "  - Anchura determina la cantidad de datos transferidos simultáneamente\n"
            "  - Típicamente 8, 16, 32, 64 bits en sistemas modernos\n"
            "  - Mayor anchura = mayor rendimiento\n\n"

            "• [BOLD]Ejemplos de Ancho de Bus:[/BOLD]\n"
            "  - 8 bits: Sistemas embebidos, microcontroladores\n"
            "  - 16 bits: Sistemas legados (8086, 80286)\n"
            "  - 32 bits: Arquitecturas x86 estándar\n"
            "  - 64 bits: Sistemas modernos (x86-64, ARM64)\n"
            "  - 128+ bits: Buses especializados (GPU, memoria gráfica)\n\n"

            "[BOLD]BUS DE DIRECCIONES:[/BOLD]\n"
            "• [BOLD]Función:[/BOLD] Especifica la ubicación de memoria o E/S a acceder\n"
            "• [BOLD]Características:[/BOLD]\n"
            "  - Unidireccional: Solo la CPU genera direcciones\n"
            "  - Anchura determina el espacio de direccionamiento máximo\n"
            "  - n bits de dirección = 2^n ubicaciones direccionables\n\n"

            "• [BOLD]Capacidad de Direccionamiento:[/BOLD]\n"
            "  - 16 bits: 64 KB (sistemas de 8 bits)\n"
            "  - 20 bits: 1 MB (8086 con segmentación)\n"
            "  - 32 bits: 4 GB (sistemas x86 estándar)\n"
            "  - 48 bits: 256 TB (x86-64 actual)\n"
            "  - 64 bits: 16 EB (x86-64 teórico)\n\n"

            "[BOLD]BUS DE CONTROL:[/BOLD]\n"
            "• [BOLD]Función:[/BOLD] Coordina y controla las operaciones del sistema\n"
            "• [BOLD]Características:[/BOLD]\n"
            "  - Señales unidireccionales o bidireccionales\n"
            "  - Número variable de líneas según complejidad\n\n"

            "• [BOLD]Señales Típicas de Control:[/BOLD]\n"
            "  - READ: Indica operación de lectura\n"
            "  - WRITE: Indica operación de escritura\n"
            "  - CLOCK: Señal de sincronización\n"
            "  - RESET: Reinicio del sistema\n"
            "  - INTERRUPT: Solicitud de interrupción\n"
            "  - READY/WAIT: Estados de dispositivos\n"
            "  - BUS_GRANT: Concesión del bus\n"
            "  - BUS_REQUEST: Solicitud del bus\n\n"
        
            "[SUBTITLE]ARQUITECTURAS DE BUS:[/SUBTITLE]\n\n"
            
            "[BOLD]1. BUS ÚNICO (Von Neumann):[/BOLD]\n"
            "   • Un solo bus para datos, direcciones y control\n"
            "   • Ventajas:\n"
            "     - Código relocatable (independiente de posición)\n"
            "     - Útil para saltos y llamadas a procedimientos\n"
            "     - Rango limitado pero eficiente\n\n"

            "[BOLD]2. BUSES SEPARADOS (Harvard):[/BOLD]\n"
            "   • Buses independientes para instrucciones y datos\n"
            "   • Ventajas: Mayor rendimiento, paralelismo\n"
            "   • Desventajas: Mayor complejidad, costo\n\n"

            "[SUBTITLE]PROCESAMIENTO DE INSTRUCCIONES:[/SUBTITLE]\n"
            "El procesamiento de instrucciones es el mecanismo fundamental mediante el cual "
            "la CPU ejecuta los programas. Involucra múltiples etapas y optimizaciones para "
            "maximizar el rendimiento del sistema.\n\n"

            "[BOLD]CICLO BÁSICO DE INSTRUCCIÓN:[/BOLD]\n"
            "1. Fetch (Búsqueda): Obtener instrucción de memoria\n"
            "2. Decode (Decodificación): Interpretar la instrucción\n"
            "3. Execute (Ejecución): Realizar la operación\n"
            "4. Store (Almacenamiento): Guardar resultados\n\n"

            "[BOLD]CICLOS DE RELOJ Y PIPELINE:[/BOLD]\n"
            "El pipeline es una técnica de optimización que permite el procesamiento simultáneo "
            "de múltiples instrucciones en diferentes etapas.\n\n"

            "[BOLD]¿Qué es un Pipeline?:[/BOLD]\n"
            "• Analogía: Línea de ensamblaje industrial\n"
            "• Solapamiento: Múltiples instrucciones en ejecución simultánea\n"
            "• Etapas: División del procesamiento en fases independientes\n"
            "• Throughput: Número de instrucciones completadas por unidad de tiempo\n\n"

            "[BOLD]PIPELINE CLÁSICO (5 ETAPAS - RISC):[/BOLD]\n\n"

            "[BOLD]1. IF (Instruction Fetch):[/BOLD]\n"
            "   • Obtener instrucción desde memoria/caché\n"
            "   • Actualizar contador de programa (PC)\n"
            "   • Duración: 1 ciclo de reloj\n"
            "   • Recursos: Cache de instrucciones, PC\n\n"

            "[BOLD]2. ID (Instruction Decode):[/BOLD]\n"
            "   • Decodificar código de operación\n"
            "   • Leer registros fuente\n"
            "   • Generar inmediatos y desplazamientos\n"
            "   • Duración: 1 ciclo de reloj\n"
            "   • Recursos: Decodificador, banco de registros\n\n"

            "[BOLD]3. EX (Execute):[/BOLD]\n"
            "   • Operaciones aritméticas/lógicas en ALU\n"
            "   • Cálculo de direcciones efectivas\n"
            "   • Evaluación de condiciones de salto\n"
            "   • Duración: 1 ciclo de reloj\n"
            "   • Recursos: ALU, unidades funcionales\n\n"

            "[BOLD]4. MEM (Memory Access):[/BOLD]\n"
            "   • Acceso a memoria para loads/stores\n"
            "   • Lectura/escritura de datos\n"
            "   • Bypass para instrucciones sin acceso a memoria\n"
            "   • Duración: 1+ ciclos (según latencia de memoria)\n"
            "   • Recursos: Cache de datos, controlador de memoria\n\n"

            "[BOLD]5. WB (Write Back):[/BOLD]\n"
            "   • Escribir resultado en registro destino\n"
            "   • Actualizar flags de estado\n"
            "   • Commit de la instrucción\n"
            "   • Duración: 1 ciclo de reloj\n"
            "   • Recursos: Banco de registros\n\n"

            "[BOLD]PIPELINE SUPERESCALAR:[/BOLD]\n"
            "• Múltiples pipelines paralelos\n"
            "• Emisión de múltiples instrucciones por ciclo\n"
            "• Análisis de dependencias dinámico\n"
            "• Renombrado de registros\n"
            "• Ejecución fuera de orden\n\n"

            "[SUBTITLE]MODOS DE DIRECCIONAMIENTO:[/SUBTITLE]\n"
            "Los modos de direccionamiento determinan cómo se calculan las direcciones "
            "efectivas de los operandos en las instrucciones.\n\n"

            "[BOLD]CLASIFICACIÓN DE MODOS DE DIRECCIONAMIENTO:[/BOLD]\n\n"

            "[BOLD]1. DIRECCIONAMIENTO INMEDIATO:[/BOLD]\n"
            "   • El operando es parte de la instrucción\n"
            "   • Formato: INST #valor\n"
            "   • Ejemplo: MOV AX, #100 (AX = 100)\n"
            "   • Ventajas:\n"
            "     - No requiere acceso adicional a memoria\n"
            "     - Velocidad máxima (1 ciclo)\n"
            "     - Simplicidad de implementación\n"
            "   • Desventajas:\n"
            "     - Limitado por tamaño de la instrucción\n"
            "     - No puede modificarse durante ejecución\n"
            "     - Aumento en tamaño del código\n"
            "   • Usos típicos: Constantes, inicializaciones\n\n"

            "[BOLD]2. DIRECCIONAMIENTO DIRECTO:[/BOLD]\n"
            "   • La dirección del operando está en la instrucción\n"
            "   • Formato: INST dirección\n"
            "   • Ejemplo: MOV AX, [1000] (AX = M[1000])\n"
            "   • Cálculo: Dirección_efectiva = dirección\n"
            "   • Ventajas: Acceso directo a cualquier ubicación\n"
            "   • Desventajas: Espacio de direcciones limitado\n\n"

            "[BOLD]3. DIRECCIONAMIENTO INDIRECTO:[/BOLD]\n"
            "   • La instrucción contiene dirección de la dirección\n"
            "   • Formato: INST [[dirección]]\n"
            "   • Ejemplo: MOV AX, [[1000]] (AX = M[M[1000]])\n"
            "   • Requiere dos accesos a memoria\n"
            "   • Ventajas:\n"
            "     - Espacio de direcciones completo\n"
            "     - Flexibilidad para punteros\n"
            "     - Útil para estructuras de datos dinámicas\n"
            "   • Desventajas:\n"
            "     - Mayor latencia (múltiples accesos)\n"
            "     - Complejidad adicional\n\n"

            "[BOLD]4. DIRECCIONAMIENTO POR REGISTRO:[/BOLD]\n"
            "   • El operando está en un registro\n"
            "   • Formato: INST registro\n"
            "   • Ejemplo: MOV AX, BX (AX = BX)\n"
            "   • Velocidad máxima (acceso directo)\n"
            "   • Limitado por número de registros\n\n"

            "[BOLD]5. DIRECCIONAMIENTO INDIRECTO POR REGISTRO:[/BOLD]\n"
            "   • El registro contiene la dirección del operando\n"
            "   • Formato: INST [registro]\n"
            "   • Ejemplo: MOV AX, [BX] (AX = M[BX])\n"
            "   • Cálculo: Dirección_efectiva = contenido_registro\n"
            "   • Ventajas:\n"
            "     - Flexibilidad para direccionamiento dinámico\n"
            "     - Útil para arreglos y punteros\n"
            "     - Un solo acceso a memoria adicional\n\n"

            "[BOLD]6. DIRECCIONAMIENTO CON DESPLAZAMIENTO:[/BOLD]\n"
            "   • Combina registro base con desplazamiento constante\n"
            "   • Formato: INST [registro + desplazamiento]\n"
            "   • Ejemplo: MOV AX, [BX + 10] (AX = M[BX + 10])\n"
            "   • Cálculo: Dirección_efectiva = registro + desplazamiento\n"
            "   • Variantes:\n"
            "     - Base + Desplazamiento\n"
            "     - Índice + Desplazamiento\n"
            "     - Base + Índice + Desplazamiento\n\n"

            "[SUBTITLE]Arquitecturas Superescalares[/SUBTITLE]\n"
            "[BOLD]Definición: Ejecutan múltiples instrucciones por ciclo usando unidades de ejecución paralelas.[/BOLD]\n"
            "[BOLD]Requisitos:[/BOLD]\n"
            "- Pipeline profundo.\n"
            "- Múltiples ALUs, FPUs, etc.\n"
            "- Lógica de despacho (scheduler) avanzada.\n"
            "[BOLD]Ejemplo:[/BOLD] Intel Pentium (2 pipelines), procesadores modernos (10+ pipelines).\n"
            "[BOLD]Limitaciones:[/BOLD] \n"
            "- Dependencias de datos y control. \n"
            "- Complejidad de diseño.\n\n "

            "[SUBTITLE]Procesadores Multinúcleo[/SUBTITLE]\n"
            "[BOLD]Concepto:[/BOLD] Integrar múltiples CPUs (cores) en un solo chip.\n"
            "[BOLD]Ventajas:[/BOLD] \n"
            "- Paralelismo real (threads simultáneos).\n "
            "- Mejor eficiencia energética.\n "
            "[BOLD]Desafíos:[/BOLD]\n "
            "- Coherencia de caché (protocolos: MESI, MOESI). \n"
            "- Sincronización (locks, semáforos). \n"
            "[BOLD]Ejemplos:[/BOLD] \n"
            "- Homogéneos: Todos los cores iguales (Intel Core i7). \n"
            "- Heterogéneos: Cores especializados (ARM big.LITTLE). \n\n"
        ),
        "url" : "https://wayground.com/admin/assessment/6881b201ba29416028b78db9?source=lesson_share"
    },
    "  Assembler": {
        "title": "Lenguaje Ensamblador (Assembler)",
        "content": (
            "El lenguaje ensamblador es un lenguaje de programación de bajo nivel que proporciona una "
            "representación simbólica de las instrucciones de máquina del procesador. Cada instrucción "
            "en ensamblador corresponde directamente a una instrucción de código máquina, estableciendo "
            "una relación uno-a-uno entre el código fuente y las operaciones del hardware.\n\n"

            "[SUBTITLE]CARACTERÍSTICAS FUNDAMENTALES:[/SUBTITLE]\n"
            "• Proximidad al hardware: Control directo sobre registros, memoria y periféricos\n"
            "• Eficiencia máxima: Sin overhead de compiladores de alto nivel\n"
            "• Control total: Acceso a todas las capacidades del procesador\n"
            "• Dependencia de arquitectura: Específico para cada familia de procesadores\n"
            "• Complejidad: Requiere conocimiento detallado del hardware\n\n"

            "[SUBTITLE]PROCESO DE TRADUCCIÓN:[/SUBTITLE]\n"
            "[BOLD]1. Código fuente (.asm, .s):[/BOLD] Texto con instrucciones simbólicas\n"
            "[BOLD]2. Ensamblador (Assembler):[/BOLD] Traduce símbolos a código máquina\n"
            "[BOLD]3. Código objeto (.obj, .o):[/BOLD] Código máquina con referencias sin resolver\n"
            "[BOLD]4. Enlazador (Linker):[/BOLD] Resuelve referencias y crea ejecutable\n"
            "[BOLD]5. Cargador (Loader):[/BOLD] Carga el programa en memoria para ejecución\n\n"

            "[SUBTITLE]VENTAJAS DEL LENGUAJE ENSAMBLADOR:[/SUBTITLE]\n"
            "• [BOLD]Máximo rendimiento:[/BOLD] Sin capas de abstracción intermedias\n"
            "• [BOLD]Control preciso:[/BOLD] Acceso a características específicas del procesador\n"
            "• [BOLD]Tamaño mínimo:[/BOLD] Código muy compacto y eficiente\n"
            "• [BOLD]Tiempo determinístico:[/BOLD] Comportamiento predecible en tiempo real\n"
            "• [BOLD]Debugging detallado:[/BOLD] Control total sobre la ejecución\n\n"

            "[SUBTITLE]DESVENTAJAS:[/SUBTITLE]\n"
            "• [BOLD]Complejidad alta:[/BOLD] Curva de aprendizaje pronunciada\n"
            "• [BOLD]Portabilidad nula:[/BOLD] Dependiente de arquitectura específica\n"
            "• [BOLD]Desarrollo lento:[/BOLD] Mayor tiempo de programación\n"
            "• [BOLD]Mantenimiento difícil:[/BOLD] Código menos legible y documentable\n"
            "• [BOLD]Propenso a errores:[/BOLD] Gestión manual de memoria y recursos\n\n"

            "[SUBTITLE]APLICACIONES TÍPICAS:[/SUBTITLE]\n"
            "• [BOLD]Sistemas operativos:[/BOLD] Kernel, drivers, boot loaders\n"
            "• [BOLD]Sistemas embebidos:[/BOLD] Microcontroladores, IoT\n"
            "• [BOLD]Aplicaciones críticas:[/BOLD] Sistemas de tiempo real\n"
            "• [BOLD]Optimización:[/BOLD] Rutinas críticas en rendimiento\n"
            "• [BOLD]Reversing:[/BOLD] Análisis de malware y ingeniería inversa\n\n"

            "[SUBTITLE]CONCEPTOS BÁSICOS:[/SUBTITLE]\n"
            "Los conceptos básicos del lenguaje ensamblador incluyen la comprensión de la sintaxis, "
            "la organización del código en secciones, y las convenciones específicas de cada ensamblador.\n\n"

            "[SUBTITLE]ELEMENTOS SINTÁCTICOS FUNDAMENTALES:[/SUBTITLE]\n"
            "[BOLD]• Etiquetas (Labels):[/BOLD] Marcadores para direcciones de memoria\n"
            "[BOLD]• Instrucciones (Instructions):[/BOLD] Operaciones del procesador\n"
            "[BOLD]• Operandos (Operands):[/BOLD] Datos sobre los que operan las instrucciones\n"
            "[BOLD]• Directivas (Directives):[/BOLD] Comandos para el ensamblador\n"
            "[BOLD]• Comentarios (Comments):[/BOLD] Documentación del código\n\n"

            "[SUBTITLE]SINTAXIS: NASM vs MASM:[/SUBTITLE]\n"
            "Existen múltiples ensambladores con sintaxis y características diferentes. "
            "Los más populares son NASM (Netwide Assembler) y MASM (Microsoft Macro Assembler).\n\n"

            "[SUBTITLE]NASM (NETWIDE ASSEMBLER):[/SUBTITLE]\n"
            "NASM es un ensamblador multiplataforma gratuito y de código abierto:\n\n"

            "[BOLD]• Características principales:[/BOLD]\n"
            "  - Sintaxis Intel clara y consistente\n"
            "  - Multiplataforma (Windows, Linux, macOS)\n"
            "  - Soporte para múltiples formatos de salida\n"
            "  - Macros potentes y flexibles\n"
            "  - Documentación extensa y comunidad activa\n\n"

            "[BOLD]• Sintaxis de instrucciones NASM:[/BOLD]\n"
            "  - Formato: [etiqueta:] instrucción [operandos] [; comentario]\n"
            "  - Orden Intel: instrucción destino, fuente\n"
            "  - Ejemplo: mov eax, ebx        ; EAX = EBX\n"
            "  - Tamaños explícitos: mov byte [esi], 0\n"
            "  - Sin sufijos de tamaño en instrucciones\n\n"

            "[BOLD]• Directivas NASM comunes:[/BOLD]\n"
            "  - section .text    ; Sección de código\n"
            "  - section .data    ; Sección de datos inicializados\n"
            "  - section .bss     ; Sección de datos no inicializados\n"
            "  - global _start    ; Símbolo global\n"
            "  - extern printf    ; Símbolo externo\n"
            "  - db, dw, dd, dq   ; Definir datos (8, 16, 32, 64 bits)\n"
            "  - resb, resw, resd ; Reservar espacio\n\n"

            "[BOLD]• Ejemplo completo NASM (Linux x86-64):[/BOLD]\n"
            "  section .data\n"
            "      msg db 'Hello, World!', 0xA, 0    ; Mensaje con newline\n"
            "      msg_len equ $ - msg - 1            ; Longitud del mensaje\n"
            "  \n"
            "  section .text\n"
            "      global _start\n"
            "  \n"
            "  _start:\n"
            "      ; Syscall write (sys_write = 1)\n"
            "      mov rax, 1          ; Número de syscall\n"
            "      mov rdi, 1          ; File descriptor (stdout)\n"
            "      mov rsi, msg        ; Puntero al mensaje\n"
            "      mov rdx, msg_len    ; Número de bytes\n"
            "      syscall             ; Llamar al kernel\n"
            "      \n"
            "      ; Syscall exit (sys_exit = 60)\n"
            "      mov rax, 60         ; Número de syscall\n"
            "      mov rdi, 0          ; Código de salida\n"
            "      syscall             ; Llamar al kernel\n\n"

            "[SUBTITLE]MASM (MICROSOFT MACRO ASSEMBLER):[/SUBTITLE]\n"
            "MASM es el ensamblador oficial de Microsoft para arquitecturas x86:\n\n"

            "[BOLD]• Características principales:[/BOLD]\n"
            "  - Integración total con Visual Studio\n"
            "  - Soporte avanzado de macros\n"
            "  - Extensiones específicas de Microsoft\n"
            "  - Optimizado para desarrollo en Windows\n"
            "  - Tipos de datos de alto nivel\n\n"

            "[BOLD]• Sintaxis MASM distintiva:[/BOLD]\n"
            "  - Directivas con punto: .386, .model, .code\n"
            "  - Definición de procedimientos: PROC/ENDP\n"
            "  - Tipos de datos: BYTE, WORD, DWORD, QWORD\n"
            "  - Estructuras: STRUCT/ENDS\n"
            "  - Condicionales: IF/ENDIF\n\n"

            "[BOLD]• Ejemplo MASM (Windows x86):[/BOLD]\n"
            "  .386\n"
            "  .model flat, stdcall\n"
            "  .stack 4096\n"
            "  \n"
            "  .data\n"
            "      msg BYTE 'Hello, World!', 0\n"
            "  \n"
            "  .code\n"
            "  include \\masm32\\include\\windows.inc\n"
            "  include \\masm32\\include\\kernel32.inc\n"
            "  include \\masm32\\include\\user32.inc\n"
            "  \n"
            "  start:\n"
            "      invoke MessageBox, NULL, addr msg, addr msg, MB_OK\n"
            "      invoke ExitProcess, 0\n"
            "  end start\n\n"

            "[SUBTITLE]COMPARACIÓN NASM vs MASM:[/SUBTITLE]\n\n"
            "| Aspecto          | NASM                    | MASM                   |\n"
            "|------------------|-------------------------|------------------------|\n"
            "| Plataforma       | Multiplataforma         | Windows principalmente |\n"
            "| Licencia         | BSD (código abierto)    | Propietaria Microsoft  |\n"
            "| Sintaxis         | Intel pura              | Intel con extensiones  |\n"
            "| Macros           | Básicas pero potentes   | Muy avanzadas         |\n"
            "| Tipos de datos   | Básicos                 | Alto nivel            |\n"
            "| Curva aprendizaje| Moderada               | Empinada              |\n"
            "| Comunidad        | Activa y global        | Específica Windows    |\n"
            "| Documentación    | Excelente              | Muy completa          |\n\n"

            "[SUBTITLE]SECCIONES DEL PROGRAMA:[/SUBTITLE]\n"
            "Los programas en ensamblador se organizan en secciones que definen diferentes "
            "tipos de datos y código con características específicas de memoria.\n\n"

            "[SUBTITLE]SECCIÓN .TEXT (CÓDIGO):[/SUBTITLE]\n"
            "Contiene las instrucciones ejecutables del programa:\n\n"

            "[BOLD]• Características:[/BOLD]\n"
            "  - Solo lectura y ejecución (R-X)\n"
            "  - Cargada en segmento de código\n"
            "  - Compartible entre procesos\n"
            "  - Optimizada para caché de instrucciones\n\n"

            "[BOLD]• Contenido típico:[/BOLD]\n"
            "  - Instrucciones del procesador\n"
            "  - Punto de entrada del programa (_start, main)\n"
            "  - Procedimientos y funciones\n"
            "  - Código de inicialización y finalización\n\n"

            "[BOLD]• Ejemplo:[/BOLD]\n"
            "  section .text\n"
            "      global _start\n"
            "  _start:\n"
            "      mov eax, 1          ; Código de operación\n"
            "      mov ebx, 0          ; Código de salida\n"
            "      int 0x80            ; Llamada al sistema\n\n"

            "[SUBTITLE]SECCIÓN .DATA (DATOS INICIALIZADOS):[/SUBTITLE]\n"
            "Almacena variables y constantes con valores iniciales:\n\n"

            "[BOLD]• Características:[/BOLD]\n"
            "  - Lectura y escritura (RW-)\n"
            "  - Valores conocidos en tiempo de compilación\n"
            "  - Ocupa espacio en el archivo ejecutable\n"
            "  - Cargada en memoria junto con el programa\n\n"

            "[BOLD]• Directivas de definición de datos:[/BOLD]\n"
            "  - DB (Define Byte): 8 bits\n"
            "    * db 0x41              ; Un byte con valor 65 ('A')\n"
            "    * db 'Hello', 0        ; Cadena terminada en null\n"
            "    * db 10, 20, 30        ; Array de bytes\n\n"
            
            "  - DW (Define Word): 16 bits\n"
            "    * dw 1000              ; Palabra de 16 bits\n"
            "    * dw 0x1234            ; Valor hexadecimal\n"
            "    * dw -1                ; Valor con signo\n\n"
            
            "  - DD (Define Doubleword): 32 bits\n"
            "    * dd 100000            ; Doble palabra\n"
            "    * dd 3.14159           ; Número en punto flotante\n"
            "    * dd $ - start         ; Dirección calculada\n\n"
            
            "  - DQ (Define Quadword): 64 bits\n"
            "    * dq 0x123456789ABCDEF ; Valor de 64 bits\n"
            "    * dq 1.7976931348623157e+308  ; Double precision\n\n"

            "[BOLD]• Ejemplo completo:[/BOLD]\n"
            "  section .data\n"
            "      mensaje db 'Programa en Assembly', 0xA, 0\n"
            "      longitud equ $ - mensaje - 1\n"
            "      numero dd 42\n"
            "      array dw 1, 2, 3, 4, 5\n"
            "      PI dd 3.14159265\n\n"

            "[SUBTITLE]SECCIÓN .BSS (DATOS NO INICIALIZADOS):[/SUBTITLE]\n"
            "Reserva espacio para variables sin valor inicial:\n\n"

            "[BOLD]• Características:[/BOLD]\n"
            "  - Lectura y escritura (RW-)\n"
            "  - Inicializada automáticamente a cero\n"
            "  - No ocupa espacio en el archivo ejecutable\n"
            "  - Eficiente para arrays grandes\n\n"

            "[BOLD]• Directivas de reserva:[/BOLD]\n"
            "  - RESB (Reserve Byte): Reserva bytes\n"
            "    * buffer resb 1024     ; Buffer de 1024 bytes\n"
            "    * temp resb 1          ; Variable temporal\n\n"
            
            "  - RESW (Reserve Word): Reserva palabras\n"
            "    * valores resw 100     ; Array de 100 words\n\n"
            
            "  - RESD (Reserve Doubleword): Reserva doble palabras\n"
            "    * resultado resd 1     ; Variable de 32 bits\n\n"
            
            "  - RESQ (Reserve Quadword): Reserva cuádruple palabras\n"
            "    * punteros resq 10     ; Array de 10 punteros de 64 bits\n\n"

            "[BOLD]• Ejemplo:[/BOLD]\n"
            "  section .bss\n"
            "      input_buffer resb 256    ; Buffer de entrada\n"
            "      counter resd 1           ; Contador de 32 bits\n"
            "      matrix resw 100          ; Matriz de 10x10 words\n\n"

            "[SUBTITLE]SECCIONES ADICIONALES:[/SUBTITLE]\n"
            "• .rodata: Datos de solo lectura (constantes)\n"
            "• .stack: Definición explícita de pila\n"
            "• .heap: Área de memoria dinámica\n"
            "• Secciones personalizadas: Para propósitos específicos\n\n"

            "[SUBTITLE]INSTRUCCIONES:[/SUBTITLE]\n"
            "Las instrucciones son los comandos que el procesador puede ejecutar directamente. "
            "Se clasifican en categorías según su funcionalidad.\n\n"

            "[SUBTITLE]FORMATO GENERAL DE INSTRUCCIONES:[/SUBTITLE]\n"
            "• Estructura: [prefijo] opcode [operando1] [, operando2] [, operando3]\n"
            "• Prefijos: Modifican el comportamiento (REP, LOCK, segment override)\n"
            "• Opcode: Código de operación que especifica la acción\n"
            "• Operandos: Fuentes y destinos de datos (0-3 operandos típicamente)\n\n"

            "[SUBTITLE]TIPOS DE OPERANDOS:[/SUBTITLE]\n"
            "• Inmediato: Valor constante incluido en la instrucción\n"
            "• Registro: Nombre de registro del procesador\n"
            "• Memoria: Referencia a ubicación en memoria\n"
            "• Implícito: Operando asumido por la instrucción\n\n"

            "[SUBTITLE]MANEJO DE REGISTROS:[/SUBTITLE]\n"
            "Las instrucciones de manejo de registros transfieren y manipulan datos "
            "entre registros y memoria de manera eficiente.\n\n"

            "[SUBTITLE]INSTRUCCIÓN MOV (MOVE):[/SUBTITLE]\n"
            "La instrucción más fundamental, copia datos del origen al destino:\n\n"
            
            "[BOLD]• Sintaxis:[/BOLD] MOV destino, origen\n"
            "[BOLD]• Características:[/BOLD]\n"
            "  - No afecta flags (excepto en algunos casos especiales)\n"
            "  - Operación no destructiva en el origen\n"
            "  - Versátil: registro-registro, registro-memoria, inmediato-registro\n\n"

            "[BOLD]• Variantes por tamaño:[/BOLD]\n"
            "  - MOV AL, BL        ; 8 bits (byte)\n"
            "  - MOV AX, BX        ; 16 bits (word)\n"
            "  - MOV EAX, EBX      ; 32 bits (doubleword)\n"
            "  - MOV RAX, RBX      ; 64 bits (quadword)\n\n"

            "[BOLD]• Modos de direccionamiento con MOV:[/BOLD]\n"
            "  - Inmediato a registro: MOV EAX, 100\n"
            "  - Registro a registro: MOV EBX, EAX\n"
            "  - Memoria a registro: MOV EAX, [direccion]\n"
            "  - Registro a memoria: MOV [direccion], EAX\n"
            "  - Inmediato a memoria: MOV DWORD [direccion], 100\n\n"

            "[BOLD]• Restricciones importantes:[/BOLD]\n"
            "  - No se puede mover memoria a memoria directamente\n"
            "  - No se puede mover inmediato a registro de segmento\n"
            "  - Tamaños de operandos deben coincidir\n\n"

            "[BOLD]• Ejemplos prácticos:[/BOLD]\n"
            "  ; Inicialización de variables\n"
            "  mov eax, 0              ; Limpiar EAX\n"
            "  mov ebx, [contador]     ; Cargar variable\n"
            "  mov [resultado], eax    ; Guardar resultado\n"
            "  \n"
            "  ; Carga de constantes\n"
            "  mov ecx, 1000           ; Contador de bucle\n"
            "  mov esi, buffer         ; Puntero a datos\n\n"

            "[SUBTITLE]INSTRUCCIÓN XCHG (EXCHANGE):[/SUBTITLE]\n"
            "Intercambia el contenido de dos operandos atómicamente:\n\n"

            "[BOLD]• Sintaxis:[/BOLD] XCHG operando1, operando2\n"
            "[BOLD]• Características:[/BOLD]\n"
            "  - Operación atómica (importante en multiprocesamiento)\n"
            "  - Implica LOCK automático para operandos de memoria\n"
            "  - No requiere registro auxiliar\n"
            "  - No afecta flags\n\n"

            "[BOLD]• Casos de uso:[/BOLD]\n"
            "  - Intercambio simple: XCHG EAX, EBX\n"
            "  - Sincronización: XCHG [semaforo], EAX\n"
            "  - Algoritmos de ordenamiento: XCHG [array+i], [array+j]\n\n"

            "[BOLD]• Comparación con intercambio manual:[/BOLD]\n"
            "  ; Método tradicional (3 instrucciones)\n"
            "  mov edx, eax\n"
            "  mov eax, ebx\n"
            "  mov ebx, edx\n"
            "  \n"
            "  ; Con XCHG (1 instrucción)\n"
            "  xchg eax, ebx\n\n"

            "[SUBTITLE]OTRAS INSTRUCCIONES DE MOVIMIENTO:[/SUBTITLE]\n\n"
            "[BOLD]LEA (LOAD EFFECTIVE ADDRESS):[/BOLD]\n"
            "• Calcula la dirección efectiva sin acceder a memoria\n"
            "• Sintaxis: LEA registro, [expresión_dirección]\n"
            "• Ejemplo: LEA ESI, [EBX + ECX*2 + 10]\n"
            "• Uso: Aritmética rápida, cálculo de direcciones\n\n"

            "[BOLD]MOVSX (MOVE WITH SIGN EXTENSION):[/BOLD]\n"
            "• Mueve con extensión de signo para números con signo\n"
            "• Ejemplo: MOVSX EAX, BL  ; BL (-1) → EAX (0xFFFFFFFF)\n\n"

            "[BOLD]MOVZX (MOVE WITH ZERO EXTENSION):[/BOLD]\n"
            "• Mueve con extensión de ceros\n"
            "• Ejemplo: MOVZX EAX, BL  ; BL (0xFF) → EAX (0x000000FF)\n\n"
            
            "[BOLD]INSTRUCCIONES ARITMÉTICAS:[/BOLD]\n"
            "Las instrucciones aritméticas realizan operaciones matemáticas y afectan "
            "los flags de estado del procesador.\n\n"
            
            "[BOLD]INSTRUCCIÓN ADD (ADDITION):[/BOLD]\n"
            "Suma dos operandos y almacena el resultado en el destino:\n\n"
            
            "[BOLD]• Sintaxis: [/BOLD]ADD destino, origen\n"
            "[BOLD]• Operación: [/BOLD]destino = destino + origen\n"
            "[BOLD]• Flags afectados:[/BOLD] CF, PF, AF, ZF, SF, OF\n\n"
            
            "[BOLD]• Variantes y ejemplos:[/BOLD]\n"
            "  ADD AL, BL              ; Suma de 8 bits\n"
            "  ADD AX, BX              ; Suma de 16 bits\n"
            "  ADD EAX, EBX            ; Suma de 32 bits\n"
            "  ADD RAX, RBX            ; Suma de 64 bits\n"
            "  ADD EAX, 100            ; Suma con inmediato\n"
            "  ADD DWORD [var], 5      ; Suma a variable en memoria\n\n"
            
            "[BOLD]• Flags importantes:[/BOLD]\n"
            "  - Carry Flag (CF): Set si hay acarreo del bit más significativo\n"
            "  - Zero Flag (ZF): Set si el resultado es cero\n"
            "  - Overflow Flag (OF): Set si hay desbordamiento con signo\n"
            "  - Sign Flag (SF): Copia del bit más significativo del resultado\n\n"
            
            "[BOLD]ADC (ADD WITH CARRY):[/BOLD]\n"
            "• Suma incluyendo el flag de acarreo previo\n"
            "• Esencial para aritmética de precisión múltiple\n"
            "• Ejemplo para suma de 64 bits en 32 bits:\n"
            "  add eax, ebx    ; Suma parte baja\n"
            "  adc edx, ecx    ; Suma parte alta + carry\n\n"
            
            "[SUBTITLE]INSTRUCCIÓN SUB (SUBTRACTION):[/SUBTITLE]\n"
            "Resta el origen del destino:\n\n"
            
            "[BOLD]• Sintaxis: [/BOLD]SUB destino, origen\n"
            "[BOLD]• Operación: [/BOLD]destino = destino - origen\n"
            "[BOLD]• Implementación: [/BOLD]Suma con complemento a dos\n"
            "[BOLD]• Flags afectados:[/BOLD] CF, PF, AF, ZF, SF, OF\n\n"
            
            "[BOLD]• Ejemplos:[/BOLD]\n"
            "  SUB EAX, EBX            ; EAX = EAX - EBX\n"
            "  SUB EAX, 50             ; EAX = EAX - 50\n"
            "  SUB DWORD [contador], 1 ; Decrementar variable\n\n"
            
            "[BOLD]SBB (SUBTRACT WITH BORROW):[/BOLD]\n"
            "• Resta incluyendo el flag de acarreo (borrow)\n"
            "• Para aritmética de precisión múltiple\n\n"

            "[SUBTITLE]INSTRUCCIONES DE INCREMENTO/DECREMENTO:[/SUBTITLE]\n"

            "[BOLD]INC (INCREMENT):[/BOLD]\n"
            "• Incrementa en 1 el operando\n"
            "• Más eficiente que ADD reg, 1\n"
            "• No afecta el Carry Flag\n"
            "• Ejemplo: INC EAX, INC DWORD [contador]\n\n"

            "[BOLD]DEC (DECREMENT):[/BOLD]\n"
            "• Decrementa en 1 el operando\n"
            "• Más eficiente que SUB reg, 1\n"
            "• No afecta el Carry Flag\n"
            "• Ejemplo: DEC ECX, DEC BYTE [var]\n\n"

            "[SUBTITLE]INSTRUCCIÓN MUL (UNSIGNED MULTIPLY):[/SUBTITLE]\n"
            "Multiplicación sin signo de precisión completa:\n\n"
            
            "[BOLD]• Sintaxis:[/BOLD] MUL operando\n"
            "[BOLD]• Operandos implícitos según tamaño:[/BOLD]\n"
            "  - MUL BH: AL × BH → AX\n"
            "  - MUL BX: AX × BX → DX:AX\n"
            "  - MUL EBX: EAX × EBX → EDX:EAX\n"
            "  - MUL RBX: RAX × RBX → RDX:RAX\n\n"
            
            "[BOLD]• Características:[/BOLD]\n"
            "  - Always produce resultado de doble tamaño\n"
            "  - CF y OF indican si la parte alta es no-cero\n"
            "  - Otros flags indefinidos\n\n"
            
            "[BOLD]• Ejemplo práctico:[/BOLD]\n"
            "  mov eax, 1000000     ; Multiplicando\n"
            "  mov ebx, 2000000     ; Multiplicador\n"
            "  mul ebx              ; EDX:EAX = 2,000,000,000,000\n"
            "  ; EDX contiene parte alta, EAX parte baja\n\n"

            "[SUBTITLE]IMUL (SIGNED MULTIPLY):[/SUBTITLE]\n"
            "[BOLD]• Multiplicación con signo[/BOLD]\n"
            "[BOLD]• Múltiples formas:[/BOLD]\n"
            "  - IMUL operando (como MUL pero con signo)\n"
            "  - IMUL reg, operando (resultado en registro especificado)\n"
            "  - IMUL reg, operando, inmediato\n\n"

            "[BOLD]• Ejemplos:[/BOLD]\n"
            "  imul ebx              ; EDX:EAX = EAX × EBX\n"
            "  imul eax, ebx         ; EAX = EAX × EBX\n"
            "  imul eax, ebx, 5      ; EAX = EBX × 5\n\n"

            "[SUBTITLE]INSTRUCCIÓN DIV (UNSIGNED DIVISION):[/SUBTITLE]\n"
            "División sin signo con cociente y residuo:\n\n"
            
            "[BOLD]• Sintaxis: [/BOLD]DIV operando\n"
            "[BOLD]• Operandos implícitos:[/BOLD]\n"
            "  - DIV BH: AX ÷ BH → AL (cociente), AH (residuo)\n"
            "  - DIV BX: DX:AX ÷ BX → AX (cociente), DX (residuo)\n"
            "  - DIV EBX: EDX:EAX ÷ EBX → EAX (cociente), EDX (residuo)\n\n"

            "[BOLD]• Consideraciones importantes:[/BOLD]\n"
            "  - División por cero genera excepción\n"
            "  - Desbordamiento si cociente no cabe en destino\n"
            "  - Flags indefinidos después de la operación\n\n"
            
            "[BOLD]• Ejemplo seguro:[/BOLD]\n"
            "  mov edx, 0           ; Limpiar parte alta\n"
            "  mov eax, 1000        ; Dividendo\n"
            "  mov ebx, 30          ; Divisor\n"
            "  div ebx              ; EAX = 33, EDX = 10\n\n"

            "[SUBTITLE]IDIV (SIGNED DIVISION):[/SUBTITLE]\n"
            "[BOLD]• División con signo[/BOLD]\n"
            "[BOLD]• Requiere extensión de signo del dividendo[/BOLD]\n"
            "[BOLD]• Instrucciones auxiliares:[/BOLD]\n"
            "  - CBW: AL → AX (byte a word)\n"
            "  - CWD: AX → DX:AX (word a doubleword)\n"
            "  - CDQ: EAX → EDX:EAX (doubleword a quadword)\n"
            "  - CQO: RAX → RDX:RAX (quadword a double-quadword)\n\n"

            "[BOLD]• Ejemplo con división con signo:[/BOLD]\n"
            "  mov eax, -100        ; Dividendo negativo\n"
            "  cdq                  ; Extender signo a EDX:EAX\n"
            "  mov ebx, 7           ; Divisor\n"
            "  idiv ebx             ; EAX = -14, EDX = -2\n\n"
        ),
        "url" : "https://wayground.com/admin/assessment/6881b47ed5e319aa5044d04a?source=lesson_share"
    },
}