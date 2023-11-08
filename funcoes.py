import random

def filtra(list,num):
    lista = []
    for i in range(len(list)):
      if len(list[i]) == num:
         menor = list[i].lower()
         if menor not in lista:
            lista.append(menor)
    return lista
def indica_posicao(sorteada,espec):
    lista = []
    if len(sorteada)!= len(espec):
        return lista
    else:  
        for i in range(len(sorteada)):
            menor_esp = espec.lower()
            menor_sort = sorteada.lower()
            if menor_sort[i] == menor_esp[i]:
                lista.append(0)
            elif menor_esp[i] in menor_sort :
                lista.append(1)
            else: 
                lista.append(2)
    return lista

def inicializa(list):
    especuladas = []
    n = len(list[0])
    tentativas = n+1
    sorteada = random.choice(list)
    d = {'n':n ,'sorteada':sorteada, 'especuladas': especuladas, 'tentativas' : tentativas }
    return d