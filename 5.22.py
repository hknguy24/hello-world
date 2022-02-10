#Huy Kevin Nguyen
#PSID: 1346435

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

serv1 = input("\nSelect first service:\n")
price1 = 0
if serv1 == "Oil change":
    price1 = 35
elif serv1 == "Tire rotation":
    price1 = 19
elif serv1 == "Car wash":
    price1 = 7
elif serv1 == "Car wax":
    price1 = 12
elif serv1 == "-":
    price1 = 0
serv2 = input("Select second service:\n")
price2 = 0
if serv2 == "Oil change":
    price2 = 35
elif serv2 == "Tire rotation":
    price2 = 19
elif serv2 == "Car wash":
    price2 = 7
elif serv2 == "Car wax":
    price2 = 12
elif serv2 == "-":
    price2 = 0

print("\nDavy's auto shop invoice\n")
if serv1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: " + serv1 + ", $" + str(price1))
if serv2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: " + serv2 + ", $" + str(price2))
total = price1 + price2
print("\nTotal: $" + str(total))