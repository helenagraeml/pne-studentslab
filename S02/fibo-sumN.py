def fibosum(n):
    a, b = 0, 1
    lst = []
    for i in range(n):
        lst.append(a)
        a, b = b, a + b
        i += 1
    return lst
print("Sum of fibonaccy sequence of the firt 5th terms is :",sum(fibosum(6)))
print("Sum of fibonaccy sequence of the firt 10th  terms is :",sum(fibosum(11)))