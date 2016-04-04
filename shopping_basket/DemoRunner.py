from logic import *
from DemoHelper import DemoHelper

class DemoRunner(object):
    """
    Sets up the demo runner with discounts as per instructions.
    
    """

    def __init__(self):
        self._helper = DemoHelper()
        self.controller = Controller()
        self.basket = self.controller.new_basket()
        self.setup_discounts()
        
    def setup_discounts(self):
        # Create a bogof offer on apples
        bogof_apple_offer = MultibuyOffer(['apple'], 2, 1.50)
        
        # Create a generic multi-buy price adjuster
        multi_buy_price_adjuster = MultibuyPriceAdjuster()
        
        # Add the  bogof offer on apples
        multi_buy_price_adjuster.add_offer(bogof_apple_offer)
        # We could add more offers here, like buy 3 for 2.50 etc..
        
        # Create 10% off for value over 20 adjuster
        ten_percent_off_on_orders_over_twenty = PercentagePriceAdjuster(10, 20)
        
        # Create a user discount adjuster at 2%
        user_loyalty_discount = PercentagePriceAdjuster(2, 0)
        
        # Add the price adjusters in the order we want them applied
        self.basket.add_price_adjuster(multi_buy_price_adjuster)
        self.basket.add_price_adjuster(ten_percent_off_on_orders_over_twenty)
        self.basket.add_price_adjuster(user_loyalty_discount)
          
    def print_basket(self, msg):
        """
        Just for convenience.
        """
        self._helper.print_basket(self.basket, msg)
        