# To sort an array


def sorted_array(arr) -> object:
    temp = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
