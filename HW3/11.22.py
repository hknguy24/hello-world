# Huy Kevin Nguyen
# PSID: 1346435

words = input()
wordslist = words.split()

for i in wordslist:
    num = 0
    for j in wordslist:
        if i == j:
            num = num + 1
    print(i, num)