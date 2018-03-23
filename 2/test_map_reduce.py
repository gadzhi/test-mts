import os
import csv
from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='localhost', port='50070',
                       user_name='hduser')
folder = os.path.abspath(os.curdir)


def _map():
    """"Разбиваем csv файл на строки"""
    with open('temp.csv', newline='') as File:
        reader = csv.reader(File)
        next(reader)
        for row in reader:
            yield row


def create_folder():

    """Создаем папки"""
    for folder in _map():
        hdfs.make_dir(folder[3])


def put_data():
    for data in _map():
        hdfs.create_file('{dir}/data.txt'.format(dir=data[3]), ",".join(data[:-1]))




