numeros = []
print("Digite números (digite 0 para encerrar):")

while True:
    entrada = input("Número: ")
    
    try:
        numero = float(entrada)
        
        if numero == 0:
            break
        
        numeros.append(numero)
    
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro ou decimal.")

quantidade = len(numeros)
soma = sum(numeros)

print('\n Total da Soma = ', soma)
print('\n Quantidade de valores: ', quantidade)