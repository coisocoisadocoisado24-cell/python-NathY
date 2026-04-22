import os
import random
import time
# ---------------------------
# FUNÇÃO QUE AVALIA A MÃO
def definirmao(cartas):
    valores = [carta[0] for carta in cartas]
    naipes = [carta[1] for carta in cartas]

    valores.sort()

    # CONTAGEM
    contagem = {}
    for v in valores:
        contagem[v] = contagem.get(v, 0) + 1

    pares = 0
    trio = 0
    quad = 0

    for v in contagem.values():
        if v == 2:
            pares += 1
        elif v == 3:
            trio = 1
        elif v == 4:
            quad = 1

    # FLUSH
    flush = 0
    for n in naipes:
        if naipes.count(n) >= 5:
            flush = 1
            naipe_flush = n
            break

    # STRAIGHT
    valores_unicos = sorted(set(valores))
    seq = 1
    straight = 0

    for i in range(len(valores_unicos)-1):
        if valores_unicos[i] + 1 == valores_unicos[i+1]:
            seq += 1
            if seq >= 5:
                straight = 1
        else:
            seq = 1

    # Ás alto
    if 1 in valores_unicos:
        valores_unicos.append(14)
        valores_unicos.sort()

        seq = 1
        for i in range(len(valores_unicos)-1):
            if valores_unicos[i] + 1 == valores_unicos[i+1]:
                seq += 1
                if seq >= 5:
                    straight = 1
            else:
                seq = 1

    # STRAIGHT FLUSH / ROYAL
    straight_flush = 0
    royal = 0

    if flush:
        cartas_flush = [c for c in cartas if c[1] == naipe_flush]
        valores_flush = sorted(set([c[0] for c in cartas_flush]))

        if 1 in valores_flush:
            valores_flush.append(14)

        valores_flush.sort()

        seq = 1
        for i in range(len(valores_flush)-1):
            if valores_flush[i] + 1 == valores_flush[i+1]:
                seq += 1
                if seq >= 5:
                    straight_flush = 1
                    if set([10,11,12,13,14]).issubset(valores_flush):
                        royal = 1
            else:
                seq = 1

    # RESULTADO
    if royal:
        return "ROYAL FLUSH"
    elif straight_flush:
        return "STRAIGHT FLUSH"
    elif quad:
        return "QUADRA"
    elif trio and pares:
        return "FULL HOUSE"
    elif flush:
        return "FLUSH"
    elif straight:
        return "STRAIGHT"
    elif trio:
        return "TRINCA"
    elif pares >= 2:
        return "DOIS PARES"
    elif pares == 1:
        return "PAR"
    else:
        return "CARTA ALTA"


# ---------------------------
# JOGO

dinheiro = 200
aumento = 0
valores = list(range(1, 14))
naipes = ["Espadas", "Copas", "Ouros", "Paus"]

while dinheiro > 0:

    # cria baralho novo a cada rodada
    baralho = [(v, n) for v in valores for n in naipes]
    random.shuffle(baralho)
    pot = 0
    mesa = []
    mao_jogador1 = []
    mao_jogador2 = []
    print("\n--- NOVA RODADA ---")

    # 2 cartas do jogador 1
    print("PLAYER 1")
    for i in range(2):
        
        carta = baralho.pop()
        mao_jogador1.append(carta)
        print("Sua carta:", carta)
    print("sua mão é ", mao_jogador1)
    play = input("fold or check ou raise?")
    
    if play == "fold":
      print("player 2 ganhou por desistencia")
      time.sleep(2)
      break
    elif play == "check":
        os.system("cls")
    elif play== "raise":
        aumento = int(input("quanto gostaria de aumentar? "))
        pot += aumento
        os.system("cls")
# 2 cartas do jogador 2
    if aumento > 0 :
        print('PLAYER 1 AUMENTOU:', aumento)
        for i in range(2):
            print("PLAYER 2")
            carta = baralho.pop()
            mao_jogador2.append(carta)
            print("Sua carta:", carta)
        print("sua mão é ", mao_jogador2)
        
        play = input("fold or check")
        if play == "fold":
            print("player 1 ganhou por desistencia")
            time.sleep(2)
            break
            
        elif play == "pagar":
            os.system("cls")
            pot += aumento
            
    else:
        for i in range(2):
            carta = baralho.pop()
            mao_jogador2.append(carta)
            print("Sua carta:", carta)
        print("sua mão é ", mao_jogador2)
        play = input("fold or check ou raise?")
        if play == "fold":
            print("player 1 ganhou por desistencia")
            time.sleep(2)
            break
        elif play == "check":
            os.system("cls")

        elif play== "raise":
            aumento = int(input("quanto gostaria de aumentar? "))
            pot += aumento
            os.system("cls")
            time.sleep(1)
            print("player 2 aumentou",aumento," reais, gostaria de pagar ou desitir")
            play = input()
            if play == "pagar":
                pot+= aumento
            elif play == "fold":
                print("player 2 ganhou por desistencia")
                time.sleep(1)
                break
    
    # FLOP (3 cartas) (player 1)
    print("\nFLOP:")
    
    print("player 1")
    for i in range(3):
        carta = baralho.pop()
        mesa.append(carta)
        print(carta)
    print(mao_jogador1)
    play = input("fold or check ou raise")
    if play == "fold":
      print("jogador 2 ganhou por desistencia")
      time.sleep(3)
      break
    elif play == "check":
        os.system("cls")
    elif play == "raise":
        aumento =  int(input("quanto gostaria de aumentar?"))
        pot+= aumento
    #PLAYER 2 *FLOP*
    if aumento > 0:
        print("player 1 aumentou", aumento,"e as cartas são:")
        print(mesa)
        print(mao_jogador2)
        play == input("fold ou pagar?")
        if play == "pagar":
            pot += aumento
        if play == "fold":
            print("player 1 ganhou por desistencia")
            time.sleep(2)
            break
    else:
        
        print(mesa)

  # junta tudo (7 cartas)
        todas_cartas1 = mao_jogador1 + mesa
        total_cartas2 = mao_jogador2 + mesa
    print("\nSuas cartas + mesa:", todas_cartas1)
    print("\nSuas cartas + mesa:", total_cartas2)
    resultado = definirmao(todas_cartas1)
    resultado2 = definirmao(total_cartas2)
    print("\nMao o player 1 é: ", resultado)
    print("\nMao o player 2 é: ", resultado2)
    break