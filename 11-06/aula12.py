
def print_msg():
    print("Hello World!")

print_msg()


#======================


def inverte(a,b):
    return b,a 

a = 2
b = 3

x,y = inverte(a,b)
print(x,',',y)


#=======================


def digitar():
    return "Digite um numero:"

def somar(n1,n2):
    return int(n1)+ int(n2)

a = input(digitar())
b = input(digitar())

print("Soma = ",somar(a,b))


#=========================


def ler_nota():
    n = float(input("Digite uma nota: "))
    return "Digite uma nota: "

def situacao(n1,n2):
    media = (n1+n2)/2
    print("Media: ",media, " Situação: ", end = "")
    if media >= 7.0:
        print("Aprovado")
    else:
        print("Reprovado")

try:
    a = ler_nota()
    b = ler_nota()
    situacao(a,b)
except Exception:
    print("Impossivel fazer a conta")


#=========================

