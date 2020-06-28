# 归并：先排序左右子数组，然后合并两个有序子数组
# 1. 把长度为n的输入序列分成两个长度为n/2的子序列；
# 2. 对这两个子序列分别采用归并排序；
# 3. 将两个排序好的子序列合并成一个最终的排序序列。

def merge_sort(a):
    merge_sort_c(a, 0, len(a) - 1)


def merge_sort_c(a, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_c(a, left, mid)
        merge_sort_c(a, mid + 1, right)
        merge(a, left, mid, right)


def merge(a, left, mid, right):
    i, j = left, mid + 1
    temp = []
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


def test_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)
    test_merge_sort()
