import csv
import os


def _map():
    """"Разбиваем csv файл на строки"""
    with open('temp.csv', newline='') as File:
        reader = csv.reader(File)
        next(reader)
        for row in reader:
           yield row


def _reduce():
    for i in (_map()):
        try:
            os.makedirs(i[3])
            f = open('{}/data.txt'.format(i[3]), 'a', encoding='utf-8')
            f.write(",".join(i[:-1]))
            f.close()
        except OSError:
            """если папка существует, то записываем данные в файл """
            f = open('{}/data.txt'.format(i[3]), 'a', encoding='utf-8')
            print(i[:-1])
            f.write('\n' + ",".join(i[:-1]))
            f.close()

_reduce()
#print(_map())