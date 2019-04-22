
"""
1) Dada uma matriz mxn, onde cada posiÃ§Ã£o contem um valor entre 0 e 255 (escala de cinzas),
implemente um algoritimo recursivo que receba 2 parÃ¢metros, um ponto (x,y), uma cor (0 a 255),
e um par de valores (a, b).
A partir do ponro inicial,
o algoritimo deve sibistituir todos os pontos adjascentes dentro da faixa
de valores [a .. b], pela cor


ta entre a e b
ve todos na avolta 
criterio de parada 


recursão
pontos adjascentes
"""
from colorama import init
from termcolor import colored
from random import randint

init()
m = 10
n = 10

matriz = [[] , []]

maior_linha = m
maior_coluna = n

cont1 = 0
cont2 = 0
while cont1 < maior_linha:
    while cont2 < maior_coluna:
        matriz[0].append(randint(0, 255))
        cont2 += 1
    matriz[1].append(randint(0, 255))
    cont1 += 1
x_y = (randint(0, (maior_linha-1)), randint(0, (maior_coluna-1)))

print(f"Ponto inicial: {x_y}")

cor = randint(0, 255)

print(f"Cor: {cor}")

par_valores  = (randint(0, maior_linha), randint(0, maior_coluna))

print(f"A, B: {par_valores}")

def pintar(x_y, cor, par_valores):


    for cont_linha, linha in enumerate(matriz[0]):
        for cont_coluna, coluna in enumerate(matriz[1]):
            if(x_y[0] == cont_linha and x_y[1] == cont_coluna):
               print(colored(f"[{cor}]", "grey", "on_white"), end=" ") 
            if((x_y[0]-1) == cont_linha  and x_y[1] == cont_coluna):
               print(colored(f"[{cor}]", "grey", "on_white"), end=" ")
            if((x_y[0]+1) == cont_linha and  x_y[1] == cont_coluna):
                print(colored(f"[{cor}]", "grey", "on_white"), end=" ")
            if(x_y[0] == cont_linha and  (x_y[1]-1) == cont_coluna):
                print(colored(f"[{cor}]", "grey", "on_white"), end=" ")
            if(x_y[0] == cont_linha and  (x_y[1]+1) == cont_coluna):
                print(colored(f"[{cor}]", "grey", "on_white"), end=" ")
            else:
                print(f"[{cont_linha}, {cont_coluna}]", end=" ") 
            
        print()

pintar(x_y, cor, par_valores) 
