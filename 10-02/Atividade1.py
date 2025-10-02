num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if type(num1)==int and type(num2) == int :
    if num1==num2:
        print("Os numeros são iguais")
    else:
        if num1>num2:
            print("O numero maior é ", num1)
        else:
            print("O numero maior é ", num2)


else:
    print("Favor digitar inteiros")