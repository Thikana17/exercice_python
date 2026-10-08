temperature = 20

if temperature < 0:
    print("gel")
elif temperature < 15:
    print("froid")
elif temperature < 25:
    print("doux")
else:
    print("chaud")

temperature = -3
print("gel" if temperature < 0 else "froid" if temperature < 15 else "doux" if temperature < 25 else "chaud")

temperature = 0
print("gel" if temperature < 0 else "froid" if temperature < 15 else "doux" if temperature < 25 else "chaud")

temperature = 15
print("gel" if temperature < 0 else "froid" if temperature < 15 else "doux" if temperature < 25 else "chaud")

temperature = 31
print("gel" if temperature < 0 else "froid" if temperature < 15 else "doux" if temperature < 25 else "chaud")
