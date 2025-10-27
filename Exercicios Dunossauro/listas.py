
#Exercicio 1

i = 0
vetor = []
for i in range(5):
    vetor.append(int(input()))
print(vetor)


#Exercicio 2


i = 0
vetor = []
for i in range(10):
    vetor.append(int(input()))
    
i2 = 9
while i2>=0:
    print(vetor[i2])
    i2 =i2 -1


#Exercicio 3


vetor = []
i = 0
for i in range(4):
    vetor.append(int(input()))
    
i2=0    
media = 0
for i2 in range(4):
    media = media + vetor[i2]
media = media /4
print(media)


#Exercicio 4


vetor = []
i =0
for i in range(10):
    vetor.append(input().lower())

i2=0
q = 0
for i2 in range(10):
    if vetor[i2] != "a" and vetor[i2]!= "e" and vetor[i2]!= "i" and vetor[i2] != "o" and vetor != "u":
        q = q+1   
    
print(q)


#Exercicio 5


vetor =[]
i = 0

for i in range(20):
    vetor.append(int(input()))

i2 =0
impar = []
par = []

for i2 in range(20):
    if vetor[i2] %2 ==0:
        par.append(vetor[i2])
    else:
        impar.append(vetor[i2])
        
print(vetor)
print(impar)
print(par)


#Exercicio 6


vetor =[]
i =0
n1 =0
n2=0
n3 =0
n4= 0
quantidadeAluno =0
for i in range(10):
    n1=float(input())
    n2=float(input())
    n3=float(input())
    n4=float(input())
    
    media = (n1+n2+n3+n4)/4
    if media >=7:
        vetor.append(media)
        quantidadeAluno = quantidadeAluno+1
        
print(vetor)
print(quantidadeAluno)


#Exercicio 7


vetor =[]

for _ in range(5):
    vetor.append(int(input()))

i=0
soma=0
for i in range(5):
    soma += vetor[i]
print(soma)

mult=1
for i in range(5):
    mult *= vetor[i]
print(mult)


#Exercicio 8


idade=[]
altura=[]

for i in range(5):
    idade.append(int(input("Digite sua idade: ")))
    altura.append(float(input("Digite sua altura: ")))

i=4

while i>=0:
    print(idade[i])
    print(altura[i])
    i= i -1


#Exercicio 9


vetor =[]

for i in range(10):
    vetor.append(int(input()))

quadrado =0
for i in range(10):
    quadrado = vetor[i]*vetor[i]
    print("O quadrado de ",vetor[i]," é ", quadrado)


#Exercicio 10


vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    vetor1.append(int(input()))

for i in range(10):
    vetor2.append(int(input()))
    
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(vetor3)


#Exercicio 11


vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
for i in range(10):
    vetor1.append(int(input()))

for i in range(10):
    vetor2.append(int(input()))
    
for i in range(10):
    vetor3.append(int(input()))
    
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(vetor4)


#Exercicio 12


idade=[]
altura=[]

for _ in range(30):
    idade.append(int(input()))
    altura.append(float(input()))
    
media = 0.0
for i in range(30):
    media = media + altura[i]
media = media/30

quantidade = 0
for i in range(30):
    if idade[i] >13 and altura[i] < media:
        quantidade = quantidade +1
print(quantidade)


#Exercicio 13


temperatura =[]
mes =["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
for i in range(12):
    temperatura.append(int(input()))


for i in range(12):
    print("A media da temperatura de ", mes[i], " foi ", temperatura[i])
print("==============================")


media = 0.0
for i in range(12):
    media = media+ temperatura[i]
media = media/12

print("A media de temperatura anual é ", media)
print("==============================")

for i in range(12):
    if temperatura[i]> media:
        print("No mes ", mes[i], " teve a media ", temperatura[i]," que supera a media anual")


#Exercicio 14


respostas = []
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
probabilidade = 0
for i in range(5):
    print(perguntas[i])
    respostas.append(input().lower().replace(" ",""))
    if respostas[i] == "sim":
        probabilidade +=1
if probabilidade ==2:
    print("Suspeito")
elif probabilidade>= 3 and probabilidade <= 4:
    print("Cumplice")
elif probabilidade>4:
    print("Assassino")
else:
    print("Inocente")


    