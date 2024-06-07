"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - test_Function_uni.py
unittest for function_help
"""
from unittest import TestCase
from unittest.mock import patch,Mock
import models.function_help


class Function_help_test(TestCase):

    def test_get_info(self):
        with patch("models.function_help.requests.get") as requests_get_Mock:
            response = Mock()
            response.status_code = 200
            response.json.return_value = {"results": ["1","2","3"]}
            requests_get_Mock.return_value = response
            result = models.function_help.get_info("AAPL", "2023-01-05", "2023-01-05", "day")
            self.assertEqual(result, {"results": ["1","2","3"]})

    def test_get_info_wrong_status_code(self):
        with self.assertRaises(PermissionError):
            with patch("models.function_help.requests.get") as requests_get_Mock:
                response = Mock()
                response.status_code = 404
                response.json.return_value = {"results": ["1","2","3"]}
                requests_get_Mock.return_value = response
                result = models.function_help.get_info("AAPL", "2023-01-05", "2023-01-05", "day")

    def test_get_info_wrong_type_stock_name(self):
        with self.assertRaises(TypeError):
            data = models.function_help.get_info(1, "2023-01-05", "2023-01-05", time_unit="day")

    def test_get_info_wrong_type_from_time(self):
        with self.assertRaises(TypeError):
            data = models.function_help.get_info("AAPL", 1, "2023-01-05", time_unit="day")

    def test_get_info_wrong_type_to_time(self):
        with self.assertRaises(TypeError):
            data = models.function_help.get_info("AAPL", "2023-01-05", 1, time_unit="day")

    def test_get_info_wrong_type_time_unit(self):
        with self.assertRaises(TypeError):
            data = models.function_help.get_info("AAPL", "2023-01-05", "2023-01-05", 1)

    def test_get_stock_list(self):
        with patch("models.function_help.requests.get") as requests_get_Mock:
            response = Mock()
            response.status_code = 200
            response.json.return_value = {"tickers": [{"ticker": "1"}, {"ticker": "2"}]}
            requests_get_Mock.return_value = response
            result = models.function_help.get_stock_list()
            self.assertEqual(result, ["1","2"])

    def test_get_stock_list_wrong_status_code(self):
        with self.assertRaises(PermissionError):
            with patch("models.function_help.requests.get") as requests_get_Mock:
                response = Mock()
                response.status_code = 404
                response.json.return_value = {"tickers": [{"ticker": "1"}, {"ticker": "2"}]}
                requests_get_Mock.return_value = response
                result = models.function_help.get_stock_list()

    def test_get_date_for_compare(self):
        year, month, day = models.function_help.get_date_for_compare('2023-01-05')
        self.assertEqual(year, 2023)
        self.assertEqual(month, 1)
        self.assertEqual(day, 5)

    def test_get_date_for_compare_wrong_type_input(self):
        with self.assertRaises(TypeError):
            year, month, day = models.function_help.get_date_for_compare(1)
