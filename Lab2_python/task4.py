
from abc import ABC, abstractmethod


class Delivery(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate_price(self, distance):
        pass

    @abstractmethod
    def deliver(self):
        pass

    def info(self):
        return f"Спосіб доставки: {self.name}"


class CourierDelivery(Delivery):
    @property
    def name(self):
        return "Кур'єр"

    def calculate_price(self, distance):
        return 45 + distance * 12

    def deliver(self):
        return "Кур'єр доставляє замовлення"


class PostDelivery(Delivery):
    @property
    def name(self):
        return "Пошта"

    def calculate_price(self, distance):
        return 35 + distance * 4

    def deliver(self):
        return "Посилка передана поштовій службі"


class Order:
    def __init__(self, number, delivery):
        self.number = number
        self.delivery = delivery

    def show_order(self, distance):
        print("Замовлення:", self.number)
        print(self.delivery.info())
        print("Вартість:", self.delivery.calculate_price(distance), "грн")
        print(self.delivery.deliver())


try:
    delivery = Delivery()
except TypeError:
    print("Не можна створити об'єкт абстрактного класу")

deliveries = [
    CourierDelivery(),
    PostDelivery()
]

for delivery in deliveries:
    order = Order(238, delivery)
    order.show_order(7)
    print()
