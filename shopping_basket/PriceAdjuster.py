"""
Price Adjusters are used for adjusting the price of a shipping basket.

It is up to the caller to apply these in correct order to shopping baskets.
"""
class BasePriceAdjuster(object):
    """
    The basic implementation which other PriceAdjuster must follow.
    This one simply returns the previous total (i.e. does nothing)
    """
    
    def get_adjusted_price(self, previous_total, items):
        """
        previous_total: shopping basket total after previous adjustments
        items: list of ItemInBasket
        Returns a new total.
        """
        new_total = previous_total
        return new_total


