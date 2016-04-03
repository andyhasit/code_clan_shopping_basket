import pytest
from logic import * 

class TestMultibuyPriceAdjuster:
    
    def __test_bogof_multibuy(self):
        """
        PriceAdjuster 
        """
        apple = Product('apple', 2)
        lemon = Product('lemon', 1.50)
        orange = Product('orange', 1.50)
        bogof_citrus = MultibuyOffer(['lemon', 'orange'], 2, 1.50),
        three_apples_for_fiver = MultibuyOffer(['lemon', 'orange'], 2, 1.50),
        offers = [
            
        ]
        
    @pytest.fixture
    def items():
        apple = Product('apple', 2)
        orange = Product('orange', 2.50)
        lemon = Product('lemon', 1.50)
        items_in_basket = [
                ItemInBasket(apple, 3),
                ItemInBasket(orange, 2), 
                ItemInBasket(lemon, 4) 
                ]
        
        
    def test_bogof_multibuy(self, items):
        print items()
        #adjuster = MultibuyPriceAdjuster(offers)
        
        #adjuster.get_adjusted_price(self, previous_total, items())
    
        