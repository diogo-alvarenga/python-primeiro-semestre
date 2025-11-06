#Atividade 1080
vetor = []
vetormaior=0
posicao =0

for i in range(100):
    vetor.append(int(input()))

for i in range(100):
    if vetormaior<vetor[i]:
        vetormaior = vetor[i]
        posicao = i+1
        
print(vetormaior)
print(posicao)
