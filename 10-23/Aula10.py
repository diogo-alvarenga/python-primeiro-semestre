#lista - tupla - set- dicionario

#>>>>ORDENADOS
#Lista é uma coleçao de objetos que sao ordenados, indexados,
#permitem membros duplicados e mutaveis(podem ser alterados)

#Tupla - colecao de objetos que sao ordenados, indexados, permitem
#membros duplicados e sao IMUTAVEIS (nao podem ser alterados)

#>>>>NAO ORDENADOS
#Set - coleçao nao ordenada, mutavel, nao indexado e nao permite
#valores duplicados

#Dicinario - colecao nao ordenada, mutavel, indexada e que 
#permite varlores duplicados

#LISTA

nome_lista = [] #Posso declarar ja com valores, usando apenas a linha abaixo
nome_lista =[10,65,"asd",43,29,True]
print(nome_lista)
print(nome_lista[2])

a= 0
while True:
    print(nome_lista[a])
    a= a+1
    if a==6:
        break
print("Fim")

listaDeListas=[nome_lista,nome_lista] #uma lista pode conter listas
print(listaDeListas)

#=======================

list1 =['John', 'Paul','George','Ringo']
# [começa em : termina antes de]
print('list1[1]:',list1[1])
print('list1[-1]:',list1[-1])#vai mostrar o ultimo numero
print('list1[1:3]:', list1[1:3])#o segundo valor é ele - 1, entao mostra Paul e George
print('list1[:3]:',list1[:3])#até o 3
print('list1[1:]:',list1[1:])#a partir do 1

#=======================

vetor = [5,64,87,26,44,31]
for item in vetor:
    print(item)

for indice in range(6):
    print(vetor[indice])

for indice in range(len(vetor)):
    print(vetor[indice])

#=======================    

list1 = ['John', 'Paul', 'George','Ringo']
list1.append('Pete')
print(list1)

#=======================

alunos = []
nota = []
indice= 0
for indice in range(3):
    alunos.append (input("Nome "+str(indice+1)+ " "))
    nota.append(input("Nota do aluno "+str(indice+1)+" ")) 
    
print(alunos)
print(nota)

#=======================

#Os valores no inicio NÃO definem a quantidade de indexes, pode ser adicionado mais conforme o programa

a =["Aaa","bbb","ccc"]
a.append(234)
print(a)

#=======================

#Insert voce pode escolher o index
#append vai para o proximo indice

#remove remove a string da lista
outralista =['Gustavo', 'Walter','Jesse']
print(outralista)
outralista.remove('Walter')
print(outralista)

print(outralista[1])#o Jesse passou a ser o index 1, antes ele era o 2

#del deleta com index
del outralista[1]
print(outralista)

#=======================

list1  =[1,2,3]
list2 = [1,2,3]
list3 = list1 +list2
print(list3)

#=======================

num = [2,3,4,5]
q = num #quando eu faço isso ele fica atrelado, se eu mudar em q, mudará em num
q[2] = 9
p = num[:] #os dois pontos faz criar uma copia, se eu NÃo usar, uma fica atrelado ao outro
p[2] =6
print(p[:])
print(num[:])
print(q)

