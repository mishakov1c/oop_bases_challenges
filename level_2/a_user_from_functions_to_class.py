""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


class User:
    def make_username_capitalized(self, username: str):
        return username.capitalize()

    def generate_short_user_description(self, username: str, user_id: int, name: str):
        return f'User with id {user_id} has {username} username and {name} name'
