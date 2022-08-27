i=0
SCORE1=0
SCORE2=0
SCOREemp=0
numinicial=int(input("¿Cuántas veces quiere jugar? "))
while i < numinicial:
    i = i+1
    
    print("1=Piedra \n 2=Papel \n 3=Tijera")
    a=int(input("Jugador 1, escoge 1,2 o 3 "))
    
    b=int(input("Jugador 2, escoge 1,2 o 3 "))

    if b==a:
        print("\n Empate, no hay puntos\n")
        SCOREemp=SCOREemp+1
          
    elif a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
        print("\n Gana jugador 1\n")
        SCORE1=SCORE1+1
          
    elif b==1 and a==3 or b==2 and a==1 or b==3 and a==2:
        print("\n Gana jugador 2\n")
        SCORE2=SCORE2+1
        
    
stats1=SCORE1/numinicial*100
stats2=SCORE2/numinicial*100
statsEMP=SCOREemp/numinicial*100

print("El jugador 1 ganó ",SCORE1, " veces \n Gano el ",stats1,"% de las veces")
print("El jugador 2 ganó ",SCORE2, " veces \n Gano el ",stats2,"% de las veces")
print("Empataron ",SCOREemp, " veces \n Gano el ",statsEMP,"% de las veces")
    
