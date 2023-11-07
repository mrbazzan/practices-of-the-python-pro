
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

class ShoppingCartTestCase(unittest.TestCase):
    def test_and_remove_product(self):
        xl_black_shoes = Product("shoes", "XL", "black")
        shoe_cart = ShoppingCart()

        self.assertEqual(shoe_cart.products, {})

        shoe_cart.add_product(xl_black_shoes)
        self.assertEqual(
            len(shoe_cart.products),
            1
        )

        shoe_cart.remove_product(xl_black_shoes)
        self.assertEqual(shoe_cart.products, {})
