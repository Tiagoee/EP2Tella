import random

def filtra(list,num):
    lista = []
    for i in range(len(list)):
      if len(list[i]) == num:
         menor = list[i].lower()
         if menor not in lista:
            lista.append(menor)
    return lista


def indica_posicao(sorteada, espec):
    lista = []
    if len(sorteada) != len(espec):
        print('\033[0;31;40m{}\033[m' .format('A quantidade de letras está errada!!!'))
        return lista
    else:
        for i in range(len(sorteada)):
            menor_esp = espec.lower()
            menor_sort = sorteada.lower()
            if menor_sort[i] == menor_esp[i]:
                lista.append('\033[1;36;40m{}\033[m'.format(menor_esp[i]))
            elif menor_esp[i] in menor_sort:
                lista.append('\033[1;33;40m{}\033[m'.format(menor_esp[i]))
            else:
                lista.append('\033[1;37;40m{}\033[m'.format(menor_esp[i]))
    return ' '.join(lista)


def inicializa(list):
    especuladas = []
    n = len(list[0])
    tentativas = n+1
    sorteada = random.choice(list)
    d = {'n':n ,'sorteada':sorteada, 'especuladas': especuladas, 'tentativas' : tentativas }
    return d