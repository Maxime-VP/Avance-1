# Piedra papel y tijeras multijugador local y vs cpu

En un futuro yo aspiro a poder convertirme en un programador de videojuegos, sin embargo a día de hoy no cuento con todas las habilidades necesarias para hacerlo. En este proyecto mi objetivo es poder programar un juego sencillo con el conocimiento que he adquirido. 
Tras contemplar varias opciones me he decidido en programar un juego de piedra papel o tijeras, este juego es relativamente sencillo desde una perspectiva lógica sin embargo, quiero incluir además, varias opciones de juego (multijugador local y un solo jugador contra la máquina), y un contador de victorias contra derrotas que se reinicie cuando se le ordene terminar de jugar.

Algoritmo

ENTRADA:
Multijugador local
Un jugador vs la computadora
Piedra 
Papel
Tijera

PROCESO:
Igualar una variable llamada SCORE_A a 0
Igualar una variable llamada SCORE_B a 0
Solicitar al usuario elegir un tipo de juego (multijugador local o vs la computadora)
Validar que sea un tipo de juego válido
Solicitar al usuario (a) su elección (piedra, papel o tijera) [Almacenar el dato en una variable A]
Validar que la elección sea válida
Si se seleccionó multijugador local, solicitar al segundo usuario su elección (piedra papel o tijera) [Almacenar el dato en variable B]
Validar la elección del segundo jugador
Si se seleccionó vs la computadora, generar un número de 1-3
Por medio de funciones if, elif y else, transformar el número obtenido a piedra (1), Papel (2) o tijera (3) [Almacenar el dato en variable B]
Emplear funciones if, elif, else en conjunto con and para determinar quien gana o si es un empate
Si gana el jugador A, aumentar en 1 la variable SCORE_A
Si gana el jugador B o la consola, aumentar en 1 la variable SCORE_A
Solicitar si se desea seguir jugando
Si se selecciona que si, repetir desde solicitar al usuario (a) su elección
Alternativamente terminar el programa

SALIDA:
Ganador
SCORE_A
SCORE_B

Funcionamiento:
Requisitos: tener instalado el archivo “Piedra Papel o Tijeras c historial.py” y el al archivo “SCORES.txt” en una misma carpeta
Formas de correr el programa: 
•	Abrir el archivo con terminación .py en Thonny y darle play
•	Correr en terminal con python “Tijeras c historial.py”

	
El programa solicitara al usuario decidir entre cuatro opciones:

1. Jugador contra jugador
•	Pide el número de veces que se quiere jugar
•	Pide un valor a dos usuarios (se repite el número de veces seleccionado)
•	Compara e imprime las elecciones y los resultados

2. Jugador contra la máquina
•	Pide el número de veces que se quiere jugar
•	Pide un valor a un usuario y genera otro aleatoriamente (se repite el número de veces seleccionado)
•	Compara e imprime las elecciones y los resultados

3. Prueba
•	Juega 3 veces
•	Tiene hardcodeados los valores 1, 2, 3 para el jugador 1. Y 3, 2, 1 para el jugador 2
•	Compara e imprime las elecciones y los resultados

4. Salir
•	Termina el programa


Tras concretarse cualquiera de las primeras 3 opciones surge un menú con otras cuatro opciones:

1. Continuar jugando
•	Vuelve a solicitar al usuario que elija una de las cuatro primeras opciones

2. Revisar el historial
•	Lee un archivo que tiene guardadas los tipos de juego, elecciones y resultados anteriores

3. Borrar el historial
•	Elimina el contenido del historial

4. Salir
•	Termina el programa


