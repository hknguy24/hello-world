#Huy Kevin Nguyen
#PSID: 1346435

lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serv = float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields " + '{:.2f}'.format(serv) + " servings")
print('{:.2f}'.format(lemon) + " cup(s) lemon juice")
print('{:.2f}'.format(water) + " cup(s) water")
print('{:.2f}'.format(agave) + " cup(s) agave nectar")

servs = float(input("\nHow many servings would you like to make?\n"))
addserv = servs/serv
lemons = lemon * addserv
waters = water * addserv
agaves = agave * addserv
print("\nLemonade ingredients - yields " + '{:.2f}'.format(servs) + " servings")
print('{:.2f}'.format(lemons) + " cup(s) lemon juice")
print('{:.2f}'.format(waters) + " cup(s) water")
print('{:.2f}'.format(agaves) + " cup(s) agave nectar")


glemons = lemons/16
gwaters = waters/16
gagaves = agaves/16
print("\nLemonade ingredients - yields " + '{:.2f}'.format(servs) + " servings")
print('{:.2f}'.format(glemons) + " gallon(s) lemon juice")
print('{:.2f}'.format(gwaters) + " gallon(s) water")
print('{:.2f}'.format(gagaves) + " gallon(s) agave nectar")