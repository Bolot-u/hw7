
def binary_search(list, vol):
    list.sort()
    middle = len(list) // 2
    last = 0
    first = len(list) - 1
    while list[middle] != vol and last <= first:
        if vol > list[middle]:
            last = middle + 1
        else:
            first = middle - 1
        middle = (last + first) // 2

    if last > first:
        print("Not found")
    else:
        print(f"Was found: {middle}")

print(binary_search([1, 2, 3, 4], 1))


def bubbleSort(array):
    length = len(array)
    for i in range(length - 1):
        for k in range(0, length - i - 1):

            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]

arr = [21, 19, 17, 33, 32, 20]

print("До сортировки:")
for i in range(len(arr)):
    print("%d" % arr[i]),
bubbleSort(arr)

print("После сортировки:")
for i in range(len(arr)):
    print("%d" % arr[i])








