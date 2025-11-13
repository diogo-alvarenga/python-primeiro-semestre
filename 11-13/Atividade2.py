def calcularQuant(quant):
    res = 0
    if quant>1:
        res = ((quant-1)*2.95)+10.95
        print(f"A quantidade de produtos comprados foi: {quant}")
        print(f"O frete é {res}")
    elif quant == 1:
        res = 10.95
        print(f"A quantidade de produtos comprados foi: {quant}")
        print(f"O frete é {res}")
    else:
        print("Nenhum produto digitado")

quant = int(input("Digite a quantidade "))
calcularQuant(quant)