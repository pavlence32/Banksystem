from exceptions import InvalidBalanceError, NegativeBalanceError, NotEnoughMoneyError, NegativeError


class Account:
    number = 100000

    def __init__(self, owner, balance: float):
        if not isinstance(balance, (int, float)):
            raise InvalidBalanceError("Неверная инициализация баланс")
        self.number = Account.number
        Account.number += 1
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise NegativeError("Сумма должна быть числом")
        elif amount <= 0:
            raise NegativeError("Сумма должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise NegativeError("Сумма должна быть числом")
        elif self._balance-amount < 0:
            raise NegativeBalanceError("Недостаточно средств для снятия")
        self._balance -= amount

    def transfer(self, recipient, amount):
        if not isinstance(amount, (int, float)):
            raise NegativeError("Сумма должна быть числом")
        elif self._balance-amount < 0:
            raise NegativeBalanceError("Недостаточно средств для перевода")
        recipient.deposit(amount)
        self.withdraw(amount)

    def __str__(self):
        return (
            f"Счет №{self.number}\n"
            f"Владелец: {self.owner.name}\n"
            f"Баланс: {self._balance}"
        )

    @property
    def balance(self):
        return self._balance
