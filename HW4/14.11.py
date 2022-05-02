#Huy Nguyen
#PSID 1346435

def selection_sort_descend_trace(n):
    for i in range(len(n) - 1):
        k = i
        for j in range(i + 1, len(n)):
            if n[k] < n[j]:
                k = j
        n[i], n[k] = n[k], n[i]
        for value in n:
            print(value, end=" ")
        print()
    return n

if __name__ == "__main__":
    n = []
    n = [int(x) for x in input("").split()]
    selection_sort_descend_trace(n)