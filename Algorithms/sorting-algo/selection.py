# 选择排序（Selection Sort） 每次找最小值，然后放到待排序数组的起始位置。
# https://www.toutiao.com/a6767920995815653892/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1577785975&app=news_article&utm_source=weixin&utm_medium=toutiao_ios&req_id=20191231175254010026076020270B6E37&group_id=6767920995815653892


def selection_sort(a):
    if len(a) < 1:
        return a

    for i in range(len(a)):
        min_index = i
        min_val = a[i]
        for j in range(i, len(a)):
            if a[j] < min_val:
                min_index = j
                min_val = a[j]
        a[i], a[min_index] = a[min_index], a[i]


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]


test_selection_sort()
