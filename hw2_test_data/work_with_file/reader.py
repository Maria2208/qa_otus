from csv import DictReader
from json import loads
from json import dumps


class Reader:

    def read_books(self, path='../data/books.csv'):
        with open(path, 'r') as file:
            """читаем файл и создаем коллекцию пользователей с нужными ключами-значениями"""
            reader = DictReader(file)
            books = []
            for item in reader:
                books.append({"title": item["Title"], "author": item["Author"], "height": item["Height"]})
            return books

    def read_users(self, path='../data/users.json'):
        """читаем файл и создаем коллекцию книг с нужными ключами-значениями"""
        with open(path, 'r') as f:
            file = f.read()
            users_dict = loads(file)
            users = []
            for item in users_dict:
                users.append({"name": item["name"], "gender": item["gender"], "address": item["address"]})
            return users


class Writer(Reader):
    reader = Reader()
    books = reader.read_books(path='../data/books.csv')
    users = reader.read_users(path='../data/users.json')
    i = 1
    for i in range(0, len(users)):
        user = users[i]
        if i < len(books):
            book = books[i]
            user['books'] = [book]
        else:
            user['books'] = []
    i += 1
    with open('./result.json', 'w') as f:
        s = dumps(users, indent=4)
        f.write(s)
