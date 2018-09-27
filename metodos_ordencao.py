"""

Métodos de Ordenação


Tabela que mostra o resultados de 4 métodos de ordenação

MergeSort | QuickSort | SelectionSort | NativeSort

"""

import time
from random import shuffle

# Métodos de Ordenação

# MergeSort
def merge( e, d ):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append( e[i] )
            i += 1
        else:
            r.append( d[j] )
            j += 1
    r += e[i:]
    r += d[j:]
    return r
#
def mergesort( v ):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort( v[:m] )
        d = mergesort( v[m:] )
        return merge( e , d )

# QuickSort
def quicksort( v ):
    if len(v) <= 1:
        return v

    pivô = v[0]
    iguais = [x for x in v if x == pivô ]
    menores = [x for x in v if x < pivô ]
    maiores = [x for x in v if x > pivô ]
    
    return quicksort( menores ) + iguais + quicksort( maiores )

# SelectionSort
def seleção( v ):
    resp = []
    while len(v) > 0:
        m = min(v)
        resp.append(m)
        v.remove(m)
    return resp


def separador():
    print( '{:-^53}'.format('') )

def iniciar():
    print( '        |  MergeSort  QuickSort  Selection  Native |' )

def printresultado( lista , tempoMerge , tempoQuick , tempoSelection , tempoNative ):
    print( '{!s}{}|{: ^5}{:.2f}{: ^7}{:.2f}{: ^6}{:.2f}{}{:.2f}{: ^2}|'.format( len(lista) , '    ' if len(lista) < 10000 else '   ' , '', tempoMerge , '', tempoQuick , '', tempoSelection , '      ' if tempoSelection < 10 else '     ', tempoNative , '') )


separador()
print( '{:^53}'.format('tempo(s)') )
separador()
iniciar()

inicioloop = time.time() # Controlar o tempo do loop inteiro
lista = list( range(2000) ) # Lista Inicial

# É necessário rodar por aproximadamente MEIO minuto
while time.time() - inicioloop < 30:

    copia = list( lista ) # Cria uma cópia da lista
    shuffle( copia ) # Embaralha os itens dentro da list

    # Tempo para cada método de ordenação
    # MergeSort, QuickSort, Selection, Native
    tempo = [ 0 , 1 , 2 , 3]
    
    for m in range( 4 ):
        inicio = time.time()
        
        if m == 0:
            mergesort( copia )
        elif m == 1:
            quicksort( copia )
        elif m == 2:
            seleção( copia )
        else:
            copia.sort()
        
        tempo[m] = time.time() - inicio

    # Mostra o resultado formatado corretamente
    printresultado( lista , tempo[0] , tempo[1] , tempo[2] , tempo[3] )

    # Aumenta a lista em 2000
    lista = list( range( len(lista) + 2000 ) )

separador()
