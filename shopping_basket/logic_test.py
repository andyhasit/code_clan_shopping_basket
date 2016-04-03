from logic import * 

def test_add_one_item():
    apple = Product('apple', 2)
    orange = Product('orange', 2.50)
    basket = BasicShoppingBasket()
    basket.add_item(apple, 4)
    items = basket.get_items()
    assert len(items) == 1
    item = items[0]
    assert item.description == 'apple'
    assert item.quantity == 4
    
def test_add_two_different_items():
    apple = Product('apple', 2)
    orange = Product('orange', 2.50)
    basket = BasicShoppingBasket()
    basket.add_item(apple, 4)
    basket.add_item(orange, 6)
    items = basket.get_items()
    assert len(items) == 2
    item = items[0]
    assert item.description == 'apple'
    assert item.quantity == 4
    item = items[1]
    assert item.description == 'orange'
    assert item.quantity == 6
    
def test_add_two_same_items_increments_quantity():
    apple = Product('apple', 2)
    orange = Product('orange', 2.50)
    basket = BasicShoppingBasket()
    basket.add_item(apple, 4)
    basket.add_item(orange, 6)
    basket.add_item(apple, 6)
    items = basket.get_items()
    assert len(items) == 2
    item = items[0]
    assert item.description == 'apple'
    assert item.quantity == 10
    item = items[1]
    assert item.description == 'orange'
    assert item.quantity == 6
    