print("===== Cardápio ====")
print("Hamburguer = 8 R$")
print("Cheeseburguer = 9,50 R$")
print("Fritas = 5,50 R$")
print("Refrigerante = 5 R$")
print("Milkshake = 8 R$")
print("==================\n")

hamburguer = 8
cheeseburguer = 9.50
fritas  = 5.50
refrigerante = 5
milkshake = 8

quantidadeHamb = int(input("Quantos hamburgueres consumiu? "))
quantidadeCheese = int(input("Quantos CheeseBurguer consumiu? "))
quantidadeFritas = int(input("Quantas fritas consumiu? "))
quantidadeRefri = int(input("Quatos refrigerantes consumiu? "))
quantidadeMilk = int(input("Quantos milkshakes consumiu? "))


soma = (hamburguer*quantidadeHamb) + (cheeseburguer*quantidadeCheese) + (fritas*quantidadeFritas) + (refrigerante*quantidadeRefri) + (milkshake*quantidadeMilk)

print("A sua conta final é:  ", soma)