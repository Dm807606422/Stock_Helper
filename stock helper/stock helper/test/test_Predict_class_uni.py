"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - test_Predict_class_uni.py
unittest for Predict class
"""
from unittest import TestCase
from models.Final_predict_class import Predict


class Predict_test(TestCase):

    def test_init_name(self):
        stock = Predict('AAPL')
        self.assertEqual(stock.stock_name, 'AAPL')

    def test_init_wrong_type_name_input(self):
        with self.assertRaises(TypeError):
            stock = Predict(1)

    def test_get_stock_shake(self):
        stock = Predict("AAPL")
        stock.one_year_data = {
            'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
        result =[0, 0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
        stock.get_stock_shake()
        self.assertEqual(stock.stock_shake, result)

    def  test_get_stock_shake_Zero_Division_error(self):
        with self.assertRaises(ZeroDivisionError):
            stock = Predict("AAPL")
            stock.one_year_data = {
                'results': [{'c': 2, 'o': 0}, {'c': 2, 'o': 0}, {'c': 2, 'o': 0}, {'c': 2, 'o': 0}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 0}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 0}, {'c': 2, 'o': 1}, {'c': 2, 'o': 0}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
            stock.get_stock_shake()

    def test_get_bbands(self):
        stock = Predict("AAPL")
        stock.one_year_data = {
            'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
        result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.0, 2.0, 2.0]
        stock.get_bbands()
        self.assertEqual(stock.bbands, result)

    def test_get_bbands_rate(self):
        stock = Predict("AAPL")
        stock.one_year_data = {
            'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
        result = [0.0, 0.0, 0.0]
        stock.get_bbands()
        stock.get_bbands_rate()
        self.assertEqual(stock.bbands_rate, result)

    def test_get_bbands_rate_Zero_Division_error(self):
        with self.assertRaises(ZeroDivisionError):
            stock = Predict("AAPL")
            stock.one_year_data = {
                'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
            stock.bbands =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            stock.get_bbands_rate()

    def test_get_bbands_rate_bbands_not_long_enough_error(self):
        with self.assertRaises(ValueError):
            stock = Predict("AAPL")
            stock.one_year_data = {
                'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                            {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
            stock.bbands =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            stock.get_bbands_rate()

    def test_get_increase(self):
        stock = Predict("AAPL")
        stock.one_year_data = {
            'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
        result = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
        stock.get_increase()
        self.assertEqual(stock.increase_list, result)

    def test_get_scatter_plot(self):
        stock = Predict("AAPL")
        stock.one_year_data = {
            'results': [{'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1},
                        {'c': 2, 'o': 1}, {'c': 2, 'o': 1}, {'c': 2, 'o': 1}]}
        x_red_test_result, y_red_test_result, x_green_test_result, y_green_test_result = [], [], [100.0, 100.0], [0.0, 0.0]
        stock.get_stock_shake()
        stock.get_bbands()
        stock.get_bbands_rate()
        x_red, y_red, x_green, y_green = stock.get_scatter_plot()
        self.assertEqual(x_red, x_red_test_result)
        self.assertEqual(y_red, y_red_test_result)
        self.assertEqual(x_green, x_green_test_result)
        self.assertEqual(y_green, y_green_test_result)

    def test_muti_regression(self):
        stock = Predict("AAPL")
        stock.bbands_rate = [1,2,3,4]
        stock.stock_shake = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 7, 9]
        stock.increase_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 10]
        result = stock.muti_regression()
        self.assertEqual(result, "This stock has a 60% probability of making a profit on the next trading day")

    def test_muti_regression_increase_list_not_long_enough(self):
        with self.assertRaises(ValueError):
            stock = Predict("AAPL")
            stock.bbands_rate = [1, 2, 3, 4]
            stock.stock_shake = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 7, 9]
            stock.increase_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            result = stock.muti_regression()

    def test_muti_regression_stock_shake_list_not_long_enough(self):
        with self.assertRaises(ValueError):
            stock = Predict("AAPL")
            stock.bbands_rate = [1, 2, 3, 4]
            stock.stock_shake = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            stock.increase_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 10]
            result = stock.muti_regression()

