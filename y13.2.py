animal = str(input("Sisestage oma lemmikloom: "))
words = animal.split()
for word in words:
    print(word[0])
animals = ["koer", "kass", "siga"]
print(animals)
words2 = animals[-1].split("g")
for word in words2:
    print(word)