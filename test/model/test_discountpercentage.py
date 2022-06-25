import unittest
from src.model.product import Product
from src.model.discount import DiscountPercentage

PRICE = 100
PRODUCT = "Test"


class DiscountPercentageTest(unittest.TestCase):

    def test_calculate_discount_10_per_cent(self):
        product = Product(PRICE, "DIS_10_PRODUCT", PRODUCT)

        discount = DiscountPercentage.calculate_discount(product)

        self.assertEqual(discount, 10)

    def test_calculate_discount_15_per_cent(self):
        product = Product(PRICE, "DIS_15_PRODUCT", PRODUCT)

        discount = DiscountPercentage.calculate_discount(product)

        self.assertEqual(discount, 15)
