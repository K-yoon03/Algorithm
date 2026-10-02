import time
import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    while lo < hi:
        pivot = arr[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        # arr[lo:lt] < pivot, arr[lt:gt+1] == pivot, arr[gt+1:hi+1] > pivot
        if lt - lo < hi - gt:
            quick_sort(arr, lo, lt - 1)
            lo = gt + 1
        else:
            quick_sort(arr, gt + 1, hi)
            hi = lt - 1
    return arr


def bench(name, func, data):
    copy = data.copy()
    start = time.time()
    func(copy)
    end = time.time()
    assert copy == sorted(data), f"{name} Wrong Result!"
    print(f"{name}: {end - start:.4f}s")


if __name__ == "__main__":
    # array = [random.randint(1, 100) for _ in range(10000)]
    array = [random.uniform(1, 100) for _ in range(10000)]

    bench("SelectionSort", selection_sort, array)
    bench("InsertionSort", insertion_sort, array)
    bench("QuickSort", quick_sort, array)
    bench("list.sort() (embedded)", list.sort, array)