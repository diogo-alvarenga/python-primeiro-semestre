
a= 15
b= 32

print(a, ' ==', b, ':' , a == b)
print(a, ' ==', b, ':' ,not( a == b))
print(a, " != ", b ," : ", a != b)
print(a, " > ", b ," : ", a > b)
print(a, " < ", b ," : ", a < b)
print(a, " >= ", b ," : ", a >= b)
print(a, " <= ", b ," : ", a <= b)


#=============


A= 15
B = 90
C = 29

print("A == B and B > C : ", A== B and B> C)
print("A != B or B < C : ", A!= B or B< C)
print("not (A > B) : ", not(A>B))



#============


idade = 18
if idade >= 18:
    print('Voce ja pode votar!')


#==========


idade = 10
if idade>= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


#=========

"""
 idade = 18
 if idade >= 18:
         print('Parabens!')
         print('Voce ja pode votar!')
"""

#=========


a= input("Digite um numero a: ")
b= input("Digite um numero b: ")

if a > b:
    c = a
    a = b
    b = c

else:
    print('a < b')
print('a = ', a)
print('b = ', b)


#============

print("O numero a deve ser maior que o numero b para cair no if")
a = int(input("Digite um numero a: "))
b = int(input("Digite um numero b: "))

if a > b:
    c = a
    a = b
    b = c

else:
    print('a < b')
print('a = ', a)
print('b = ', b)


#=============


A= float(input("Informe a primeira nota: "))
B = float(input("Informe a segunda nota: "))

media = (A+B)/2

if media>= 7.0:
    print("Media: %.1f = APROVADO " %media)
else:
    print("Media: %.1f = REPROVADO "%media)


#==========


snowing = False
temp = -1
if temp < 0:
    print("Its freezing")
    if snowing:
        print("Put on boots")
    print("Time for hot chocolate")
print("bye")


#==========


sexo = input("Digite M para masculino ou F para feminino")

if sexo == "M":
    print("Sexo masculino")
elif sexo =="F":
    print("Sexo feminino")
else:
    print("Sexo indefinido")


