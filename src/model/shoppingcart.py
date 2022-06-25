from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order
from src.model.loyaltypointshandler import LoyaltyPointsHandler
from src.model.pricecalculator import PriceCalculator


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        for product in self.products:
            loyalty_points_earned += LoyaltyPointsHandler.calculate_loyalty_points_earned(product)
            total_price += PriceCalculator.calculate_price_single_product_percentage_discount(product)
        return Order(int(loyalty_points_earned), total_price)

    def __str__(self):
        product_list = "".join('%s'%product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
