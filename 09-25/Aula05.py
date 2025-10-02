


num = (input('Digite um numero: '))
print(num)
print(type(num))

num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o primeiro numero: ")
soma = num1+num2
print(soma)


taxa = float(input("Digite a taxa de conversao: "))
print(taxa)
print(type(taxa))


situacao = Verdadeiro
print(situacao)
print(type(situacao))



situacao = float
print(situacao)
print(type(situacao))

situacao = ''
print(situacao)
print(type(situacao))


situacao = ''
print(situacao)
print(type(situacao))


print('Ela disse "Ola" para todos')

nome = "Carlos Henrique Bueno Carlos Henrique Bueno Carlos Henrique Bueno"

palavra = nome.count("Henrique")

print(palavra)


curso = 'Python'
ano = 2019
valor = 200

print('Curso:' , curso , 'Custa: R$' , valor, 'em', ano)

nome = 'Carlos'
print (f"Meu nome é {nome}")


nome = 25
print(int("Meu nome é {nome}"))



curso = 'Python'
ano = 2015
valor = 1500.00

mensagem = 'Curso: ' + curso + ' Custa: R$  ' + str(valor) + ' em ' + str(ano)

print(mensagem)


print(type(mensagem))




codigo = 135
nome = 'Maria da Silva'
ativo = True
salario = 2346.16


print("Código: %d" % codigo) # %d (Inteiro): Insere um valor inteiro
print("Nome: %s " % nome) # %s (String): Insere uma representação de string do valor
print("Ativo: %r" %ativo) # %r (Representação "raw"): Insere a representação "raw" de um objeto, que geralmente é a que você usaria no próprio código Python para recriar o objeto, e é útil para depuração.
print("Salário: %.2f " % salario) # %.2f (Ponto Flutuante com duas casas decimais): Insere um número de ponto flutuante (float) arredondado para duas casas decimais.
# print("O valor é %.2f" % meu_numero) formata meu_numero para exibir duas casas decimais. 




curso = 'Desenvolvimento de Software Multiplataforma'
inicio = 2025
duracao = 3

fim = int(inicio) + duracao

print('Nome do curso:', curso,'\nInicio em:',inicio,'\tTérmino em:',fim)


A = 10 + 2
B = A - 5
C = 587 * A + B
valor = 5.5 / 2
D = 34 % 3 
E = 34 / 3
F = 34 // 3
G = 6**4


print('10+2 = ' , A)
print('A - 5 = ', B)
print('587 * A + B = ', C)
print('5.5 / 2', valor)
print('34 % 3 = ' , D )
print('34 / 3 = ' , E)
print('34 // 3 = ', F)
print('7 ** 4 = ' , G)


# O valor da potenciação 
num1 = math.pow(2,3)
print("O valor da potenciação é %.0f" %num1)

#  O valor da raiz quadrada
num1 = math.cbrt(8)
print("O valor da raiz quadrada é %.0f" %num1)


# O valor da hipotenusa
num2 = math.hypot(3,4)
print("O valor da hipotenusa é %.0f" % num2)


# O valor do número PI
num3 = math.pi
print("O valor do número PI é %.2f" % num3)


# Arredonda o valor para cima
num4 = math.ceil(2.6)
print("O valor do número é" , num4)










import math
num = math.sqrt(8)

#O valor da raiz quadrada
print("O valor da raiz quadrada:\n%.0f" % num)

