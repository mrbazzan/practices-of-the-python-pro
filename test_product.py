
import unittest
from product import Product
from cart import ShoppingCart

class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product("shoes", "S", "black")
        expected_value = "SHOES"
        self.assertEqual(
            expected_value,
            small_black_shoes.transform_name_for_sku()
        )
