def factorial(num):
    n = num -1
    while n>0:
        num = num *n 
        n = n-1
    factor =num
    count = 0
    for num in str(factor)[::-1]:
        num = int(num)
        while num == 0:
            count+=1
    return count
print(factorial(6))


    

