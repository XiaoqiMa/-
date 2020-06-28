# 快排：先调配出左右子数组，然后对于左右子数组进行排序
# 数组取标杆 pivot，将小元素放 pivot左边，大元素放右侧，
# 然后依次 对右边和右边的子数组继续快排；以达到整个序列有序。


def quick_sort(a):
    quick_sort_c(a, 0, len(a) - 1)


def quick_sort_c(a, left, right):
    if left < right:
        border = partition(a, left, right)
        quick_sort_c(a, left, border - 1)
        quick_sort_c(a, border + 1, right)


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


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)
    test_quick_sort()

# def quick_sort(a: List[int]):
#     _quick_sort_between(a, 0, len(a) - 1)
#
#
# def _quick_sort_between(a: List[int], low: int, high: int):
#     if low < high:
#         # get a random position as the pivot
#         k = random.randint(low, high)
#         a[low], a[k] = a[k], a[low]
#
#         m = _partition(a, low, high)  # a[m] is in final position
#         _quick_sort_between(a, low, m - 1)
#         _quick_sort_between(a, m + 1, high)
#
#
# def _partition(a: List[int], low: int, high: int):
#     pivot, j = a[low], low
#     for i in range(low + 1, high + 1):
#         if a[i] <= pivot:
#             j += 1
#             a[j], a[i] = a[i], a[j]  # swap
#     a[low], a[j] = a[j], a[low]
#     return j
