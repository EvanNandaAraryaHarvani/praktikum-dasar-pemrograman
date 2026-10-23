
bilangan = 17

for i in range(2, bilangan):
    if bilangan % i == 0:
        print(f"{bilangan} Bukan Bilangan Prima")
        break

else:
    print(f"{bilangan} Adalah Bilangan Prima")

