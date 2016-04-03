import pytest
from logic import * 

class TestMultibuyPriceAdjuster:
    
    def test_without_adjusters(self):
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        offers = [
            MultibuyOffer()
        ]
        adjuster = MultibuyPriceAdjuster()
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.total == 4 + 6
        