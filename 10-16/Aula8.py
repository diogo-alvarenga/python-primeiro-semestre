
for n in range(10):
    print(n)


#===

#A variavel n começa no valor 5
for n in range(5,16):
    print(n)

#===

#O terceiro argumento, o -1, faz ele contar de forma decrescente (começa no 10 e termina no 1 (numero antes do 0))
for n in range(10,0,-1):
    print(n)

#===

#o terceiro argumento faz ele pular de 2 em 2
for i in range(0,10,2):
    print(i)
print('Feito!')

#===

# _ é uma variavel anonima 
#variaveis anonimas nao serao usadas, é apenas um espaço de memoria
for _ in range(0,10,2):
    print('Hello')
print('Feito')

#===

numero = int(input("Digite um numero para a tabuada: "))
for t in range(0,11):
    print(numero,'x',t,'=',numero*t)

#===

x= 1
while x <= 15:
    print(x)
    x = x+1

#===

quantidade = 0
soma = 0
media = 0

valor = float(input("Digite um valor: "))

while valor>0.0:
    soma = soma+valor
    quantidade = quantidade +1

    valor = float(input("Digite um valor: "))
media = soma /quantidade

print("\nTotol da soma =", soma)
print("\nQuantidade de valores: ", quantidade)
print("\nMedia total dos valores: ", media)

#===

numero = int(input("Digite um numero inteiro "))
for i in range(0,10):
    if i == numero:
        break
    print(i)
print("Feito")

#===

numero = int(input("Digite um numero inteiro"))
i=0
while i< 10:
    if i== numero:
        break
    print(i)
    i= i+1
print("Feito")

#===

for i in range(0,10):
    print(i)
    if i % 2 ==1:
        continue #pula o resto do codigo
    print('O numero acima é par')
print('Done')

#===

for i in range(1,11):
    if 1%2==0:
        print(i)
        if i ==6:
            break
else:
    print('Estes sao os pares de 1 a 10')

#===

x= 1
while x<= 10:
    if x% 2 ==0:
        print(x)
    x = x+1
else:
    print("Todos os numeros de 1 a 10 forma exibidos")

#===

import random 
print(random.randrange(100))
print(random.randrange(50,100))
print(random.choice([20,5,10,15,54]))
print(random.random())
print(random.randint(10,60))