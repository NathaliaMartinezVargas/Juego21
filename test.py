from random import shuffle

def baraja():
    return [(n, p) for n in ['A', 'J', 'Q', 'K'] +[ str(x) for x in range (2,11)] for p in ['♥','♣','♦','♠']]

def mezclar(baraja):
    shuffle(baraja)
    return baraja

def sacar_carta(mazo):
    if mazo == []:
        pass
    else:
        print(mazo[0], valor_carta(mazo[0]))
        sacar_carta(mazo[1:])

def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def valor_mano(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_juego(mano):
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)

def repartir_mano_jugador(mazo, jugador, dealer):
    print(jugador)
    if len(mazo) > 2 and valor_juego(jugador) < 21 and input("Presione p para pedir carta, si no presione Enter: ")=="p":
        repartir_mano_jugador(mazo[1:], jugador+[mazo[0]], dealer)
    else:
        print("Cartas Jugador: \n" + str(jugador))
        repartir_mano_dealer(mazo, dealer, jugador)

def repartir_mano_dealer(mazo, dealer, jugador):
    if valor_juego(jugador) <= valor_juego(dealer) or valor_juego(jugador) > 21:
        print("Cartas Dealer: \n" + str(dealer))
        ganador_es(valor_juego(jugador), valor_juego(dealer))
    elif valor_juego(dealer) < 21:
        repartir_mano_dealer(mazo[1:], dealer+[mazo[0]], jugador )
        print (valor_juego(dealer[0]))
  

def ganador_es(jugador, dealer):
    if jugador > 21:
        print( jugador, dealer)
        print("Dealer Gana")
        return False
    elif dealer > 21 :
        print( jugador, dealer)
        print("Jugador Gana")
        return False
    elif jugador > dealer:
        print( jugador, dealer)
        print("Jugador Gana")
        return False
    else:
        print( jugador, dealer)
        print("Dealer Gana")
        return False
    return True

def jugar(mazo, jugador, dealer):
    repartir_mano_jugador(mazo[4:], jugador+[mazo[0]]+[mazo[1]], dealer+[mazo[2]]+[mazo[3]])
    

#print(mezclar(baraja ()))
#sacar_carta(mezclar(baraja()))
jugar(mezclar(baraja()),[],[])
