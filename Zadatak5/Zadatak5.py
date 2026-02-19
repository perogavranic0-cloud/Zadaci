#Učitajte 12 brojeva. Izračunajte umnožak svakog trećeg učitanog broja. Ako učitate broj 0 ispišite „Slijed nije pravilan” i
#završite program. Ako učitate negativni broj, za izračun umnoška uzmite njegovu apsolutnu vrijednost. Ako niti jedan učitani broj nije bio 0, na kraju ispišite umnožak.


umnozak = 1

for i in range(1, 13):
    x = int(input("Upisi broj: "))

    if x == 0:
        print("Slijed nije pravilan")
        break

    if i % 3 == 0:
        umnozak *= abs(x)
else:
    print("Umnozak je", umnozak)
