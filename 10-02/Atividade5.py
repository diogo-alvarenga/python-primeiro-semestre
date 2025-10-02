num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3= int(input("Digite o terciero numero: "))

if num1 == num2 and num1 ==num3:
    print("Seus numero sao todos iguais")
elif num1 ==num2 or num1 == num3 or num2 == num3:
    print("Alguns dos seu numeros estao iguais")
else:
    if num1> num2 and num1>num3:
        if num2>num3:
            print("O maior numero é o primeiro, ",num1, " o menor é o terceiro ",num3)
        else:
            print("O maior numero o primeiro,  ",num1, " o menor é o segundo ", num2 )
    elif num2> num1 and num2 > num3:
        if num1>num3:
            print("O maior numero é o segundo, ",num2, " seu menor numero é o terceiro, ",num3)
        else:
            print("Seu maior numero é o segundo, ",num2," e seu menor numero é o primeiro, ",num1)
    elif num3> num2 and num3> num1:
        if num1>num2:
            print("Seu maior numero é o terceiro ", num3, " e seu menor numero é o segundo, ", num2)
        else:
            print("Seu maior numero é o terceiro, ",num3, " e seu menor numero é o primeiro, ", num1)