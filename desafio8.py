def fibonacci(x):
    antes = 0
    depois = 1
    soma = 0
    for c in range(0,num):
        print(antes,end=" -> ")
        soma = depois + antes
        antes = depois
        depois = soma


num=int(input("Enésimo número: "))
print(fibonacci(num))