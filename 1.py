''' Задание: необходимо написать SQL , который должен
 вывести уникальные строки для поля ID с максимальной датой или если даты одинаковые с максимальной value.'''
import sqlite3

base = sqlite3.connect('mts.db')
c = base.cursor()


def create_database():

    c.execute('create table if not exists MTS (ID INTEGER, Value INTEGER, Date DATE, )')
    c.execute('INSERT INTO MTS (ID, Value, Date) values (1,5,?)', ('2017-01-01',))
    c.execute('INSERT INTO MTS (id, Value, Date) values (1, 6,?)', ('2017-01-01',))
    c.execute('INSERT INTO MTS (id, Value, Date) values (2, 2,?)', ('2017-01-02',))
    c.execute('INSERT INTO MTS (id, Value, Date) values (3, 5, ?)', ('2017-05-06',))
    c.execute('INSERT INTO MTS (id, Value, Date) values (3, 6, ?)',  ('2017-06-06',))
    base.commit()


def result():
    return c.execute('select rowid, ID, max(Date), max(Value) from MTS GROUP BY id').fetchall()
#a = c.execute('select rowid FROM MTS WHERE Date=(SELECT MAX(Date) FROM MTS) AND Value = (SELECT MAX(Value) FROM MTS)').fetchall()


create_database()
pritn(result())