import pytest
from logic import * 

class TestBasketWithDiscount:
    
    def test_s(self):
        inner_basket = BasicBasket()
        basket = BasketWithDiscounts(inner_basket)
        basket.add_price_adjuster()
        