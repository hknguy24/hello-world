#Huy Nguyen
#PSID 1346435

num_calls = 0

def partition(ids, a, b):
    pivot = ids[b]
    index = a - 1
    for c in range(a, b):
        if ids[c] <= pivot:
            index += 1
            ids[index], ids[c] = ids[c], ids[index]
    ids[index+1], ids[b] = ids[b], ids[index+1]
    return index+1


def quicksort(ids, a, b):
    if a < b:
        p = partition(ids, a, b)
        quicksort(ids, a, p-1)
        quicksort(ids, p+1, b)

if __name__ == "__main__":
    ids = []
    id = input()
    while id != "-1":
        ids.append(id)
        id = input()
    quicksort(ids, 0, len(ids) - 1)
    num_calls = int(2 * len(ids) - 1)
    print(num_calls)
    for id in ids:
        print(id)