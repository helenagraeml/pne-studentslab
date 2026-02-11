def letter(grade):
    if 9<= grade <= 10:
        result = "A"
    elif 7<= grade < 9:
        result = "B"
    elif 5 <= grade < 7:
        result = "C"
    elif 3 <= grade < 5:
        result = "D"
    else:
        result = "F"
    return result

flag = True
while flag:
    grade = float(input("Enter a grade from 0-10: "))

    if 0 > grade or grade > 10:
        print("Invalid grade.")
    else :
        print("Score --->", letter(grade))
        flag = False


