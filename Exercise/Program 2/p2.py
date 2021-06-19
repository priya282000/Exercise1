import csv
try:
    with open("C:\\Users\\padmapriya\\Downloads\\CT.csv",'r') as data:
        for line in csv.DictReader(data):
            print(line)
except IOError:
    print("File not found exception")