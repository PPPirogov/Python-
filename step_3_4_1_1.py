import csv

# with open("exemple.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open("exemple.tsv") as f:
#     reader = csv.reader(f,delimiter = "\t")
#     for row in reader:
#         print(row)
#
students = [
    ["Greg","dean",70,60,55,"good boy"],
    ["Sam","Won",90,35,45,"bad, boy"]
]
with open("exemple.csv","a",newline='') as f:
    writer1 =csv.writer(f)
    # for student in students:
    #     writer1.writerow(student)
    writer1.writerows(students)
