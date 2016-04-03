"""
This is basic shopping backet which just allows adding and removing of items.
Functionality for apply discounts don't belong in here.
See BasketWithDiscounts.
"""

from ItemInBasket import ItemInBasket

class BasicBasket(object):
    """
    A basic shopping backet which allows adding and removing of items.
    Each product is only listed once, if added again, quantity is updated.
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
        Note: this is a copy, so manipulating the returned list has no effect on
        the shopping basket.
        """
        return self._items[:]
    
    def remove_item(self, item_in_basket):
        self._items.remove(item_in_basket)
        
    def empty(self):
        """
        Empties the list.
        Note: retains the same list object, in case that ends up being tracked
        elsewhere (e.g UI databinding)
        """
        del self._items[:]
            
    def get_item_in_basket(self, product):
        """
        Returns the entry for the specified product, or None.
        """
        matcher = (x for x in self._items if x.description == product.description)
        return next(matcher, None)
    
    @property
    def total(self):
        running_total = 0
        for item_in_basket in self._items:
            running_total += item_in_basket.total
        return running_total