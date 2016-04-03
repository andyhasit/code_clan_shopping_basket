from logic import *

class TestItemInBasket():
    
    def test_total(self):
        apple = Product('apple', 1.50)
        item_in_basket = ItemInBasket(apple, 2)
        assert item_in_basket.total == 3.0
        item_in_basket.update_quantity(3)
        assert item_in_basket.total == 4.5