"""
.. moduleauthor:: Adam Gagorik <adam.gagorik@gmail.com>
"""
from pydarkstar.tables.auction_house import AuctionHouse
import pydarkstar.auction.auctionbase
import pydarkstar.timeutils
import pydarkstar.database
import pydarkstar.item

class Seller(pydarkstar.auction.auctionbase.AuctionBase):
    """
    Buyer/Seller

    :param db: database object
    :param seller: auction house seller id
    :param seller_name: auction house seller name
    """
    def __init__(self, db, seller=0, seller_name='Zissou', *args, **kwargs):
        super(Seller, self).__init__(db, *args, **kwargs)
        self.seller = int(seller)
        self.seller_name = str(seller_name)

    def setHistory(self, itemid, stack, price, date, count=1):
        """
        Set the history of a particular item.

        :param itemid: item number
        :param stack: stack 0|1
        :param date: timestamp
        :param price: price
        :param count: rows
        """
        with pydarkstar.logutils.capture():
            itemid = self._validate_itemid(itemid)
            stack  = self._validate_stack(stack)
            price  = self._validate_price(price)
            date   = self._validate_date(date)

            # add row
            with self.scopped_session() as session:

                # add the item multiple times
                for i in range(count):

                    row = AuctionHouse(
                        itemid      = itemid,
                        stack       = stack,
                        seller      = self.seller,
                        seller_name = self.seller_name,
                        date        = date,
                        price       = price,
                        buyer_name  = self.seller_name,
                        sale        = price,
                        sell_date   = date,
                    )

                    session.add(row)

if __name__ == '__main__':
    pass