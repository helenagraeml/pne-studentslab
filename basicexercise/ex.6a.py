def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = float(input("enter a number: "))
print(f"is_even({number}) =", is_even(number))