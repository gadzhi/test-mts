import json
import sqlite3


#открываем файл для чтения и создаем базу
file = open('1.json', 'r')
son = json.load(file)
base = sqlite3.connect('3.db')

#создаем таблицу
c = base.cursor()
c.execute('create table if not exists MTS (name varchar(50), tweet_text varchar(150), country_code varchar(5),'
          'display url VARCHAR(40), lang VARCHAR(6), created_at varchar(25), location VARCHAR(45), tweet_sentiment integer(25))')
base.commit()
#парсим файл json

data = son['data']


def write_data(data):
    # проходимся циклом
    for el in data:
        # если встречается удаленный твит, удаляем его из json файла
        if 'delete' in el:
            del el['delete']
        else:
            name = el['user']['name']
            tweet = el['text']
            lang = el['user']['lang']
            location = el['user']['location']
    #        country = el['retweeted_status']['place']['country_code']
            create = el['created_at']


            c.execute("INSERT INTO MTS "
                      "(name,created_at,tweet_text, lang, location, tweet_sentiment) "
                      "values (?,?,?,?,?, 0);", (name, create, tweet, lang, location))

            base.commit()


def sentiments():

    ''' Разбиваем наш текстовый файл в ключ:значение. Ключом будет у нас слово '''

    d = {}
    with open("AFINN-111.txt", encoding='utf-8') as f:
        for line in f:
            (key, val) = line.split('\t')
            d[key] = val
    #Проходимся циклом по базе и разбиваем сообщение на слова
    a = c.execute('SELECT tweet_text FROM MTS').fetchall()
    rowid = 1
    for title in a:

        z = title[0].split()

        for emotion in z:
            # если есть
            if emotion in d.keys():

                value = d[emotion]

                c.execute('UPDATE MTS SET tweet_sentiment = tweet_sentiment + (?) where rowid = ?; ', (int(value), rowid))
                base.commit()
            else:
                pass
        rowid += 1


def user():
     lucky = c.execute('SELECT name FROM MTS WHERE tweet_sentiment = (select MAX(tweet_sentiment) from MTS)').fetchone()
     unlucky = c.execute('SELECT name FROM MTS WHERE tweet_sentiment = (select MIN(tweet_sentiment) from MTS)').fetchone()

     return ("Самая счастливый юзер: " + str(lucky[0]) + "\nСамая несчастливая: " + str(unlucky[0]))


def country():
    '''
    Поиск самой счастливой страны
    '''

    a = c.execute('SELECT SUM(tweet_sentiment) AS result FROM MTS GROUP BY lang ').fetchall()
    lucky_v = int(max(a)[0])
    unlucky_v = int(min(a)[0])

    lucky = c.execute('SELECT lang, SUM(tweet_sentiment) AS result FROM MTS GROUP BY lang  '
                     'HAVING result >= {value};'.format(value=lucky_v)).fetchall()
    unlucky = c.execute('SELECT lang, SUM(tweet_sentiment) AS result FROM MTS GROUP BY lang  '
                     'HAVING result <= {value};'.format(value=unlucky_v)).fetchall()

    return ("Самая счастливая страна: " + str(lucky) + "\nСамая несчастливая: " + str(unlucky))

print(write_data(data))
print(sentiments())

print(user())
print(country())



