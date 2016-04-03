from logic import * 


def test_add_one_item():
    apple = Product('apple', 2)
    orange = Product('orange', 2.50)
    basket = BasicShoppingBasket()
    basket.add_item(apple, 4)
    items = basket.get_items()
    assert len(items) == 1
    item1 = items[0]
    assert item1.description == 'apple'
    assert item1.quantity == 4
    
    
    