temperatures =[12.5 , 14 , 9.5, 17 , 21 , 19.5 , 11]

moyennne_temperatures = sum(temperatures) / len(temperatures)
print(moyennne_temperatures, round(moyennne_temperatures, 2))

print(max(temperatures))
print(min(temperatures))

for i in range(len(temperatures)):
    if temperatures[i] >15:
        print("températures au dessus de 15°C")

for i in range(len(temperatures)):
    temperatures[i] = temperatures[i] * 9 / 5 + 32

print(temperatures[i] * 9 / 5 + 32)

for i in range(len(temperatures)):
    jour = i + 1

    print("jour", jour, ":", temperatures[i], "°C")
     
