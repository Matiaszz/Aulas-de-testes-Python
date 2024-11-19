import requests


class Person:
    def __init__(self, name, surname, receive_data=False):
        self.name = name
        self.surname = surname
        self.receive_data = receive_data

    def receive_all_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if response.ok:
            self.receive_data = True
            return 'CONNECTED'

        self.receive_data = False
        return 'Error 404'
