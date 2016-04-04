"""
Simply runs the demo...
"""
from DemoRunner import DemoRunner

def run_demo():
    """
    This runs the whole demo, feel free to muck around with this.
    """
    runner = DemoRunner()
    basket = runner.basket
    apple = runner.controller.new_product('apple', 1.50)
    orange = runner.controller.new_product('orange', 2.00)
    banana = runner.controller.new_product('banana', 0.50)
    pear = runner.controller.new_product('pear', 1.00)
    
    runner.print_basket("Empty basket")
     
    basket.add_item(orange, 6)
    basket.add_item(orange, 6)
    runner.print_basket("There should be 12 oranges")
    
run_demo()
