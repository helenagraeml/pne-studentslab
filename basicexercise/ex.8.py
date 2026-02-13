def average(grades):
    avg = sum(grades) / len(grades)
    return avg

def get_status(avg):
    if avg >= 5 :
        return "PASS"
    else:
        return "FAIL"
students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

for i in students:
    name = i["name"]
    grades = i["grades"]
    avg = round(average(grades), 2)
    status = get_status(avg)
    print(f"{name} : {avg} ---> {status}")
