#Desafio 15
def criarlinha():
        print("~"*30)


ctn=''
while ctn != 0:
    nome=str(input("Digite o seu nome: "))
    precos=[]
    for i in range(0,1):
        valor,valor1,valor2=["A ="],["B ="],["C ="]
        for j in range(0,1):
            valor.append("R$ 2.98"),valor1.append("R$ 3.90"),valor2.append("R$ 1.99")
        precos.append(valor),precos.append(valor1),precos.append(valor2)
    matriz = []
    criarlinha()
    for i in range(0,1):
        linha,linha1,linha2=["A ="],["B ="],["C ="]
        for j in range(0,1):
            linha.append(int(input("Digite quantos gramas de A: ")))
            tot= (linha[1]*0.01)*2.98
            linha.append(tot)
            linha1.append(int(input("Digite quantos gramas de B: ")))
            tot1=(linha1[1]*0.01)*3.90
            linha1.append(tot1)
            linha2.append(int(input("Digite quantos gramas de C: ")))
            tot2=(linha2[1]*0.01)*1.99
            linha2.append(tot2)
        matriz.append(linha),matriz.append(linha1),matriz.append(linha2)
        linha[1],linha1[1],linha2[1]=f"{linha[1]}g",f"{linha1[1]}g",f"{linha2[1]}g"
        linha[2],linha1[2],linha2[2]=f"R$ {linha[2]:.2f}",f"R$ {linha1[2]:.2f}",f"R$ {linha2[2]:.2f}"
    criarlinha()
    print("Tabela de preços (100g):")
    for y in range(0,3):
        precos[y]=str(precos[y]).replace("'","").replace("[","").replace("]","").replace(",","")
        print(precos[y])
    criarlinha()
    print(f"Pagamento total de {nome}:")
    for x in range(0,3):
        matriz[x]=str(matriz[x]).replace("'","").replace("[","").replace("]","").replace(",","")
        print(matriz[x])
    total=tot+tot1+tot2
    print(f"Valor total: R${total:.2f}")
    criarlinha()
    ctn=int(input("Outra compra? [S1m/Nã0] "))
    while ctn != 0 and ctn != 1:
        print("Valor errado, digite novamente...")
        ctn=int(input("Outra compra? [S1m/Nã0] "))
print("Volte sempre!")
