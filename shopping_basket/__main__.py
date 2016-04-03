from logic import *

COLUMNS = ('item', 'qty', 'unit', 'total')
PADDING_VALUES = (20, 8, 8, 8)

def table_line(items, padding_values):
    padded_strings = []
    for i, s in enumerate(items):
        padding_value = padding_values[i]
        padded_strings.append('{:<{}s}'.format(s, padding_value))
    return "|   ".join(padded_strings)

def print_basket(basket, message):
    print "---------------------------------------"
    print message
    print ""
    print table_line(COLUMNS, PADDING_VALUES)
    for item in basket.items:
        print table_line((
            item.description, 
            item.quantity, 
            item.unit_price, 
            item.total), 
            PADDING_VALUES)
    print ""
    print "Gross:{}".format(basket.total)
    print "Gross:{}".format(basket.total)
    
def run_demo():
    """
    This is just a sequential run through showing the features.
    """
    controller = Controller()
    apple = controller.new_product('apple', 1.50)
    orange = controller.new_product('orange', 2.00)
    banana = controller.new_product('banana', 0.50)
    pear = controller.new_product('pear', 1.00)
    
    # Create a bogof offer on apples
    bogof_apple_offer = MultibuyOffer(['apple'], 2, 1.50)
    
    # Create a generic multi-buy price adjuster
    multi_buy_price_adjuster = MultibuyPriceAdjuster()
    
    # Add the  bogof offer on apples
    multi_buy_price_adjuster.add_offer(bogof_apple_offer)
    # We could add more offers here, like buy 3 for 2.50 etc..
    
    # Create 10% off for value over 20 adjuster
    ten_percent_off_on_orders_over_twenty = PercentagePriceAdjuster(10, 20)
    
    # Create a user discount adjuster at 2%
    user_loyalty_discount = PercentagePriceAdjuster(2, 0)
    
    # Create our basket
    basket = controller.new_basket()
    
    # Add the price adjusters in the order we want them applied
    basket.add_price_adjuster(multi_buy_price_adjuster)
    basket.add_price_adjuster(ten_percent_off_on_orders_over_twenty)
    basket.add_price_adjuster(user_loyalty_discount)
    
    print_basket(basket, "Empty basket")
    #basket.add_item(

if __name__ == "__main__":
    run_demo()
