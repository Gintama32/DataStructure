#this is the implementation of bubble sort without recursion and uses nested loop instead
def bblesrt(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    
array = [3,5,2,1,9]
bblesrt(array)
print(array)