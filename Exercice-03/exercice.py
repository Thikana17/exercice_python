temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]


moyenne = sum(temperatures) / len(temperatures)
minimum = min(temperatures)
maximum = max(temperatures)

print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {minimum} / Max : {maximum}")


jours_au_dessus = 0

for temperature in temperatures:
    if temperature > 15:
        jours_au_dessus += 1

print(f"Jours > 15 °C : {jours_au_dessus}")


fahrenheit = []

for temperature in temperatures:
    f = temperature * 9 / 5 + 32
    fahrenheit.append(round(f, 1))

print(f"Fahrenheit : {fahrenheit}")

for jour, temperature in enumerate(temperatures, start=1):
    print(f"Jour {jour} : {temperature} °C")