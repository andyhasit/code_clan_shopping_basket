from Product import Product
from BasicShoppingBasket import BasicShoppingBasket

class Controller(object):
    """
    The main controller for the application.
    This is the only object the UI has a reference to (initially).
    It ensures new products have unique descriptions (currently products can 
    only be added, not edited or removed)
    """
    def __init__(self):
        self._products = []
        self._used_descriptions = []
        self._unique_desc_error_message = \
                "Description ${0} is already claimed by an other product"
        
    def get_products(self):
        return self._products[:]
    
    def new_product(self, description, price):
        if description in self._used_descriptions:
            raise ValueError(self._unique_desc_error_message.format(description))
        self._used_descriptions.append(description)
        self._products.append(Product(description, price))
        
    def new_basket(self, name):
        """
        Returns a new shopping basket.
        This is where we set up the discounts for a basket.
        """
        basic_basket = BasicShoppingBasket()
        extended_basket = BasketWithDiscounts(basic_basket)
        extended_basket.add_price_adjuster()
        return extended_basket