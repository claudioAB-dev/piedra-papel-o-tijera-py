import random

jugadapc = ""
man = 2
print("bienvenido al juego")
print("recuerda:")
print("1= piedra")
print("2= papel")
print("3= tijera")
while man < 4:
    pc = random.randint(1, 3)

    man = int(input())
    if pc == 1:
        jugadapc = "piedra"
    elif pc == 2:
        jugadapc = "papel"
    elif pc == 3:
        jugadapc = "tijera"

    """""
    1= piedra
    2= paple
    3= tijera
    """

    if pc == man:
        print(jugadapc)
        print("empate")
    elif man == 1 & pc == 2:
        print(jugadapc)
        print("perdiste")
    elif man == 1 & pc == 3:
        print(jugadapc)
        print("ganaste")
    elif man == 2 & pc == 1:
        print(jugadapc)
        print("ganaste")
    elif man == 2 & pc == 3:
        print(jugadapc)
        print("perdiste")
    elif man == 3 & pc == 1:
        print(jugadapc)
        print("perdiste")
    else:
        print(jugadapc)
        print("ganaste")
