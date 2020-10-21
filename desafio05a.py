#Desafio 05 for
c=acumula=0
for c in range(0,20):
    idd=int(input(f"Digite a sua idade, usuário {c+1}: "))
    c+=1
    if c == 1 or c+1:
       acumula += idd
med = acumula/c
print(f"\033[32mA média das {c} idades deu: {med:.2f}\033[m")
