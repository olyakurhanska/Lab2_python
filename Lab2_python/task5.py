
class RegularDiscount:
    def calculate(self, price):
        return price


class StudentDiscount:
    def calculate(self, price):
        return price * 0.9


class HolidayDiscount:
    def calculate(self, price):
        return price * 0.8


class BirthdayDiscount:
    def calculate(self, price):
        return price * 0.85


class Shop:
    def __init__(self, discount):
        self.discount = discount

    def final_price(self, price):
        return self.discount.calculate(price)


price = 1350

discounts = [
    ("Без знижки", RegularDiscount()),
    ("Студентська знижка", StudentDiscount()),
    ("Святкова знижка", HolidayDiscount()),
    ("Знижка на день народження", BirthdayDiscount())
]

for name, discount in discounts:
    shop = Shop(discount)
    print(name, ":", round(shop.final_price(price), 2), "грн")
