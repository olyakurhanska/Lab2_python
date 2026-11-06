
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс має бути числом")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.__balance = value

    @property
    def balance_with_bonus(self):
        return self.__balance * 1.05


account = BankAccount("Ольга", 2350)

print("Власник:", account._owner)
print("Баланс:", account.balance, "грн")
print("Баланс із бонусом:", account.balance_with_bonus, "грн")

account.balance = 3100
print("\nНовий баланс:", account.balance, "грн")
print("Новий баланс із бонусом:", account.balance_with_bonus, "грн")

try:
    account.balance = -200
except ValueError as error:
    print("\nПомилка:", error)

try:
    account.balance = "три тисячі"
except TypeError as error:
    print("Помилка:", error)

try:
    print(account.__balance)
except AttributeError:
    print("Прямий доступ до приватного атрибута заборонено")

print("Доступ через name mangling:", account._BankAccount__balance)
