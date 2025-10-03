from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")


try:
    data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")

    hoje = datetime.today()
    idade = hoje.year - data_nasc.year


    if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
        idade -= 1

    print("Sua idade é:", idade)

    if idade >= 18:
        print("Você pode assinar a documentação.")
    else:
        print("A documentação precisa ser assinada por seu responsável legal.")

except ValueError:
    print("Data de nascimento inválida.")
