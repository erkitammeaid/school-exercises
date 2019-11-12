import random

valikud = ["r", "p", "s"]
valik = input("tee oma valik: ")
cpuvalik = random.randint(0,2)
if valik == cpuvalik:
    print("Sinu valik: ", + valik + ", Arvuti valik: " + cpuvalik + ", Tulemus on viik")

elif valik > cpuvalik:
    print("Sinu võit!")

else valik < cpuvalik:
    print("Oled kaotanud")

replay = input("Kas soovid veel mängida?(y/n): ")
