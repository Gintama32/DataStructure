#simple bubblesort implementation using recursion
array = [3,5,1,8,7]
def bubblesort(rnge):
    if rnge == 1:
        return 
    
    for i in range(rnge-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    (bubblesort(rnge-1))


bubblesort(len(array))
print(array)