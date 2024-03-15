nums= [5,2,6,8,1,9]
target = 12
def pair_finder(lists,target):
    output=[]
    for num in lists:
        search = target - num
        if search in lists and ((search,num) not in output) and (num!=search): 
            output.append((num,search))
    return output
pairs = pair_finder(nums,target)
if len(pairs)==0:
    print("Pair not found")
else:
    for pair in pairs:
        print("Pair found", pair)



    

    
