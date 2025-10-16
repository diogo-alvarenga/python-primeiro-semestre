

con= True
while con:
    try:
        num = int(input("Digite um numero inteiro para fazer o calculo de tabuada "))
        for i in range(0,11):
            print(i ," x ", num, " = ", i*num)
        pergunta = ""
        while pergunta != "sim" and pergunta != "nao" and pergunta != "não":
            pergunta = input("Deseja continuar? Responda com 'Sim','Nao'").lower()
            if(pergunta== "nao" or pergunta =="não"):
                con = False
    except Exception:
        print("Digite um numero inteiro")

