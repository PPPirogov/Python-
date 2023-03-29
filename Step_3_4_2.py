import csv,time

Primary_Type = {}
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = time.strptime(row["Date"],"%m/%d/%Y %H:%M:%S %p")
        if a.tm_year == 2015:
            b = Primary_Type.setdefault(row["Primary Type"],0) + 1
            Primary_Type[row["Primary Type"]] = b
max = 0
name = 'a'
#print(Primary_Type)
for a in Primary_Type:
    if Primary_Type[a]>max:
        name = a
        max= Primary_Type[a]

print(name)
print(max)

