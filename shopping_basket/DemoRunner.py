from logic import *
from DemoHelper import DemoHelper

class DemoRunner(object):
    """
    Sets up the demo runner with discounts.
    """

    def __init__(self):
        self._helper = DemoHelper()
        self.controller = Controller()
        self.basket = self.controller.new_basket()
        self._offers = []
        self._percentage_discounts = []
        
    def add_offer(self, offer):
         self._offers.append(offer)
        
    def add_percentage_discount(self, percentage_discount):
         self._percentage_discounts.append(percentage_discount)
    
    def setup_discounts(self):
        """
        Sets up the multibuy discount, then percentage discounts in the order
        they were added.
        """
        self._setup_multibuy_discount()
        self._setup_percentage_discounts()
        
    def _setup_multibuy_discount(self):
        """
        Adds a multi-buy price adjusters to the basket, with all the offers
        (e.g. bogof on oranges)
        """
        multi_buy_price_adjuster = MultibuyPriceAdjuster()
        for offer in self._offers:
            multi_buy_price_adjuster.add_offer(offer)
        self.basket.add_price_adjuster(multi_buy_price_adjuster)
        
    def _setup_percentage_discounts(self):
        """
        Adds the percentage price adjusters to the basket.
        """
        for percentage_discount in self._percentage_discounts:            
            self.basket.add_price_adjuster(percentage_discount)
          
    def print_basket(self, msg):
        """
        Just for convenience.
        """
        self._helper.print_basket(self.basket, msg)
        