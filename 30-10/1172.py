#Atividade 1172

vetor = []
for i in range(10):
    vetor.append(int(input()))
for i in range(10):
    if vetor[i]<i:
        vetor[i] = 1
for i in range(10):
    print(f"X[{i}] =", vetor[i])