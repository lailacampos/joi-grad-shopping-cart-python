from abc import ABC, abstractmethod


class Discount(ABC):

    @staticmethod
    @abstractmethod
    def calculate_discount(product):
        pass


class DiscountPercentage(Discount):

    @staticmethod
    def calculate_discount(product):
        if product.product_code.startswith("DIS_10"):
            return DiscountPercentage.calculate_10_per_cent_discount(product)

        elif product.product_code.startswith("DIS_15"):
            return DiscountPercentage.calculate_15_per_cent_discount(product)

        else:
            return 0.00

    @staticmethod
    def calculate_10_per_cent_discount(product):
        discount = product.price * 0.1
        return discount

    @staticmethod
    def calculate_15_per_cent_discount(product):
        discount = product.price * 0.15
        return discount


class DiscountBuyXTakeY(Discount):

    @staticmethod
    @abstractmethod
    def calculate_discount(product):
        pass
