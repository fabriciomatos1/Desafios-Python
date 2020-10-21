#Desafio 11
from time import sleep

#Decoração de títulos
def linha1(x):
    print("\033[1;33m>\033[m"*len(x))
    print(f"\033[1;36m{x}\033[m")
    print("\033[1;33m<\033[m"*len(x))
    return x


def linha2(c):
    print("\033[1;31m-\033[m"*len(c))
    print(c)
    print("\033[1;31m-\033[m"*len(c))
    return c


def linha3():
    print("\033[1;32m==\033[m"*15)


#Chamadas e título
filmes=[]
linha1("Catálogo de filmes")
x=()

#Comandos principais
while True:
    linha2('''[1] Inserir um filme no catálogo;
[2] Atualizar um filme do catálogo;
[3] Remover um filme do catálogo;''')
    x=int(input("Digite a operação que deseja realizar: "))
    if x == 1:
        y= str(input("Digite o nome do filme: "))
        filmes.append(y)
    if x == 2:
        pos = int(input("Digite a posição do filme: "))
        while ((pos > len(filmes) or pos < 0) or ((pos == 0 and pos == len(filmes))or pos == 1 and pos == len(filmes))):
            print("Fora do intervalo...")
            pos = int(input("Digite a posição do filme: "))
        filmes[pos] = str(input("Digite o novo filme: "))
    if x == 3:
        a=str(input("Digite o nome do filme que será removido: "))
        if a not in filmes:
            print("Filme não existe!")
        else:
            filmes.remove(a)

#Inserção de entrada fora do intervalo
    while (x > 3 or x < 1):
        print("\033[1;31mOpção inválida! Digite novamente:\033[m")
        linha2('''[1] Inserir um filme no catálogo;
[2] Atualizar um filme do catálogo;
[3] Remover um filme do catálogo;''')
        x = int(input("Digite a operação que deseja realizar:"))
        if x == 1:
            y = str(input("Digite o nome do filme: "))
            filmes.append(y)
        if x == 2:
            pos = int(input("Digite a posição do filme: "))
            while ((pos > len(filmes) or pos < 0) or ((pos == 0 and pos == len(filmes)) or pos == 1 and pos == len(filmes))):
                print("Fora do intervalo...")
                pos = int(input("Digite a posição do filme: "))
            filmes[pos] = str(input("Digite o novo filme: "))
        if x == 3:
            a = str(input("Digite o nome do filme que será removido: "))
            if a not in filmes:
                print("Filme não existe!")
            else:
                filmes.remove(a)

#Lista de filmes
    linha3()
    for i in filmes:
        print(i)
    linha3()

#Confirmar continuação
    b=int(input("Quer continuar? [S\033[32m1\033[mM/NA\033[31m0\033[m] "))
    if b > 1:
        ("Dígito incorreto, digite novamente: ")
        b = int(input("Quer continuar? [S\033[32m1\033[mM/NA\033[31m0\033[m] "))
    if b == 0:
        sleep(1)
        print("\033[34mVolte sempre!\033[m")
        break
