#Atividade 1175
vetor = []
vetortroca = []
for i in range(20):
    vetor.append(int(input()))

indexnegativo = 19
for i in range(20):
    vetortroca.append(vetor[indexnegativo])
    indexnegativo =indexnegativo -1

for i in range(20):
    print(f"N[{i}] =",vetortroca[i])