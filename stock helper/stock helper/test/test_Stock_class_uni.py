"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - test_Stock_class_uni.py
unittest for Stock class
"""
from unittest import TestCase
from models.Final_stock_class import Stock



class Stock_test(TestCase):


    def test_init_(self):
        stock = Stock("AAPL", "2023-01-05", "day")
        self.assertEqual(stock.stock_name, "AAPL")
        self.assertEqual(stock.from_time, "2023-01-05")
        self.assertEqual(stock.to_time, "2023-01-05")
        self.assertEqual(stock.open_price, 127.13)
        self.assertEqual(stock.close_price, 125.02)
        self.assertEqual(stock.high_value, 127.77)
        self.assertEqual(stock.low_value, 124.76)


    def test_get_profit_rate(self):
        stock = Stock("AAPL", "2023-01-05", "day")
        profit_rate = stock.get_profit_rate()
        self.assertEqual(profit_rate, -1.66)

    def test_wrong_input_stock_name_int(self):
        with self.assertRaises(TypeError):
            stock = Stock(1, "2023-01-05", "day")

    def test_wrong_input_date_int(self):
        with self.assertRaises(TypeError):
            stock = Stock("AAPL", 1, "day")

    def test_wrong_input_time_unit_int(self):
        with self.assertRaises(TypeError):
            stock = Stock("AAPL","2023-01-05", 1)

    def test_get_profit_rate_Zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            stock = Stock("AAPL", "2023-01-05", "day")
            stock.open_price = 0
            profit_rate = stock.get_profit_rate()

    def test_stock_init_date_dont_exist(self):
        with self.assertRaises(ValueError):
            stock = Stock("AAPL", "2023-12-03", "day")

