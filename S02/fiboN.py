def fibonacci(n):
    a , b = 0 , 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a+b
        i += 1
    return lst
lst = fibonacci(16)
print("the 5th fibonacci term is:", lst[5])
print("the 10th fibonacci term is:", lst[10])
print("the 15th fibonacci term is:", lst[15])