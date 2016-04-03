

class Product(object):
    """
    A product in the shop.
    """
    def __init__(self, description, price):
        self.description = description
        self.price = description
    
    
class BasicShoppingBasket(object):
    """
    A basic shopping backet which allows adding and removing of items.
    """
    
    def __init__(self):
        self._items = []
    
    def add_item(self, product, quantity):
        """
        Adds an entry in the basket, or increments the quantity if the product
        is already in the basket.
        """
        existing_entry_for_product = self.get_item_in_basket(product)
        if existing_entry_for_product:
            new_quantity = existing_entry_for_product.quantity + quantity
            existing_entry_for_product.update_quantity(new_quantity)
        else:
            self._items.append(ItemInBasket(product, quantity))
        
    def get_items(self):
        """
        Returns a list of the items.
        Note this is a copy, so manilpulating the returned list has no effect on
        the shopping basket.
        """
        return [i for i in self._items]
        
    def get_item_in_basket(self, product):
        """
        
        """
        
class ItemInBasket(object):
    """
    An item  in the shopping basket.
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