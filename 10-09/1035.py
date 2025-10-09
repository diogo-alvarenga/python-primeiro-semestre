#Exercicio 4

A=int(input())
B=int(input())
C=int(input())
D=int(input())
if B > C and D > A:
        if (C + D) > (A + B):
            if C > 0 and D > 0:
                if A % 2 == 0:
                    print("Valores aceitos")
else:
    print("Valores nao aceitos")