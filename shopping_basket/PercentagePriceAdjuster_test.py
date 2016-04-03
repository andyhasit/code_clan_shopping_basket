import pytest
from logic import * 

class TestPercentagePriceAdjuster:
            
    def test_percentage_normally(self):
        adjuster = PercentagePriceAdjuster(10)
        assert adjuster.get_adjusted_price(25, []) == 22.5
        