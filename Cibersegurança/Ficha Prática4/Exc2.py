somatorio = 0

for i in range(11,52):
    if i % 2 != 0:
        print(i)
        somatorio = somatorio + i

print(f"Somatório: {somatorio}")
