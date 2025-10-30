#Atividade 174
vetor =[]
vetorposicao=[]
vetorvalor=[]
quant = 0
for i in range(100):
    vetor.append(float(input()))
    
for i in range(100):
    if vetor[i] <= 10:
        vetorposicao.append(i)
        vetorvalor.append(vetor[i])
        quant = quant +1

for i in range(quant):
    print(f"A[{vetorposicao[i]}] =",vetorvalor[i])