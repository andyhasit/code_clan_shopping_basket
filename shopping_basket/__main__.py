"""
A shopping basket demo application for CodeClan.

App runs as a mini demo to show it works.
To see what actually all works you're best checking the test files.

"""
from logic import *
from DemoRunner import DemoRunner

def run_demo():
    """
    This runs the quick demo, feel free to muck around with this.
    This isn't structured code, just a playground :-)
    """
    demo = DemoRunner()
    basket = demo.basket
    apple = demo.controller.new_product('apple', 1.50)
    orange = demo.controller.new_product('orange', 2.00)
    banana = demo.controller.new_product('banana', 0.50)
    pear = demo.controller.new_product('pear', 1.00)
    
    # Create a bogof offer on apples    
    bogof_apple_offer = MultibuyOffer(['apple'], 2, apple.price)
    demo.add_offer(bogof_apple_offer)
    """
    We could add more offers here, like buy 3 for 2:
    three_apples_for_two = MultibuyOffer(['apple'], 3, apple.price * 2)
    Or 4 for 3 pounds
    four_apples_for_three_pounds = MultibuyOffer(['apple'], 4, 3.00)
    """
    
    # Create 10% off for value over 20 adjuster
    ten_percent_off_on_orders_over_twenty = PercentagePriceAdjuster(10, 20)
    demo.add_percentage_discount(ten_percent_off_on_orders_over_twenty)
    
    # Create a user discount adjuster at 2%
    user_loyalty_discount = PercentagePriceAdjuster(2, 0)
    demo.add_percentage_discount(user_loyalty_discount)
        
    # Tell demo to setup discounts
    demo.setup_discounts()
    
    # Add & remove & show basic 2% discount
    basket.add_item(pear, 10)
    apple_entry = basket.add_item(apple, 100)
    basket.remove_item(apple_entry)
    demo.print_basket("10 pears, with 2% discount")
    basket.empty()
    
    # Adding multiple items of same type consolidates values
    # 10% discount applied as we reached threshold of 20
    basket.add_item(orange, 6)
    basket.add_item(orange, 6)
    demo.print_basket("12 oranges, with 10% then 2% discount (21.168)")
    basket.empty()
    
    # Adding items with bogof
    basket.add_item(apple, 5)
    demo.print_basket("5 apples at 1.50, 2 cancelled out = 4.50, then 2%")
    basket.empty()
    
run_demo()
