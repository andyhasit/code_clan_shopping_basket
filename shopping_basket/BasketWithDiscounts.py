"""
This is a shopping basket that allos the applying of discounts
 
I implemented this as separate to BasicBasket and used object composition
instead of inheritance, i.e. it uses an "inner basket" instead of subclassing
BasicShoppingBasket.

Advantages:
    
    It's asier to test. We can pass it a mock inner basket with just the basic 
    functionality needed to test the calculation of totals.
    
    In production we can pass an inner basket which persists changes to the 
    database, and still trust it will behave the same.
    
    We can build other types of shopping basket which use an inner basket without
    affecting this one
    
All of the above would be difficult if we implemented the discount calculations
in the same class as BasicBasket, or inherited from it.

"""

class BasketWithDiscounts(object):
    """
    A shopping which allows adding of price adjusters, which may be discounts.
    """
    
    def __init__(self, inner_basket):
        """
        inner_basket must be an implementation of BasicBasket.
        """
        self._basket = inner_basket
        self._price_adjusters
        
    def add_price_adjuster(self, price_adjuster):
        """
        price_adjuster must be an implementation of PriceAdjuster.
        Price adjusters will be applied when caculating the total in the order
        they were added here. Caller is responsible for ensuring correct order.
        """
    
    @property
    def total(self):
        initial_total = self._basket.total
        
        
        
        