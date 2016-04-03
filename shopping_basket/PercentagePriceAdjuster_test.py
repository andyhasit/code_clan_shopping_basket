import pytest
from logic import * 

class TestPercentagePriceAdjuster:
    
        
    @pytest.fixture
    def items(self):
        apple = Product('apple', 2)
        orange = Product('orange', 1.50)
        lemon = Product('lemon', 1.50)
        grapefruit = Product('grapefruit', 1.25)
        return [
                ItemInBasket(apple, 3),
                ItemInBasket(orange, 2), 
                ItemInBasket(lemon, 4), 
                ItemInBasket(grapefruit, 1)
                ]
        
    def normal_total(self, items):
        return sum([x.total for x in items])
        
    def test_percentage_normally(self, items):
        apple = Product('apple', 2)
        orange = Product('orange', 3)
        
        adjuster = Perc()
        assert adjuster.get_adjusted_price(25, items) == 25
        assert adjuster.get_adjusted_price(37, items) == 37