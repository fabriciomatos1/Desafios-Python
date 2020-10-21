#Desafio 06
c=valor=num=0
while (num >= 0):
    num=int(input(f"Digite o valor {c+1} [OBS: inteiro e maior que zero / negativo encerra o programa]: "))
    if num >= 0:
        c+=1
        if (c == 1 or c+1) and num >= 0:
            valor+=num
med = valor/c
print(f"\033[32mFoi digitado {c} valores, com média: {med:.2f}\033[m")
