# Linear Search

def linearSearch(array, n, x):

    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [5, 8, 2, 9, 17, 25]
x = 17
n = len(array)

result = linearSearch(array, n, x)
if result == -1:
    print("Element topilmadi!")
else:
    print(f"Element {result} chi index da topildi!")
