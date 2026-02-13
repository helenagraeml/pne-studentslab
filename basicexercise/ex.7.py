student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])
print("Number of subjects:", len(student["subjects"]) )
print("Enrolled in PNE:", "PNE" in student["subjects"])
print("Databases grade:", student["grades"]["Databases"])
avrg = sum(student["grades"].values()) / len(student["grades"])
print("Average grade:", round(avrg, 2))
print("Student grade:")
for key, value in student["grades"].items():
    print(f"   {key}: {value}")