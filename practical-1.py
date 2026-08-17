import random
import time


# =========================================================
# Bubble Sort
# =========================================================
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# =========================================================
# Selection Sort
# =========================================================
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# =========================================================
# Insertion Sort
# =========================================================
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# =========================================================
# Merge Sort
# =========================================================
def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# =========================================================
# Quick Sort
# =========================================================
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# =========================================================
# Main Program
# =========================================================
def main():

    n = 100

    # Generate 100 random numbers
    arr = [random.randint(0, 999) for _ in range(n)]

    print("Number of Elements =", n)
    print()

    # -----------------------------------------------------
    # Bubble Sort
    # -----------------------------------------------------
    start = time.perf_counter()

    temp = arr.copy()
    bubble_sort(temp)

    stop = time.perf_counter()

    print("Bubble Sort Time    :", 
          int((stop - start) * 1_000_000), "microseconds")


    # -----------------------------------------------------
    # Selection Sort
    # -----------------------------------------------------
    start = time.perf_counter()

    temp = arr.copy()
    selection_sort(temp)

    stop = time.perf_counter()

    print("Selection Sort Time :", 
          int((stop - start) * 1_000_000), "microseconds")


    # -----------------------------------------------------
    # Insertion Sort
    # -----------------------------------------------------
    start = time.perf_counter()

    temp = arr.copy()
    insertion_sort(temp)

    stop = time.perf_counter()

    print("Insertion Sort Time :", 
          int((stop - start) * 1_000_000), "microseconds")


    # -----------------------------------------------------
    # Merge Sort
    # -----------------------------------------------------
    start = time.perf_counter()

    temp = arr.copy()
    merge_sort(temp, 0, n - 1)

    stop = time.perf_counter()

    print("Merge Sort Time     :", 
          int((stop - start) * 1_000_000), "microseconds")


    # -----------------------------------------------------
    # Quick Sort
    # -----------------------------------------------------
    start = time.perf_counter()

    temp = arr.copy()
    quick_sort(temp, 0, n - 1)

    stop = time.perf_counter()

    print("Quick Sort Time     :", 
          int((stop - start) * 1_000_000), "microseconds")


# =========================================================
# Program Execution
# =========================================================
if __name__ == "__main__":
    main()