"""La función tijera() al ser ejecutada solicita a los jugadores cuántas rondas quieren jugar y una
elección entre piedra papel o tijera, posteriormente las compara y registra cuántas veces ganó o perdió
cada uno. Al terminar las rondas elegidas el programa emplea las rondas ganadas de cada jugador y les
da las estadísticas de sus partidas."""

import random
def tijeraJugadores():
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    
    """
    Se crearon dos listas (ListaA y ListaB) para almacenar las elecciones de los jugadores
    Matriz almacena las dos listas previamente mencionadas para luego mostrarselas al usuario
    ListaResultados almacena el resultado de cada juego para mostrarlo al final de la partida
    """
    
    Matriz=[]
    ListaA=[]
    ListaB=[]
    ListaResultados=[]
    
    
    numinicial=int(input("¿Cuántas veces quiere jugar? "))
    while i < numinicial:
        i = i+1
    
        print("\n \n \n \n \n \n Partida número", i, "\n \n 1=Piedra \n 2=Papel \n 3=Tijera \n")
        
        """El ciclo while se emplea para que el programa no se rompa cuando se elija un número diferente a 1, 2 o 3
        solicitando un nuevo valor cada vez. Este ciclo se emplea para todas las entradas de las funciones tijera() y
        tijeracompu(). """
        
        x=0
        
        
        while x<1:
            
            a=int(input("Jugador 1 \n \n escoge 1,2 o 3 "))
            if a == 1 or a== 2 or a== 3:
                
                #Se almacena la eleccion del jugador A en la listaA solo si esta está dentro de 1, 2, 3
                ListaA.append(a)
                
                x=1
            else:
                print("Error elija de nuevo")
                x=0
                
        print("\n \n \n \n \n \n Partida número", i, "\n \n 1=Piedra \n 2=Papel \n 3=Tijera \n ")
        x=0
        
        
        while x<1:
            b=int(input("Jugador 2 \n \n escoge 1,2 o 3 "))
            if b == 1 or b== 2 or b== 3:
                ListaB.append(b)
               
                x=1
            else:
                print("Error elija de nuevo")
                x=0

        if b==a:
            ListaResultados.append("Empate")
            SCOREemp=SCOREemp+1
          
        elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
            ListaResultados.append("Gana jugador 1")
            SCORE1=SCORE1+1
          
        elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
            ListaResultados.append("Gana jugador 2")
            SCORE2=SCORE2+1
            
    #Se insertan las listas de las elecciones de los jugadores en una matriz        
    Matriz.insert(0,ListaA)
    Matriz.insert(1,ListaB)
    #Se imprimen las elecciones
    print("Las elecciones de los jugadores fueron ", Matriz)
    #Se imprimen los resultados de las interacciones
    print(ListaResultados)
    #Se imprime la estadística de los jugadores
    estadística(SCORE1, SCORE2, SCOREemp, numinicial)
    
    
    
""" La función tijeracompu() realiza el mismo prceso que la función tijera() cambiando el dato elejido por una variable
entera generada aleatoriamente."""
def tijeracompu():
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    
    Matriz=[]
    ListaA=[]
    ListaB=[]
    ListaResultados=[]
    
    numinicial=int(input("¿Cuántas veces quiere jugar? "))
    while i < numinicial:
        i = i+1
    
        print("\n \n \n \n \n \n  Partida número", i, "\n \n 1=Piedra \n 2=Papel \n 3=Tijera \n")
        x=0
        conta=0
        while x<1:
            a=int(input("Jugador 1 \n \n escoge 1,2 o 3 "))
            if a == 1 or a== 2 or a== 3:
                ListaA.append(a)
                
                x=1
            else:
                print("Error elija de nuevo")
                x=0
    
        b=random.randint(1, 3)
        ListaB.append(b)
        
        
        
        if b==a:
            ListaResultados.append("Empate")
            SCOREemp=SCOREemp+1
          
        elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
            ListaResultados.append("Gana jugador 1")
            SCORE1=SCORE1+1
          
        elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
            ListaResultados.append("Gana jugador 2")
            SCORE2=SCORE2+1
            
            
    #Se insertan las listas de las elecciones de los jugadores en una matriz        
    Matriz.insert(0,ListaA)
    Matriz.insert(1,ListaB)
    #Se imprimen las elecciones
    print("Las elecciones de los jugadores fueron ", Matriz)
    #Se imprimen los resultados de las interacciones
    print(ListaResultados)
    #Se imprime la estadística de los jugadores
    estadística(SCORE1, SCORE2, SCOREemp, numinicial)

"""La función estadística(SCORE1, SCORE2, SCOREemp, numinicial) emplea los datos de las funciones tijera() y
tijeracompu() para calcular el porcentaje que gano o empató cada jugador."""

