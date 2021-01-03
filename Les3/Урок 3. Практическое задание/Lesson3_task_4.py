"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4


def get_hash(url, salt_):
    res = hashlib.sha256(salt_.encode('utf-8') + url.encode('utf-8')).hexdigest()
    return res


def get_link(url, list_hash, salt_):
    if get_hash(url, salt_) not in link_hash:
        print('Новый url добавлен')
        list_hash.append(get_hash(url, salt_))
    else:
        print('Указанный url есть в списке')
    return print(list_hash)


user_salt = uuid4().hex
link_hash = []
link = ['rbc.ru', 'rambler.ru', 'mfd.ru', 'forexpf.ru', 'госуслуги.рф']
for el in link:
    link_hash.append(get_hash(el, user_salt))
user_link = input('Введите url: ')
get_link(user_link, link_hash, user_salt)
