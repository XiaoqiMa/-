def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def selection_sort(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i, len(a)):
            if a[j] < a[min_ind]:
                min_ind = j
        a[min_ind], a[i] = a[i], a[min_ind]


def insertion_sort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = i - 1
        while j >= 0 and a[j] > val:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = val


def quick_sort(a):
    quick_sort_c(a, 0, len(a) - 1)


def quick_sort_c(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quick_sort_c(a, left, pivot - 1)
        quick_sort_c(a, pivot + 1, right)


def partition(a, left, right):
    pivot_val = a[right]
    border, pointer = left, left
    while pointer <= right:
        if a[pointer] < pivot_val:
            a[border], a[pointer] = a[pointer], a[border]
            border += 1
        pointer += 1
    a[border], a[right] = a[right], a[border]
    return border


def merge_sort(a):
    merge_sort_c(a, 0, len(a) - 1)


def merge_sort_c(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_c(a, left, mid)
        merge_sort_c(a, mid + 1, right)
        merge(a, left, mid, right)


def merge(a, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    start = i if i <= mid else j
    end = mid if i <= mid else right
    temp.extend(a[start:end + 1])
    a[left:right + 1] = temp


def build_heap(a):
    for i in range(len(a) // 2, -1, -1):
        heapify(a, i)


def heapify(a, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arr_len and a[left] > a[largest]:
        largest = left
    if right < arr_len and a[right] > a[largest]:
        largest = right
    if largest != i:
        swap(a, i, largest)
        heapify(a, largest)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def heap_sort(a):
    global arr_len
    arr_len = len(a)
    build_heap(a)
    for i in range(len(a) - 1, -1, -1):
        swap(a, i, 0)
        arr_len -= 1
        heapify(a, 0)
    return a


def test_heap_sort():
    a1 = [3, 5, 6, 7, 8]
    heap_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    heap_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    heap_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    heap_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


test_heap_sort()
