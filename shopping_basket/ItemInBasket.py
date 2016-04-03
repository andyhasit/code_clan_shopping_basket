
class ItemInBasket(object):
    """
    An item in a shopping basket.
    """
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity
    
    @property
    def description(self):
        return self._product.description
    
    @property
    def quantity(self):
        return self._quantity
        
    def update_quantity(self, new_quantity):
        self._quantity = new_quantity
        
    @property
    def total(self):
        return self._quantity * self._product.price