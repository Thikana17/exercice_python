temperature = -3

if temperature < 0:
    print(f"{temperature} °C : gel")
elif temperature < 15:
    print(f"{temperature} °C : froid")
elif temperature < 25:
    print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")

temperature = 0

if temperature < 0:
    print(f"{temperature} °C : gel")
elif temperature < 15:
    print(f"{temperature} °C : froid")
elif temperature < 25:
    print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")

temperature = 15

if temperature < 0:
    print(f"{temperature} °C : gel")
elif temperature < 15:
    print(f"{temperature} °C : froid")
elif temperature < 25:
    print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")

temperature = 31

if temperature < 0:
    print(f"{temperature} °C : gel")
elif temperature < 15:
    print(f"{temperature} °C : froid")
elif temperature < 25:
    print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")




annee = 2024

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"{annee} : bissextile")
else:
    print(f"{annee} : non bissextile")

annee = 1900

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"{annee} : bissextile")
else:
    print(f"{annee} : non bissextile")

annee = 2000

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"{annee} : bissextile")
else:
    print(f"{annee} : non bissextile")