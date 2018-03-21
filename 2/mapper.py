import csv
import sys
'''
def map():
      d = []
      with open('temp.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                  d.append(row[3])
            return d

print(map())
'''

def map(record):
    type, value, business_date = record.split(",")
    yield type, value
