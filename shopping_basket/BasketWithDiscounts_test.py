import pytest
from logic import * 


class PriceAdjusterAddFifty:
    
    def get_adjusted_price(self, previous_total, items):
        return previous_total + (previous_total / 2)
    
class PriceAdjusterFreeLemons:
    
    def get_adjusted_price(self, previous_total, items):
        total = previous_total
        for item in items:
            if item.description == "lemon":
                total -= item.total  
        return total
    
class TestBasketWithDiscount:
    
    def test_without_adjusters(self):
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.total == 4 + 6
      
    def test_with_one_adjuster(self):
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_price_adjuster(PriceAdjusterAddFifty())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.total == 15
          
    def test_with_two_adjusters(self):
        apple = Product('apple', 2)
        lemon = Product('lemon', 3)
        basket = BasketWithDiscounts(BasicBasket())
        basket.add_price_adjuster(PriceAdjusterFreeLemons())
        basket.add_price_adjuster(PriceAdjusterAddFifty())
        basket.add_item(apple, 2)
        basket.add_item(lemon, 2)
        assert basket.total == 4
        