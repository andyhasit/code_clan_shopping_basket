
class Controller(object):
    """
    The main controller for the application.
    This is the only object the UI has a reference to (initially).
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
        This is where we set up 
        """
        basic_basket = BasicShoppingBasket()
        extended_basket = BasketWithDiscounts(basic_basket)
        extended_basket.add_price_adjuster()
        return extended_basket
        
class Product(object):
    """
    A product in the shop. Descriptions must be unique.
    """
    
    def __init__(self, description, price):
        
        self._description = description
        self._price = price
    
    @property
    def description(self):
        return self._description
    
    @property
    def price(self):
        return self._price
    
class BasicShoppingBasket(object):
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