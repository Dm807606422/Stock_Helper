"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - Final_stock_class.py
Models, Stock class for final project
"""
import models.function_help


class Stock:
    """
    A class representing stock information for a specific date.

    Attributes:
    - stock_name (str): Ticker symbol of the stock.
    - from_time (str): Date for which the stock information is retrieved.
    - to_time (str): Date for which the stock information is retrieved (same as from_time).
    - time_unit (str): Time unit for the stock information retrieval (default is "day").
    - data (dict): Stock information retrieved using the specified parameters.
    - open_price (float): Opening price of the stock on the specified date.
    - close_price (float): Closing price of the stock on the specified date.
    - high_value (float): Highest price of the stock on the specified date.
    - low_value (float): Lowest price of the stock on the specified date.

    Methods:
    - get_profit_rate(): Calculates and returns the profit rate based on the opening and closing prices.

    Raises:
    - TypeError: If stock_name, date, or time_unit is not a string.
    - ValueError: If there is no data available for the specified date.
    - ZeroDivisionError: If the open_price is zero when calculating the profit_rate.
    """
    def __init__(self, stock_name, date, time_unit="day"):
        """
        Initializes a Stock object with stock information for a specific date.

        Parameters:
        - stock_name (str): Ticker symbol of the stock.
        - date (str): Date for which the stock information is retrieved.
        - time_unit (str, optional): Time unit for the stock information retrieval (default is "day").

        Raises:
        - TypeError: If stock_name, date, or time_unit is not a string.
        - ValueError: If there is no data available for the specified date.
        """
        if not isinstance(stock_name, str):
            raise TypeError("invalid stock_name")
        if not isinstance(date, str):
            raise TypeError("invalid date")
        if not isinstance(time_unit, str):
            raise TypeError("invalid time_unit")
        self.stock_name = stock_name
        self.from_time = date
        self.to_time = date
        self.time_unit = time_unit
        self.data = models.function_help.get_info(stock_name,date, date, time_unit="day")
        if self.data['queryCount'] == 0:
            raise ValueError("data for that day didn't exist")
        self.open_price = self.data['results'][0]['o']
        self.close_price = self.data['results'][0]['c']
        self.high_value = self.data['results'][0]['h']
        self.low_value = self.data['results'][0]['l']

    def get_profit_rate(self):
        """
        Calculates the profit rate based on the opening and closing prices.

        Returns:
        float: Profit rate as a percentage.

        Raises:
        - ZeroDivisionError: If the open_price is zero.
        """
        if self.open_price == 0:
            raise ZeroDivisionError("open_price is zero when calculate profit_rate")
        profit_rate = (self.close_price-self.open_price)/self.open_price *100
        profit_rate = round(profit_rate, 2)
        return profit_rate
