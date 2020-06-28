# 插入排序（Insertion Sort） 从前到后逐步构建有序序列；
# 对于未排序数据，在已排序序列中从后 向前扫描，找到相应位置并插入。


def insertion_sort(a):
    if len(a) < 1:
        return a

    for i in range(1, len(a)):
        value = a[i]
        j = i-1
        while j >= 0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value


def test_insertion_sort():
    test_array = [1, 1, 1, 1]
    insertion_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]


test_insertion_sort()