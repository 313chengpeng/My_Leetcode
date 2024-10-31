import random
def partition(arr, low, high):
    # 随机选择基准
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]
    return low


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

if __name__ == '__main__':
    arr = [8,5,1,3,2,10,11,4,12,20]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("排序后的数组:")
    for i in range(n):
        print("%d" % arr[i], end=" ")
