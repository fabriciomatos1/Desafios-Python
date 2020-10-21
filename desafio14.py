#Desafio 14 Jogos Vorazes
#Listas,dicionário e tupla
form={}
nomes=[]
idades=[]
telefones=[]
nmpais=[]
nmmaes=[]
volt=[]
permitir=(12,13,14,15,16,17,18)
#Funções criadas
def add(x,y):
    x.append(str(input(f"Digite para categoria {y}: ")))
    form[y]=x


def add2(a,b,c):
    a.append(b)
    form[c]=a


def cond(e,f):
    if ((e > len(f) or e < 0) or ((e == 0 and e == len(f))or e == 1 and e == len(f))):
        print("\033[31mFora do intervalo.\033[m")
    else:
        del f[e]


def cond2(g,h):
    if ((g > len(h) or g < 0) or ((g == 0 and g == len(h))or g == 1 and g == len(h))):
        print("\033[31mFora do intervalo.\033[m")
    else:
        novo=str(input(f"Digite o valor que substitui {h}: "))
        h[g]=novo


def listas(x):
    for c in x:
        print(f'\033[32m{c}\033[m')
    return c


def criarlinha():
    print('='*30)


def criarlinha2():
    print("\033[33m♨\033[m"*45)


def exib(n,m):
    if n == []:
        print("",end="")
    else:
        if k == m:
            listas(n) 
#título
criarlinha2()
print("J O G O S  V O R A Z E S - O  R E T O R N O")
criarlinha2()
#Comandos principais  
opc=0
while (opc != 6):
    criarlinha()
    print(''' [1] Adicionar cadastro \n [2] Remover informações \n [3] Alterar informações \n [4] Mostrar informações \n [5] Adicionar informações \n [6] Sair''')
    criarlinha()
    opc=int(input("Digite a opção: "))
    if (opc >= 1) and (opc <= 6):
        #Inserção de informações
        if opc == 1:
            x=int(input("Digite a sua idade: "))
            if x in permitir:
                print("\033[32mPermitido.\033[m")
                add(nomes,'Nomes')
                add2(idades,x,'Idades')
                add(telefones,'Telefones')
                add(nmpais,'Pais')
                add(nmmaes,'Mães')
                v=str(input("Voluntário? [True/False] "))
                while v not in "True" and v not in "False":
                    print("\033[31mValor inválido!\033[m")
                    v=str(input("Voluntário? [True/False] "))
                if (v == "True") or (v == "False"):
                    add2(volt,v,'Voluntários')
            else:
                print("\033[31mIdade não permitida!\033[m")
                break
        #Remoção de informações
        if opc == 2:
            itm=int(input("Digite a posição do dado: [1(Nome) 2(Idade) 3(Telefone) 4(Nome do pai) 5(Nome da mãe) 6(Voluntário)] "))
            rmv=int(input("Digite a posição da informação que deseja remover: "))
            if itm == 1:
                cond(rmv, nomes)
            elif itm == 2:
                cond(rmv,idades)
            elif itm == 3:
                cond(rmv,telefones)
            elif itm == 4:
                cond(rmv,nmpais)
            elif itm == 5:
                cond(rmv,nmmaes)
            elif itm == 6:
                cond(rmv,volt)
            else:
                print("\033[31mValor fora do intervalo!\033[m")
        #Alteração de informações
        if opc == 3:
            pos=int(input("Digite a posição do dado: [1(Nome) 2(Idade) 3(Telefone) 4(Nome do pai) 5(Nome da mãe) 6(Voluntário)] "))
            alt=int(input("Digite a posição da informação que deseja alterar: "))
            if pos == 1:
                cond2(alt,nomes)
            elif pos == 2:
                if ((alt > len(idades) or alt < 0) or ((alt == 0 and alt == len(idades))or alt == 1 and alt == len(idades))):
                    print("\033[31mIdade fora do intervalo.\033[m")
                    break
                else:
                    novoidd=int(input("Digite a nova idade: "))
                    idades[alt]=novoidd
                if novoidd not in permitir:
                    print('\033[31mIdade não permitida!\033[m')
                    idades[alt]="Idade corrompida!"
            elif pos == 3:
                cond2(alt,telefones)
            elif pos == 4:
                cond2(alt,nmpais)
            elif pos == 5:
                cond2(alt,nmmaes)
            elif pos == 6:
                if ((alt > len(volt) or alt < 0) or ((alt == 0 and alt == len(volt))or alt == 1 and alt == len(volt))):
                    print("\033[31mVoluntário fora do intervalo.\033[m")
                novovt=str(input("Voluntário? [True/False]"))
                while novovt not in "True" and novovt not in "False":
                  print("\033[31mValor inválido!\033[m")
                  novovt=str(input("Voluntário? [True/False] "))
                if (novovt == "True") or (novovt == "False"):
                  volt[alt]=novovt
            else:
                print("\033[31mFora do intervalo.\033[m")
        #Exibição dos conteúdos
        if opc == 4:
            if form == {}:
                print("\033[31mFormulário vazio!\033[m")
            for k in form.keys():
                print(f'\033[31m{k}\033[m')
                exib(nomes,'Nomes')
                exib(idades,'Idades')
                exib(telefones,'Telefones')
                exib(nmpais,'Pais')
                exib(nmmaes,'Mães')
                exib(volt,'Voluntários')
        #Adição de valores individuais
        if opc == 5:
            opc2=int(input("Digite a posição do dado: [1(Nome) 2(Idade) 3(Telefone) 4(Nome do pai) 5(Nome da mãe) 6(Voluntário)] "))
            if opc2 == 1:
                add(nomes,'Nomes')
            elif opc2 == 2:
                idade1=int(input("Digite a sua idade: "))
                if idade1 in permitir:
                    add2(idades,idade1,'Idades')
                else:
                    print("\033[31mIdade inválida!\033[m")
            elif opc2 == 3:
                add(telefones,'Telefones')
            elif opc2 == 4:
                add(nmpais,'Pais')
            elif opc2 == 5:
                add(nmmaes,'Mães')
            elif opc2 == 6:
                volt2=str(input("Voluntário? [True/False] "))
                while volt2 not in "True" and volt2 not in "False":
                    print("\033[31mValor inválido!\033[m")
                    volt2=str(input("Voluntário? [True/False] "))
                if (volt2 == "True") or (volt2 == "False"):
                    add2(volt,volt2,'Voluntários')
    else:
        print("\033[31mInválido!\033[m")
#Valor 6 digitado
print("\033[34mVolte sempre!\033[m")
