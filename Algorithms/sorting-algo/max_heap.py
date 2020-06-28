# # 堆排序（Heap Sort） — 堆插入 O(logN)，取最大/小值 O(1)
#
class MaxHeap(object):

    def __init__(self, arr):
        self.heap = [0]
        for i in arr:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max_value = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max_value = self.heap.pop()
        else:
            max_value = False
        return max_value

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        if self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.__bubbleDown(largest)


m = MaxHeap([0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10])
m.push(20)
m.push(30)
print(m.peek())
print(m.heap[1:])
m.sort()
print(m.heap)


# import heapq
# a = [1, 115, 4, 10, 30]
# heapq.heappush(a, -1)
# heapq.heapify(a)
# print(a)
# print(heapq.nlargest(3, a))

