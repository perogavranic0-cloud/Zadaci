#Učitajte 10 cijelih brojeva. Za svaki učitani broj ispišite „Djeljiv s 3”, „Djeljiv s 4”, „Djeljiv s 3 i 4” ili „Čudan ti je broj” ako nije djeljiv ni s 3, ni s 4. (3b)


for N in range(10):
    N = int(input("Napisi N broj: "))
    if N % 3 == 0 and N % 4 == 0:
        print("Broj je dijeljiv sa 3 i 4")
    elif N % 3 == 0:
        print("Broj je djeljiv sa 3")
    elif N % 4 == 0:
        print("Broj je djeljiv sa 4")
    else:
        print("Čudan ti je broj")
