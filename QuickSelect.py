from QuickSort import QuickSort

class QuickSelect:
    def __init__(self, array):
        self.array = array
        self.quick_sort = QuickSort(self.array)  # Pass the array as an argument to QuickSort()

    def search(self, target, left_index, right_index):
        if right_index - left_index <= 0:
            return self.array[left_index]

        pivot_index = self.quick_sort.partition(left_index, right_index)

        if target < pivot_index:
            return self.search(target, left_index, pivot_index - 1)
        elif target > pivot_index:
            return self.search(target, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]

arr = [1, 2, 6, 5]
look = QuickSelect(arr)
print(look.search(2, 0, len(arr) - 1))
