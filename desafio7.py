#Desafio 07
def fatorial(num, exib=False):
    global f
    f = 1
    for c in range(num, 0, -1):
        f*=c
        if exib:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
numero = int(input("Digite um número para calcular o fatorial: "))
mostrar = int(input("Modo de exibição? [nã\033[1;31m0\033[m/s\033[1;32m1\033[mm] "))
if mostrar == 0:
    fatorial(numero, exib=False)
    print(f'{numero}! = {f}', end='')
if mostrar == 1:
    fatorial(numero, exib=True)
    print(f'{f}', end='')