class LoyaltyPointsHandler:

    @staticmethod
    def calculate_loyalty_points_earned(product):
        if product.product_code.startswith("DIS_10"):
            return LoyaltyPointsHandler.earn_loyalty_points_with_DIS_10_code(product)

        elif product.product_code.startswith("DIS_15"):
            return LoyaltyPointsHandler.earn_loyalty_points_with_DIS_15_code(product)

        else:
            return LoyaltyPointsHandler.earn_loyalty_points_with_no_discount(product)

    @staticmethod
    def earn_loyalty_points_with_no_discount(product):
        loyalty_points_earned = product.price / 5
        return loyalty_points_earned

    @staticmethod
    def earn_loyalty_points_with_DIS_10_code(product):
        loyalty_points_earned = product.price / 10
        return loyalty_points_earned

    @staticmethod
    def earn_loyalty_points_with_DIS_15_code(product):
        loyalty_points_earned = product.price / 15
        return loyalty_points_earned
