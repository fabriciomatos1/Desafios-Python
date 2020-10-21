#Desafio 12
from time import sleep

#Decorações
def linha1(x):
    print("\033[1;34m<\033[m"*len(x))
    print(f"\033[1;32m{x}\033[m")
    print("\033[1;34m>\033[m"*len(x))
    return x

#Chamadas e título
linha1("Mestre da matemática")
lista1= []
lista2= []
soma= []

#Comandos principais
for i in range(1,11):
    x=int(input(f"Digite o valor {i}: [Deve ser inteiro/\033[32mlista 1\033[m] "))
    lista1.append(x)
for c in range(1,11):
    y=int(input(f"Digite o valor {c}: [Deve ser inteiro/\033[34mlista 2\033[m] "))
    lista2.append(y)

#Operação de soma
def somar(l1,l2):
    pos0=0
    pos1=0
    while (pos0 < len(l1)):
        soma.append(l1[pos0]+l2[pos1])
        pos0+=1
        pos1+=1
    return soma


#Exibição dos resultados
somar(lista1,lista2)
print("\033[34mA soma de:\033[m")
sleep(1)
for a in lista1:
    print(a, end=' ')
print("\033[34m\ncom:\033[m")
sleep(1)
for b in lista2:
    print(b,end=' ')
print("\033[34m\ndeu:\033[m")
sleep(1)
for c in soma:
    print(c, end=' ')
