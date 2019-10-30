import random
kivi = 1
paber = 2
käärid = 3
x = (random.randint(0,4))
bot_list = ["kivi", "paber", "käärid"]
bot_equals = ["S", "P", "R"]
user_equals = ["S", "P", "R"]
for x in bot_list:
    user_input = str(input("Vali kas kivi, paber või käärid: "))
    print(user_input)
    print(random.choice(bot_list))