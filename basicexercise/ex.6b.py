def classify_triangle(a, b, c):
    if a == b == c:
        result = "Equilateral"
    elif a == b or a == c or b == c:
        result = "Isosceles"
    else:
        result = "Scalene"
    return result

a = int(input("enter the first length: "))
b = int(input("enter the second length: "))
c = int(input("enter the third length: "))
print(classify_triangle(a, b, c))