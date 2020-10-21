#Desafio 16
#Barcos leva dígito '1' e bombas dígito '0';
#Apenas 1 barco por linha(1 recebe '=', 11 recebe '-='), em um tabuleiro 10x5;
#Para tornar o jogo menos cansativo os barcos e bombas são colocados automaticamente e o jogador2 é o computador, que gera as posições dele automaticamente, mas isso pode ser mudado;
#Caso apareça +30 pontos de primeira, você acertou um barco único ('1'/'=');
#Caso apareça +70 de primeira, aquela linha possui mais uma parte da embarcação...(A outra parte fica do lado esquerdo ou direito...);
#O jogo pode ter 15 ou mais barcos... Número recomendado de tentativas.
from random import randint
from time import sleep
print("/"*25)
print('\033[34mB A T A L H A  N A V A L\033[m')
print("/"*25)
def marcar():
    global mapa1
    global linha
    mapa1=[]
    for i in range(10):
        linha=[]
        for j in range(5):
            linha.append(randint(0,0))
        linha[randint(0,4)]=1
        if linha[0] == 1:
            linha[1]= 1
        elif linha[1] == 1:
            linha[2]== 1
        elif linha[2] == 1:
            linha[3]=1
        elif linha[3] == 1:
            linha[4]=1
        elif linha[4]==1:
            linha[3]=1
        mapa1.append(linha)
    global mapa2
    global linha2
    mapa2=[]
    for l in range(10):
        linha2=[]
        for c in range(5):
            linha2.append(randint(0,0))
        linha2[randint(0,4)]=1
        if linha2[0] == 1:
            linha2[1]= 1
        elif linha2[1] == 1:
            linha2[2]== 1
        elif linha2[2] == 1:
            linha2[3]=1
        elif linha2[3] == 1:
            linha2[4]=1
        elif linha2[4]==1:
            linha2[3]=1
        mapa2.append(linha2)
def lermapas():
    marcar()
    global pontuar
    global jogador1
    global l1
    global c1
    pontuar=0
    jogador1=str(input("Jogador 1: "))
    tent=int(input("Quantas tentativas? "))
    for y in range(tent):
        l1=int(input(f'{jogador1}, escolha a linha [0 até 9]: ')) 
        c1=int(input(f'{jogador1}, escolha a coluna [0 até 4]: '))
        if mapa2[l1].count(1)==2:
            if mapa2[l1].count(1)== 2:
                if mapa2[l1][c1] == 1:
                    print(f"\033[32mVocê acertou parte do barco! +70\033[m","[",mapa2[l1][c1],"]")
                    pontuar+=70
                    mapa2[l1][c1]='-'
                elif mapa2[l1][c1] == 0:
                    print("\033[31mVocê errou... +0\033[m","[",mapa2[l1][c1],"]")
                    pontuar+=0
        elif mapa2[l1].count(1)==1:
            if mapa2[l1][c1] == 1:
                print(f"\033[32mVocê acertou o resto do barco! +30\033[m","[",mapa2[l1][c1],"]")
                pontuar+=30
                mapa2[l1][c1]='='
            if mapa2[l1][c1] == '-':
                print("\033[31mVocê já acertou essa posição... +0\033[m")
                pontuar+=0
            elif mapa2[l1][c1]==0:
                print("\033[31mVocê errou... +0\033[m","[",mapa2[l1][c1],"]")
                pontuar+=0
        elif mapa2[l1].count(1)==0:
            if mapa2[l1][c1] == '-':
                print("\033[31mVocê já acertou essa posição... +0\033[m")
                pontuar+=0
            elif mapa2[l1][c1] == '=':
                print("\033[31mVocê já acertou essa posição... +0\033[m")
                pontuar+=0
    sleep(1)
    print("Gabarito:")
    for y in range(10):
            mapa2[y]=str(mapa2[y]).replace("'","").replace("[","").replace("]","").replace(",","")
            print(mapa2[y])
    sleep(1)
    global pontuar2
    global jogador2
    global c2
    global l2
    pontuar2=0
    jogador2="Computador"
    for z in range(tent):
        l2=randint(0,9) 
        print(f'Computador escolheu a linha: {l2}')
        sleep(1)
        c2=randint(0,4)
        print(f'Computador escolheu a coluna: {c2}')
        sleep(1)
        if mapa1[l2].count(1)==2:
            if mapa1[l2].count(1)== 2:
                if mapa1[l2][c2] == 1:
                    print(f"\033[32mComputador acertou parte do barco! +70\033[m","[",mapa1[l2][c2],"]")
                    pontuar2+=70
                    mapa1[l2][c2]='-'
                elif mapa1[l2][c2] == 0:
                    print("\033[31mComputador errou... +0\033[m","[",mapa1[l2][c2],"]")
                    pontuar2+=0
        elif mapa1[l2].count(1)==1:
            if mapa1[l2][c2] == 1:
                print(f"\033[32mComputador acertou o resto do barco! +30\033[m","[",mapa1[l2][c2],"]")
                pontuar2+=30
                mapa1[l2][c2]='='
            elif mapa1[l2][c2]==0:
                print("\033[31mComputador errou... +0\033[m","[",mapa1[l2][c2],"]")
                pontuar2+=0
        elif mapa1[l2][c2] == '-':
            print("\033[31mComputador já acertou essa posição... +0\033[m")
            pontuar2+=0
        elif mapa1[l2][c2] == '=':
            print("\033[31mComputador já acertou essa posição... +0\033[m")
            pontuar2+=0
    sleep(1)
    print("Gabarito:")
    for z in range(10):
        mapa1[z]=str(mapa1[z]).replace("'","").replace("[","").replace("]","").replace(",","")
        print(mapa1[z])


def pontos():
    lermapas()
    sleep(1)
    print(f"{jogador1} fez {pontuar} pontos!")
    print(f"{jogador2} fez {pontuar2} pontos!")
    if pontuar> pontuar2:
        print(f'{jogador1} venceu!')
    elif pontuar2>pontuar:
        print(f'{jogador2} venceu!')
    else:
        print(f"Empate entre {jogador1} e {jogador2}!")


pontos()
