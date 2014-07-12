from unittest import TestCase
from currencies import Currency


class TestCurrency(TestCase):
    def test_get_money_currency(self):
        currency = Currency('USD')

        self.assertIsInstance(currency.get_money_currency(), str)
        self.assertEqual(currency.get_money_currency(), 'USD')

    def test_get_currency_formats(self):
        currency_formats = Currency.get_currency_formats()

        self.assertIsNotNone(currency_formats)
        self.assertIsInstance(currency_formats, list)
        self.assertGreater(len(currency_formats), 0)