"""La función tijeraJugadores() al ser ejecutada solicita a los jugadores cuántas rondas quieren jugar y una
elección entre piedra papel o tijera, posteriormente las compara y registra cuántas veces ganó o perdió
cada uno. Al terminar las rondas elegidas el programa emplea las rondas ganadas de cada jugador y les
da las estadísticas de sus partidas."""

import random
def tijeraJugadores(archivo):
    
    """ tijeraJugadores() recibe las decisiones de dos jugadores y las compara para determinar quién gana """
    
    file = open(archivo, "a")
    file.write('\n'+ "    Partida jugador vs Jugador:" + '\n'+ '\n')
    file.close()
    
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
    estadistica(SCORE1, SCORE2, SCOREemp, numinicial)
    
    historial(ListaA, ListaB, ListaResultados, archivo)

def tijeracompu(archivo):
    
    """ tijeracompu recibe las decisiones de un jugador y genera una decisión de forma aleatoria y las compara para determinar quién gana """
    
    file = open(archivo, "a")
    file.write('\n'+"    Partida jugador vs Computadora:" + '\n'+ '\n')
    file.close()
    
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
    estadistica(SCORE1, SCORE2, SCOREemp, numinicial)

    historial(ListaA, ListaB, ListaResultados, archivo)

def estadistica (SCORE1, SCORE2, SCOREemp, numinicial):
    
    """ estadistica() recibe cuantas veces gano o empató cada jugador y promedia e imprime los resultados"""
    
    stats1=SCORE1/numinicial*100
    stats2=SCORE2/numinicial*100
    statsEMP=SCOREemp/numinicial*100

    print("El jugador 1 ganó ",SCORE1, " veces \n Gano el ",stats1,"% de las veces")
    print("El jugador 2 ganó ",SCORE2, " veces \n Gano el ",stats2,"% de las veces")
    print("Empataron ",SCOREemp, " veces \n Empataron el ",statsEMP,"% de las veces")
    

def prueba(archivo):
    
    """La función prueba verifica que el funcionamiento de las funciones sea correcto empleando valores hardcodeados """
    
    file = open(archivo, "a")
    file.write('\n'+"    Partida de Prueba:" + '\n' + '\n')
    file.close()
    
    i=0
    SCORE1=0
    SCORE2=0
    SCOREemp=0
    
    
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
    estadistica(SCORE1, SCORE2, SCOREemp, numinicial)
    
    historial(ListaA, ListaB, ListaResultados, archivo)
    
def historial(ListaA, ListaB, ListaResultados, archivo):
    
    """historial recibe las listas generadas y guarda su contenido en un archivo """
    
    
    """Esta funcion emplea .join(map(str,NombreDeLista)) para convertir el contenido de las listas a str para poder guardarlas en el archivo"""
    ListaAString=", ".join(map(str,ListaA))
    ListaBString=", ".join(map(str,ListaB))
    ListaResultadosString=" | ".join(map(str,ListaResultados))
    
    file = open(archivo, "a")
    file.write("Jugador uno eligió: " + ListaAString + '\n')
    file.write("Jugador dos eligió: " + ListaBString + '\n')
    
    file.write("Los resultados fueron:    " + ListaResultadosString + '\n')
    file.close()
    
    menu(archivo)
    
def menu(archivo):
    
    """menu recibe el archivo y le pregunta al usuario si desea jugar de nuevo, mostrar el historial, borrar el historial o salir"""
    
    print("\n Desea continuar jugando(1) \n Desea revisar el historial de partidas (2) \n Desea borrar el historial (3 \n Desea salir (4))")
    comprob= 0
    while comprob == 0:
        deci = int(input())
        if deci == 1:
            main()
            comprob = 1
            
        elif deci == 2:
            
            print("Historial:")
            file = open(archivo, "r")
            file.seek(0)
            historia=file.read()
            print(historia)
            file.close()
        elif deci == 3:
            file = open(archivo, "w")
            file.seek(0)
            file.write("")
            file.close()
        elif deci == 4:
            comprob = 1
        else:
            print("Error, escoja de nuevo")
            comprob = 0

def main():
    
    """Main() se ejecuta al iniciar el programa. Despliega un menú y ejecuta la función que elija el usuario"""
    
    archivo="SCORES.txt"
    comprob=0
    while comprob==0:
        decision= int(input("Elija qué desea jugar 1 o 2 \n 1. Piedra, papel o tijera multijugador \n 2.Piedra, papel o tijera un jugador \n 3.Prueba \n 4.Salir \n"))
        if decision == 1:
            tijeraJugadores(archivo)
            comprob=1
        elif decision == 2:
            tijeracompu(archivo)
            comprob=1
        elif decision == 3:
            prueba(archivo)
            comprob=1
        elif decision ==4:
            comprob=1
        
        else:
            print("Elección no válida")
            comprob=0
main()