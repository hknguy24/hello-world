#Huy Nguyen
#PSID 1346435

list = input().split()
name = list[0]

while name != '-1':
    try:
        age = int(list[1]) + 1
        print("{} {}".format(name, age))
    except:
        print("{} 0".format(name))
    list = input().split()
    name = list[0]