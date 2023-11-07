
from urllib.request import urlopen

def add_sales_tax(original_amount, country, region):
    sales_tax_rate = urlopen(
        f"https://tax-api.com/{country}/{region}"
        ).read().decode()
    return original_amount * float(sales_tax_rate)


"""
TEST FOR add_sales_tax
"""

import io
import unittest
from unittest import mock

class SalesTaxTestCase(unittest.TestCase):
    @mock.patch('test_tax.urlopen')
    def test_get_sales_tax_returns_proper_value_from_api(
        self,
        mock_urlopen
    ):
        test_tax_rate = 1.06
        mock_urlopen.return_value = io.BytesIO(
            str(test_tax_rate).encode("utf-8")
        )

        self.assertEqual(
            5 * test_tax_rate,
            add_sales_tax(5, 'USA', 'MI')
        )
