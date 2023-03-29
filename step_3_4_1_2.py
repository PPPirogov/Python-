import csv

students = [
    ["Greg","dean",70,60,55,"good boy"],
    ["Sam","Won",90,35,45,"bad, boy"]
]
with open("exemple.csv","a",newline='') as f:
    writer1 =csv.writer(f,quoting = csv.QUOTE_NONNUMERIC)
    writer1.writerows(students)