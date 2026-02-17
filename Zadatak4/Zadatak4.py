#Učitajte cijeli broj N. Nakon toga učitavajte cijele brojeve tako dugo dok opet ne učitate broj N. Ispišite koji je predzadnji broj bio učitan (broj prije broja N)

N = int(input("Napisi N broj: "))

prethodni = None

while True:
    X = int(input("Upisi cijeli broj: "))

    if X == N:
        print(prethodni)
        break

    prethodni = X
