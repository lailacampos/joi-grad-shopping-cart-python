import unittest
from src.model.loyaltypointshandler import LoyaltyPointsHandler
from src.model.product import Product

PRODUCT_PRICE = 100
PRODUCT = "Test"


class LoyaltyPointsHandlerTest(unittest.TestCase):

    def test_earn_loyalty_points_with_no_discount(self):
        product = Product(PRODUCT_PRICE, "", PRODUCT)
        loyalty_points_earned = LoyaltyPointsHandler.earn_loyalty_points_with_no_discount(product)

        self.assertEqual(loyalty_points_earned, 20)

    def test_earn_loyalty_points_with_DIS_10_code(self):
        product = Product(PRODUCT_PRICE, "DIS_10_PRODUCT", PRODUCT)
        loyalty_points_earned = LoyaltyPointsHandler.earn_loyalty_points_with_DIS_10_code(product)

        self.assertEqual(loyalty_points_earned, 10)

    def test_earn_loyalty_points_with_DIS_15_code(self):
        product = Product(150, "DIS_15_PRODUCT", PRODUCT)
        loyalty_points_earned = LoyaltyPointsHandler.earn_loyalty_points_with_DIS_15_code(product)

        self.assertEqual(loyalty_points_earned, 10)
