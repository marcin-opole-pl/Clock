import csv

with open('users.csv') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        i += 1
print(i)

with open('users.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'score', 'level'])
        writer.writerow({'name': 'ola'})
