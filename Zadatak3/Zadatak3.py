kolikoimabrojeva = 0   # koliko ima brojeva
zbrojbrojeva = 0   # njihov zbroj
while True:
    N = int(input("Napisi Dvoznamenkasti broj: "))
    if 10<= N <= 99:
        kolikoimabrojeva += 1
        zbrojbrojeva += N

    elif N == -1:
        print("Rezultati...")
        break

    else:
        print("Netocan broj")

print("Prosjek je", zbrojbrojeva / kolikoimabrojeva)
