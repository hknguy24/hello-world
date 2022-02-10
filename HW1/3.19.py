#Huy Kevin Nguyen
#PSID: 1346435

h = float(input("Enter wall height (feet):\n"))
w = float(input("Enter wall width (feet):\n"))

area = int(h * w)
print("Wall area: " + str(area) + " square feet")

paint = float(area/350)
print("Paint needed: " + '{:.2f}'.format(paint) + " gallons")

can = int(area/350) + (area % 350 > 0)
print("Cans needed: " + str(can) + " can(s)")

color = input("\nChoose a color to paint the wall:\n")
cost = 0
if color == "red":
    cost = 35
elif color == "blue":
    cost = 25
elif color == "green":
    cost = 23
cost = cost * can
print("Cost of purchasing " + color + " paint: $" + str(cost))

