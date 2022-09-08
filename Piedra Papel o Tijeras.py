"""La función tijera() al ser ejecutada solicita a los jugadores cuántas rondas quieren jugar y una
elección entre piedra papel o tijera, posteriormente las compara y registra cuántas veces ganó o perdió
cada uno. Al terminar las rondas elegidas el programa emplea las rondas ganadas de cada jugador y les
da las estadísticas de sus partidas."""

import random
def tijera():
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    numinicial=int(input("¿Cuántas veces quiere jugar? "))
    while i < numinicial:
        i = i+1
    
        print("1=Piedra \n 2=Papel \n 3=Tijera")
        
        """El ciclo while se emplea para que el programa no se rompa cuando se elija un número diferente a 1, 2 o 3
        solicitando un nuevo valor cada vez. Este ciclo se emplea para todas las entradas de las funciones tijera() y
        tijeracompu(). """
        
        x=0
        while x<1:
            a=int(input("Jugador 1, escoge 1,2 o 3 "))
            if a == 1 or a== 2 or a== 3:
                x=1
            else:
                print("Error elija de nuevo")
                x=0
                
        print("\n \n \n \n \n \n \n \n \n ")
        x=0
        while x<1:
            b=int(input("Jugador 2, escoge 1,2 o 3 "))
            if b == 1 or b== 2 or b== 3:
                x=1
            else:
                print("Error elija de nuevo")
                x=0

        if b==a:
            print("\n Empate, no hay puntos\n")
            SCOREemp=SCOREemp+1
          
        elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
            print("\n Gana jugador 1\n")
            SCORE1=SCORE1+1
          
        elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
            print("\n Gana jugador 2\n")
            SCORE2=SCORE2+1
        
    estadística(SCORE1, SCORE2, SCOREemp, numinicial)
    
""" La función tijeracompu() realiza el mismo prceso que la función tijera() cambiando el dato elejido por una variable
entera generada aleatoriamente."""
def tijeracompu():
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    numinicial=int(input("¿Cuántas veces quiere jugar? "))
    while i < numinicial:
        i = i+1
    
        print("1=Piedra \n 2=Papel \n 3=Tijera")
        x=0
        while x<1:
            a=int(input("Jugador 1, escoge 1,2 o 3 "))
            if a == 1 or a== 2 or a== 3:
                x=1
            else:
                print("Error elija de nuevo")
                x=0
    
        b=random.randint(1, 3)
        print("Jugador 2, escogió ", b)
        if b==a:
            print("\n Empate, no hay puntos\n")
            SCOREemp=SCOREemp+1
          
        elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
            print("\n Gana jugador 1\n")
            SCORE1=SCORE1+1
          
        elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
            print("\n Gana jugador 2\n")
            SCORE2=SCORE2+1
        
    estadística(SCORE1, SCORE2, SCOREemp, numinicial)

"""La función estadística(SCORE1, SCORE2, SCOREemp, numinicial) emplea los datos de las funciones tijera() y
tijeracompu() para calcular el porcentaje que gano o empató cada jugador."""

def estadística (SCORE1, SCORE2, SCOREemp, numinicial):
    stats1=SCORE1/numinicial*100
    stats2=SCORE2/numinicial*100
    statsEMP=SCOREemp/numinicial*100

    print("El jugador 1 ganó ",SCORE1, " veces \n Gano el ",stats1,"% de las veces")
    print("El jugador 2 ganó ",SCORE2, " veces \n Gano el ",stats2,"% de las veces")
    print("Empataron ",SCOREemp, " veces \n Gano el ",statsEMP,"% de las veces")


""" La función main() se ejecuta al iniciar el programa. Esta despliega un menú con las opciones disponibles y guarda
la elección del usuario en la variable decision. Posteriormente dependiendo del valor de decision manda a llamar la
función correspondiente a la elección del usuario"""
def main():
    decision= int(input("Elija qué desea jugar 1 o 2 \n 1. Piedra, papel o tijera multijugador \n 2.Piedra, papel o tijera un jugador \n"))
    if decision == 1:
        tijera()
    elif decision == 2:
        tijeracompu()
    else:
        print("Elección no válida")
    
main()