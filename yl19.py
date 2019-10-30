vowels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
text = "banaan"
text = text.lower()
i = 0
for char in text:

    if char in vowels:
        i += 1
        
print(i)             