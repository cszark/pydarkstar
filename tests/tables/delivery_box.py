import unittest
import pydarkstar.logutils
import pydarkstar.tables.deliverybox

pydarkstar.logutils.setDebug()

class TestCase(unittest.TestCase):
    def test_init(self):
        row = pydarkstar.tables.deliverybox.DeliveryBox()
        pydarkstar.logutils.logging.debug(row)

if __name__ == '__main__':
    unittest.main()