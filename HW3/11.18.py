num = input()
list = num.split()
numlist = []
i = 0

for i in range(len(list)):
    if int(list[i]) > -1:
        numlist.append(int(list[i]))

lst_str = []
numlist.sort()
for i in numlist:
    lst_str.append(str(i))
print(' '.join(lst_str) + ' ', end='')