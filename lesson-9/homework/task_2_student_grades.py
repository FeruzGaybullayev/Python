import csv


grades = []

with open('grades.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append({
            'Name': row['Name'],
            'Subject': row['Subject'],
            'Grade': int(row['Grade'])
        })

