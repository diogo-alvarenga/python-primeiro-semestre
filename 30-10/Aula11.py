#                                                   TUPLAS
#Nao pode alterar os valores da tupla

tupla = (1,3,5,7)
print(tupla)
print('tup[0]: ', tupla[0])
print('tup[1]: ', tupla[1])
print('tup[2]: ', tupla[2])
print('tup[3]: ', tupla[3])

tupla2 = (1,'John',True, -23.45)
print(tupla2)

#==================

tup3 = ("Apple","Pear","Plum","Apple")
for i in tup3: #Manda o i percorrer toda a tupla
    print(i)

#===================

tup3 = ("Apple","Pear","Plum","Apple")
if 'Plum' in tup3:
    print('Plum faz parte da tupla')

#===================
#NÃO pode fazer na tupla
#>Adicionar
#>Remover
#A tupla é IMUTAVEL
#===================

#                                                MATRIZES
#MATRIZ BIDIMENSIONAL
matriz = [[valores_linha1], [valores_linha2], [valores_linha3]]

#A primeira coluna será 9 e 13
#A segunda é 21 e 7
#A terceira é 17 e -5
#Cada colchete interno é uma LINHA da matriz, como por exemplo, a primeira linha é [9,21,17]
matriz_exemplo = [[9,21,17],[13,7,-5]]
print(matriz_exemplo)

matriz = []
quantidadeLinhas = 3
quantidadeColunas = 2

for i in range(quantidadeLinhas):
    linha = []
    for j in range(quantidadeColunas):
        elemento = int(input("Digite um número na posição [{}][{}]: ".format(i, j)))
        linha.append(elemento)
    matriz.append(linha)

print(matriz)

#======================

funcionarios = []
quantidade = 3
maior_salario = 0
maior_idade = 0

for i in range(quantidade):
    linha = [
            input("\nDigite o nome do funcionario: "),
            int(input("Digite a idade: ")),
            float(input("Digite o salario: "))
            ]
    funcionarios.append(linha)
for i in range(quantidade):
    if funcionarios[i][2]>funcionarios[maior_salario][2]:
        maior_salario = i
    if funcionarios[i][1]>funcionarios[maior_idade][1]:
        maior_idade=1
print("\n Funcionario com maior salario: ",funcionarios[maior_salario])
print("\n Funcionario mais velho: ", funcionarios[maior_idade])















