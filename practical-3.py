import random
import time


# =========================================================
# MAX HEAP
# =========================================================

def max_heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        max_heapify(arr, n, largest)


def max_heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        max_heapify(arr, i, 0)


# =========================================================
# MIN HEAP
# =========================================================

def min_heapify(arr, n, i):
    smallest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        min_heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)

    # Build Min Heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        min_heapify(arr, i, 0)

    # Reverse to get ascending order
    arr.reverse()


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    n = int(input("Enter number of elements: "))

    # Generate random elements
    original = [random.randint(0, 99999) for _ in range(n)]

    # Create copies
    max_heap_array = original.copy()
    min_heap_array = original.copy()


    # =====================================================
    # MAX HEAP SORT
    # =====================================================

    start_max = time.perf_counter_ns()

    max_heap_sort(max_heap_array)

    end_max = time.perf_counter_ns()


    # =====================================================
    # MIN HEAP SORT
    # =====================================================

    start_min = time.perf_counter_ns()

    min_heap_sort(min_heap_array)

    end_min = time.perf_counter_ns()


    # =====================================================
    # CALCULATE TIME
    # =====================================================

    nano_max = end_max - start_max
    micro_max = nano_max / 1000
    milli_max = nano_max / 1_000_000
    sec_max = nano_max / 1_000_000_000

    nano_min = end_min - start_min
    micro_min = nano_min / 1000
    milli_min = nano_min / 1_000_000
    sec_min = nano_min / 1_000_000_000


    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    print("\n========== MAX HEAP SORT ==========")
    print("Nanoseconds  :", nano_max, "ns")
    print("Microseconds :", micro_max, "us")


    print("\n========== MIN HEAP SORT ==========")
    print("Nanoseconds  :", nano_min, "ns")
    print("Microseconds :", micro_min, "us")


# =========================================================
# PROGRAM EXECUTION
# =========================================================

if __name__ == "__main__":
    main()