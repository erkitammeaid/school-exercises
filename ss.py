name = str.capitalize(input("Sisesta oma nimi: "))
print("Tervist " + name)

location = str.capitalize(input("Sisestage oma elukoht: "))
print("Elukohas " + location + " on hea värske õhk")

age = input("Sisestage oma vanus: ")
print("Te olete " + age + " aastane")
if int(age) >= 18:
    print("Võite juba autot juhtida")
elif int(age) < 18:
    print("Olete liiga noor, et autot juhtida")