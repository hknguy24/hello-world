dict = {}
p1n = int(input("Enter player 1's jersey number:\n"))
p1r = int(input("Enter player 1's rating:\n"))
dict[p1n] = p1r
p2n = int(input("\nEnter player 2's jersey number:\n"))
p2r = int(input("Enter player 2's rating:\n"))
dict[p2n] = p2r
p3n = int(input("\nEnter player 3's jersey number:\n"))
p3r = int(input("Enter player 3's rating:\n"))
dict[p3n] = p3r
p4n = int(input("\nEnter player 4's jersey number:\n"))
p4r = int(input("Enter player 4's rating:\n"))
dict[p4n] = p4r
p5n = int(input("\nEnter player 5's jersey number:\n"))
p5r = int(input("Enter player 5's rating:\n"))
dict[p5n] = p5r
print("\nROSTER")
for i, j in sorted(dict.items()):
    print("Jersey number: %d, Rating: %d" % (i, j))

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    option = input("\nChoose an option:\n")
    if option == 'a':
        p6n = int(input("Enter a new player's jersey number:\n"))
        p6r = int(input("Enter a new player's rating:\n"))
        dict[p6n] = p6r
    elif option == 'd':
        prem = int(input("Enter a jersey number:\n"))
        if prem in dict:
            del dict[prem]
    elif option == 'u':
        pn = int(input("Enter a jersey number:\n"))
        pnr = int(input("Enter a new rating for the player:\n"))
        if pn in dict:
            dict[pn] = pnr
    elif option == 'r':
        rate = int(input("Enter a rating:\n"))
        print('ABOVE ' + str(rate))
        for i, j in sorted(dict.items()):
            if j > rate:
                print("Jersey number: %d, Rating: %d" % (i, j))
    elif option == 'o':
        print("\nROSTER")
        for i, j in sorted(dict.items()):
            print("Jersey number: %d, Rating: %d" % (i, j))
    elif option == 'q':
        break

