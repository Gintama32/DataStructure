#implementation of Quicksort array...
class QuickSort:
    def __init__(self,array):
        self.array = array
 # implementation of partition to partition the array...
    def partition(self,left_pointer,right_pointer):
        pivot_index = right_pointer  
        pivot = self.array[pivot_index]
        right_pointer -=1
        while True:
            while self.array[left_pointer] < pivot:
                left_pointer+=1
            
            while self.array[right_pointer]>pivot:
                right_pointer-=1
            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer+=1
        self.array[left_pointer],self.array[pivot_index]=self.array[pivot_index],self.array[left_pointer]
        return left_pointer
# implementing quick_sort method for the Quicksort class, to sort given two index of an array
    def quick_sort(self,left_index,right_index):
        if right_index - left_index <=0:
            return 
        pivot_index = self.partition(left_index,right_index)
        self.quick_sort(left_index,pivot_index-1)
        self.quick_sort(pivot_index+1, right_index)
#assigning values to array 
array = [0,5,2,1,6,3]
#initializing class with the array as argument..
sorting = QuickSort(array)
# sorting the array with quick_sort method of QuickSort class..
sorting.quick_sort(0,len(array)-1)
#finally displaying the sorted array..
print(array)
#time complexity of O(NlogN)