dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mes de nascimento: "))
ano = int(input("Digite o seu ano de nascimento: "))

if type(dia) == int and type(mes)== int and type(ano)== int:
    if dia<= 32 or mes <=12:
        anoatual = 2025
        idade = 2025 -ano

        print("Sua idade é ", idade)
        if idade>= 18:
            print("Voce pode assinar a documetacao")
        else:
            print("A documentaçao precisa ser assinada por seu responsavel legal ")
    print("Data de nascimento invalida!!")
else:
    print("Data de nascimento invalida!!")