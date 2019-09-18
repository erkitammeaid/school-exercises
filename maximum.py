a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = int(input("Sisesta kolmas arv: "))

if a > b and a > c :
    maximum = a
elif b > c:
    maximum = b
else:
    maximum = c
    
print("Maksimum on " +str(maximum))