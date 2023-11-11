import funcoes
import Regras
from Palavras import PALAVRAS
num=5



lista= funcoes.filtra(PALAVRAS,num)
continuar=True
tentativas=1
palavras_usadas=[]
desistir= ['desisto','cansei','jogo chato','para','parar','parei']
while continuar==True:
    chute=''
    palavra=[]
    if tentativas>6:
        continuar=False
        print('acabaram as tentativas')
        break
    chute=input('chute: ')
    
    if chute in desistir:
        print('Que pena, tente denovo se quiser...')
        continuar=False
        break
    if len(chute)<5:
        print('So são aceitas palavras com 5 letras')
    if chute in palavras_usadas:
        print('Essa palavra ja foi usada')

    palavras_usadas.append(chute)
    tentativas = tentativas+1
    palavra.extend(chute)
    print (palavra)



