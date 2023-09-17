"""
У нас есть класс кредитного банковского аккаунта со свойсвами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    user_bank_account = BankAccount('Ivan Ivanov', 1000)
    user_bank_account.increase_balance(100)
    user_bank_account.decrease_balance(200)

    user_credit_account = CreditAccount('Ivan Ivanov', 500)
    user_credit_account.increase_balance(200)
    user_credit_account.decrease_balance(200)
    print(user_credit_account.is_eligible_for_credit())
