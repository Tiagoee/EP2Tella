import random
from Palavras import PALAVRAS
from Funcoes import filtra
from Funcoes import indica_posicao
from Funcoes import inicializa
from Regras import imprime_layout
from Regras import sorteando
from Regras import main

jogar = True
while jogar == True:
    #Instruções do Jogo
    print(imprime_layout())

    #Quantidade de Letras
    letras = int(input('Qual a quantidade de letras que a palavra deve ter?'))

    #Filtrando Palavras
    lista_palavras = filtra(PALAVRAS, letras)

    #Mensagem de Espera
    print(sorteando())

    #Informações da Rodada
    informações = inicializa(lista_palavras)

    #Percorrendo Dicionario
    for elemento, abc in informações.items():
        if elemento == 'sorteada':
            sorteada = abc

    #Exibindo o Jogo
    continuar = True
    tentativas_restantes = letras + 1
    tentativa = 0
    total = letras + 1
    while continuar == True:
        print('\033[1;35;40m{}\033[m'.format(f"Você tem {tentativas_restantes} tentativa(s)"))
        palpite = input("Qual é o seu palpite? ").lower()
        if palpite == 'desisto':
            break
        print(indica_posicao(sorteada, palpite))
        if palpite == sorteada:
            print('\033[1;32;40m{}\033[m' .format('Parabens!!! Você venceu!!!'))
            break
        if tentativas_restantes == 0:  
            print('\033[1;31;40m{}\033[m' .format('Poxa, você perdeu!!!'))
            break
        tentativas_restantes -= 1
        tentativa += 1
    print(informações)
    Repetir = input('\033[1;35;40m{}\033[m'.format('Você quer jogar novamente?(S/N) '))
    if Repetir == 'S':
        jogar = True
    if Repetir == 'N':
        jogar = False
        print('\033[1;35;40m{}\033[m'.format('Obrigado por jogar!!!'))
    
    
