#insertion sort implementation. It has O(N^2) time complexity in worst-case but has O(N) on best and O(N^2/2) time complexity in average case scenario.
class Insertion_Sort:
    def __init__(self,arr):
        self.arr = arr

    def insertion_sort(self):
        #start from second element and compare it to its immediate left element
        for i in range(1,len(self.arr)):
            current_value = self.arr[i]
            position = i-1
            #do the comparing to left for every ith element.
            while position>=0:
                #if left value is greater than right value, we shift it to the right and make space
                if  self.arr[position]>current_value:
                        self.arr[position+1]= self.arr[position]
                        #shifiting our position index further to the left to compare other left elements till we encounter lesser element than current_value to which we are comparing
                        position -= 1
                #once lesser value is encountered, we break out of while loop for that current_value since that indicates the other left element are already sorted.
                else:
                     break
            #after breaking out, we know where to put our current value since gap has been created because we shifter elements to the right.
            self.arr[position+1] = current_value
        #finally return the sorted array.
        return arr

arr=[10,5,7,4,5,3]
#initializing Insertion_Sort class with our 'arr' array.
sort_arr = Insertion_Sort(arr)
#calling our insertion_sort() method on the instance we created.
sort_arr.insertion_sort()
print(arr)
