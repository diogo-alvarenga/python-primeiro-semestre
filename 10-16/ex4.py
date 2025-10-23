import random

numero_secreto = random.randint(1, 20)

print("Adivinhe o número entre 1 e 20:")

while True:
    entrada = input("Seu palpite: ")

    try:
        palpite = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")

