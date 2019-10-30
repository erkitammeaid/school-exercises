import random
x = (random.randint(0, 100 ))
y = -1
while x != y:
    y = int(input("Mis Arvu mõtles programm välja? 0st 100ni: "))
    if x > y:
        print("Arv on sellest suurem")
    elif x < y:
        print("Arv on sellest väiksem")
    else:
        print("Olete pakkunud õige arvu")