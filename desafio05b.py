#Desafio 05 while
c=acumula=0
while (c != 20):
    idd=int(input(f"Digite sua idade, usuário {c+1}: "))
    c+=1
    if c == 1 or c+1:
        acumula+=idd
med = acumula/c
print(f"\033[32mO resultado das {c} idades deu: {med:.2f}\033[m")
