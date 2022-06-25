from src.model.discount import DiscountPercentage


class PriceCalculator:

    @staticmethod
    def calculate_price_single_product_percentage_discount(product):
        final_price = product.price - DiscountPercentage.calculate_discount(product)
        return final_price
