"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
from uuid import uuid4


def get_hash(psw, salt_):
    res = hashlib.sha256(salt_.encode('utf-8') + psw.encode('utf-8')).hexdigest()
    print('хэш введенного пароля = ', res)
    return res


user_salt = uuid4().hex
user_password = input('Введите пароль: ')
user_password_hash = get_hash(user_password, user_salt)
user_password = input('Введите повторно пароль для проверки: ')
if get_hash(user_password, user_salt) == user_password_hash:
    print('Пароль принят')
else:
    print('Пароли не совпадают')
