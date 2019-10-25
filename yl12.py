fruits = ["arbuus", "pirn", "apelsin"]
print (fruits [0])
fruits = ["arbuus", "pirn", "apelsin", "kirss"]
print (fruits[-1])
fruits[1] = "laim"
print(fruits)
if "õun" in fruits:
    print("Õun on nimekirjas")
else:
    print("Õun ei ole nimekirjas")
print(len(fruits))
fruits.remove("apelsin")
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)