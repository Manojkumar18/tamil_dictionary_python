import csv
a=str(input('Enter the English word :'))
with open('tamil.csv') as csvfile:
    read_csv = csv.reader(csvfile,delimiter=',')
    for row in read_csv:
        # print(row[0])
        if row[0] == a:
            print(row[1])
        # else:
        #     print("No meaning word found")