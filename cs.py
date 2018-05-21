import csv

with open('tamil.csv') as csvfile:
    read_csv = csv.reader(csvfile,delimiter=',')
    for row in read_csv:
        # print(row[1])
        if