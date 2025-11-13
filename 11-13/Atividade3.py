def dia1( km):
    res = 0

    res += 4.50
    res += (km* 2.75)

    printar(res)

def dia2( km):
    res = 0

    res +=5.85
    res += (km* 3.50)

    printar(res)
    
def printar(res):
     print(f"O valor da corrida da corrida é {res}")

cond = True 
while cond:
    try:
        dia = int(input("Digite o dia: "))
        hr = int(input("Digite a hora: "))
        km =int(input("Digite a quantidade de km: "))
        cond = False
    except Exception:
        print("Digite corretamente")



if dia>=2 and dia<=7:
    if hr>=6 and hr<=20:
        print("Bandeira 1")
        dia1(km)
    else:
        print("Bandeira 2")
        dia2(km)
elif dia ==1:
    print("Bandeira 2")
    dia2(km)
else:
    print("Digite o dia corretamente")