def estadística (SCORE1, SCORE2, SCOREemp, numinicial):
    stats1=SCORE1/numinicial*100
    stats2=SCORE2/numinicial*100
    statsEMP=SCOREemp/numinicial*100

    print("El jugador 1 ganó ",SCORE1, " veces \n Gano el ",stats1,"% de las veces")
    print("El jugador 2 ganó ",SCORE2, " veces \n Gano el ",stats2,"% de las veces")
    print("Empataron ",SCOREemp, " veces \n Empataron el ",statsEMP,"% de las veces")
    

"""
Se creo la función prueba que recibe datos hardcodeados para verificar que los resultados sean los esperados
Esta funcion prueba al mismo tiempo las funciones de tijeraJugadores() y tijeracompu() pues funcionan de forma similar excepto por
la variable b que se genera mediante un random en la segunda. De igual forma se prueba la función estadística() pues está integrada
dentro de las funciones mencionadas.
"""
def prueba():
    
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    
    """
    Se crearon dos listas (ListaA y ListaB) para almacenar las elecciones de los jugadores
    Matriz almacena las dos listas previamente mencionadas para luego mostrarselas al usuario
    ListaResultados almacena el resultado de cada juego para mostrarlo al final de la partida
    """
    
    Matriz=[]
    ListaA=[]
    ListaB=[]
    ListaResultados=[]
    
    """
    Igualamos número inicial a 3 para que solo juegue 3 veces
    """
    numinicial=3
    
    while i < numinicial:
        i = i+1
    
        print("\n \n \n \n \n \n Partida número", i, "\n \n 1=Piedra \n 2=Papel \n 3=Tijera \n")
        
        
        x=0
        while x<1:
            
            """
            a=i para que en este caso el jugador elija piedra, luego papel y luego tijera
            """
            
            a=i
            
            print ("El valor de a es ", a)
            
            if a == 1 or a== 2 or a== 3:
                
                #Se almacena la eleccion del jugador A en la listaA solo si esta está dentro de 1, 2, 3
                ListaA.append(a)
                
                x=1
            else:
                print("Error elija de nuevo")
                x=0
                
        print("\n \n \n \n \n \n Partida número", i, "\n \n 1=Piedra \n 2=Papel \n 3=Tijera \n ")
        x=0
        
        
        while x<1:
            
            """
            b se compara con i para elegir tijera, papel y piedra en ese ordén de esta forma el resulrado esperado es que todos ganen 1 vez
            """
            if i==1:
                b=3
            elif i==2:
                b=2
            elif i==3:
                b=1
            
            print("El valor de b es ",b)
            
            if b == 1 or b== 2 or b== 3:
                ListaB.append(b)
               
                x=1
            else:
                print("Error elija de nuevo")
                x=0

        if b==a:
            ListaResultados.append("Empate")
            SCOREemp=SCOREemp+1
          
        elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
            ListaResultados.append("Gana jugador 1")
            SCORE1=SCORE1+1
          
        elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
            ListaResultados.append("Gana jugador 2")
            SCORE2=SCORE2+1
            
            
    print("\n Los valores esperados son [[1,2,3],[3,2,1]] \n [Gana jugador1, Empate, Gana jugador 2] \n ")
    print("El jugador 1 ganó ",1, " veces \n Gano el ",33.3333,"% de las veces")
    print("El jugador 2 ganó ",1, " veces \n Gano el ",33.3333,"% de las veces")
    print("Empataron ",1, " veces \n Empataron el ",33.3333,"% de las veces")
    
    print("\n Los resultados obtenidos son: \n")
    
    #Se insertan las listas de las elecciones de los jugadores en una matriz        
    Matriz.insert(0,ListaA)
    Matriz.insert(1,ListaB)
    #Se imprimen las elecciones
    print("Las elecciones de los jugadores fueron ", Matriz)
    #Se imprimen los resultados de las interacciones
    print(ListaResultados)
    #Se imprime la estadística de los jugadores
    estadística(SCORE1, SCORE2, SCOREemp, numinicial)


""" La función main() se ejecuta al iniciar el programa. Esta despliega un menú con las opciones disponibles y guarda
la elección del usuario en la variable decision. Posteriormente dependiendo del valor de decision manda a llamar la
función correspondiente a la elección del usuario"""
def main():
    
    decision= int(input("Elija qué desea jugar 1 o 2 \n 1. Piedra, papel o tijera multijugador \n 2.Piedra, papel o tijera un jugador \n 3.Prueba \n"))
    if decision == 1:
        tijeraJugadores()
    elif decision == 2:
        tijeracompu()
    elif decision == 3:
        prueba()
    else:
        print("Elección no válida")
    
main()