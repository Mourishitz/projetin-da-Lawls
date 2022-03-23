# Questão 1

salario = int(input("Digite o seu salário: "))
gasto = int(input("Digite seus gastos: "))
total = (salario - gasto)
if gasto > salario:
    print("Seus gastos estão maiores do que o seu salário")
    print("Você terá despesas de: "+str(total))
else:
    print("Seus gastos estão dentro do seu orçamento")
    print("Você ficará com "+str(total)+" após pagar suas contas")

# Questão 2

X = int(input("Digite um número: "))
if (X % 5 == 0):
    print("O número "+str(X)+" é divisível por 5!")
else:
    print("O número "+str(X)+" não é divisível por 5")

# Questão 3

Y = int(input("Digite um número: "))
if (Y % 2 == 0):
    print("O número "+str(Y)+" é divisível por 2!")
else:
    print("O número "+str(Y)+" não é divisível por 2")

# Questão 4

vX = int(input("Digite um valor para X: "))
if vX < 0:
    print("O número selecionado é menor do que 0")
else:
    a = int(input("Digite um valor para 'a': "))
    b = int(input("Digite um valor para 'b': "))
    c = int(input("Digite um valor para 'c': "))
    if vX % 2 == 0:
        soma = (a+b+c)
        media = soma/3
        print("A média aritmética de a, b e c é de: "+str(soma))
    else:
        if vX > 10:
            a1 = a*2
            b1 = b*3
            c1 = c*4
            peso_1 = a1+b1+c1
            total = peso_1/9
            print("A media ponderada de a, b e c é de: "+str(total))

# Questão 5

x = int(input("Digite um número: "))
y = int(input("Digite um segundo número: "))
z = int(input("Digite um  terceiro número: "))
numeros = [x,y,z]
numeros.sort()
print(numeros)
