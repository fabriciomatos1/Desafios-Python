#Desafio 13
#Comandos principais
dicionario={}
def guardar():
    ano=0
    while (ano >= 0):
        ano=int(input("Digite sua data de nascimento: "))
        if (ano<=2020) and (ano>=0):
            if ano in dicionario:
                dicionario[ano]+=1
            else:
                dicionario[ano]=1
        elif ano > 2020:
            print("\033[31mAno inválido.\033[m")
            break
        else:
            print("\033[32mVolte sempre!\033[m")
            break
    return dicionario


#Exibição dos resultados
guardar()
for chave,valor in dicionario.items():
    print(f'\033[33m{valor}\033[m pessoa(s) nasceu/nasceram em \033[33m{chave}\033[m.')
