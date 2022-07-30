def binarySearch(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        midle = (low + high) // 2
        guess = lista[midle]

        if guess == item:
            return midle
        elif guess > item:
            high = midle - 1
        else:
            low = midle + 1

    return None

my_list = [1, 3, 5, 7, 9]

print (binarySearch(my_list, 3))
print (binarySearch(my_list, -1))
