import cmath

def hipotenusa(a,b):


    c = (a*a) + (b*b)
    
    raiz = cmath.sqrt(c)

    return raiz

a = int(input("Digite o primeiro cateto "))
b = int(input("Digite o segundo cateto "))
c = hipotenusa(a,b)
print(f"A hipotenusa de {a}² e {b}² é {c}") 
