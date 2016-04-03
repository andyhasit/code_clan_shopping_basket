"""

A MultibuyPriceAdjuster allows for multibuy offers, which could be:
        buy one get one free
        buy two for the price of three
        buy three for 2.50

Place all the offers available in one MultibuyPriceAdjuster, so it can raise an 
Exception if an item is included in multiple offers (which you wouldn't want)

This is more flexible than a plain buy-one-get-one-free adjuster.

For MultibuyOffer you specify quantity and final price for that quantity, 
which is better than specifying a discoutn, as it allow x qty for x pounds type
offers.

The MultibuyOffer objects are responsible for calculating the total for all items
included (e.g bogof with 3 apples, the third apple is charged std price). This
keeps the MultibuyPriceAdjuster simple, and allows more complex offers in the 
future. (open/closed principle)


"""

class MultibuyPriceAdjuster(object):
    """
    Adjusts the price for buy-one-get-one-free offers.
    """
    
    def __init__(self, offers):
        """
        offers: list of all the multi-buy offers to apply.
        """
        self._offers = _offers[:]
        
    def get_adjusted_price(self, previous_total, items):
        total = previous_total
        for item in items:
            if self.item_will_be_included_in_an_offer(item):
                self._include_item_in_offer(item)
            else:
                total += item.total
        for offer in self._offers:
            total += offer.total_value_of_items
        return total
          
    def item_will_be_included_in_an_offer(self, item):
        """
        Tests whether an item will be included in an offer.
        """
        for offer in self._offers:
            if offer.is_item_included(item):
                return true
        return false
    
    def _include_item_in_offer(self, item):
        """
        Adds the item to an offer.
        """
        matching_offer = None
        for offer in self._offers:
            if offer.is_item_included(item):
                if first_matching_offer is None:
                    matching_offer = offer
                else:
                    raise MoreThanOneMatchingOfferException(matching_offer, 
                        matching_offer, offer)
        matching_offer.include_item(item)

    
class MultibuyOffer(object):
    """
    A multi-buy offer, which could be:
        buy one get one free
        buy two for the price of three
        etc...
    """
    
    def __init__(self, descriptions, quantity, price_for_that_quantity):
        """
        descriptions: the descriptions to which the offer applies.
        quantity: the quantity of items that must be present in order to apply
        the adjustment
        price_for_that_quantity: the price for that quantity.
        
        If apples cost 3.5 and you want a bogof, set:
            quantity=2
            price_for_that_quantity=3.5
        """
        self._descriptions = descriptions[:]
    
    def is_item_included(self, item):
        pass
    
    def include_item(self, item):
        pass
    

class MoreThanOneMatchingOfferException(BaseException):
    
    def __init__(self, item, offer1, offer2):
        msg = "Item ${0} is covered by multiple multibuy offers: ${1}, ${2}"
        self.message =  msg.format(item.description, offer1, offer2)
        
