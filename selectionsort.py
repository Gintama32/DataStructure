#simple implentation of selection sort with nested loop
def selectionSort(array):
    for i in range(len(array)-1):
        smallest = array[i]
        for j in range(i+1,len(array)):
            if smallest > array[j]:
                smallest = array[j]
                array[i],array[j] = array[j],array[i]
array = [3,5,2,7,1]
selectionSort(array)
print(array)


