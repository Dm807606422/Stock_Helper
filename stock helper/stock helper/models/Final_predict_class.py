"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - Final_predict_class.py
Models, Predict class for final project
"""
import models.function_help
import numpy as np
from sklearn.linear_model import LinearRegression
import time


class Predict:
    """
    A class for predicting stock market trends based on various indicators.

    Attributes:
    - stock_name (str): Ticker symbol of the stock.
    - one_year_data (dict): Stock data for the past year.
    - stock_shake (list): List of stock shake rates.
    - bbands (list): List of Bollinger Bands values.
    - bbands_rate (list): List of Bollinger Bands percentage rates.
    - increase_list (list): List of daily stock price increase percentages.

    Methods:
    - get_one_year_data(): Fetches one year of historical stock data.
    - get_stock_shake(): Calculates stock shake rates.
    - get_bbands(): Calculates Bollinger Bands values.
    - get_bbands_rate(): Calculates Bollinger Bands percentage rates.
    - get_increase(): Calculates daily stock price increase percentages.
    - get_scatter_plot(): Generates data for a scatter plot based on stock shake and Bollinger Bands.
    - muti_regression(): Performs multiple linear regression and provides a probability prediction.

    Raises:
    - TypeError: If the stock_name is not a string.
    - ZeroDivisionError: If division by zero occurs during rate calculations.
    - ValueError: If there is insufficient data for certain calculations.
    """

    def __init__(self, stock_name):
        """
        Initializes a Predict object with a given stock name.

        Parameters:
        - stock_name (str): Ticker symbol of the stock.

        Raises:
        - TypeError: If stock_name is not a string.
        """
        if not isinstance(stock_name, str):
            raise TypeError("invalid stock_name")
        self.stock_name = stock_name
        self.one_year_data = None
        self.stock_shake = None
        self.bbands = None
        self.bbands_rate = None
        self.increase_list = None

    def get_one_year_data(self):
        """
        Fetches historical stock data for the past year.

        Sets the 'one_year_data' attribute with the fetched data.

        Raises:
        - PermissionError: If there is an issue with the API request (non-200 status code).
        """
        now = int(time.time())
        timeArray = time.localtime(now)
        now_date = time.strftime("%Y-%m-%d", timeArray)

        year_before = int(time.time()) - 31536000
        timeArray_year_before = time.localtime(year_before)
        year_before_date = time.strftime("%Y-%m-%d", timeArray_year_before)
        self.one_year_data = models.function_help.get_info(self.stock_name, year_before_date, now_date, time_unit="day")

    def get_stock_shake(self):
        """
        Calculates stock shake rates based on historical stock data.

        Sets the 'stock_shake' attribute with the calculated rates.

        Raises:
        - ZeroDivisionError: If division by zero occurs during rate calculations.
        """
        stock_shake = [0, 0]
        shock_start_point = 2
        while shock_start_point < len(self.one_year_data['results']):
            if self.one_year_data['results'][shock_start_point - 3]['o'] == 0:
                raise ZeroDivisionError("Zero can't divide")
            rate = (float(self.one_year_data['results'][shock_start_point]['c']) - float(
                self.one_year_data['results'][shock_start_point - 3]['o'])) / float(
                self.one_year_data['results'][shock_start_point - 3]['o']) * 100
            rate = round(rate, 2)
            stock_shake.append(rate)
            shock_start_point += 1
        self.stock_shake = stock_shake

    def get_bbands(self):
        """
        Calculates Bollinger Bands values based on historical stock data.

        Sets the 'bbands' attribute with the calculated values.

        """

        bbands = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bb_start_point = 21
        while bb_start_point <= len(self.one_year_data['results']):
            sum = 0
            for i in range(bb_start_point - 21, bb_start_point):
                sum += float(self.one_year_data['results'][i]['c'])
            bbands_number = sum / 21
            bbands_number = round(bbands_number, 2)
            bbands.append(bbands_number)
            bb_start_point += 1
        self.bbands = bbands

    def get_bbands_rate(self):
        """
        Calculates Bollinger Bands percentage rates based on historical stock data.

        Sets the 'bbands_rate' attribute with the calculated rates.

        Raises:
        - ValueError: If there is insufficient data for certain calculations.
        """
        bbands_rate = []
        if len(self.bbands) < 21:
            raise ValueError("bbands not enough long")
        for i in range(20, len(self.one_year_data['results'])):
            if self.bbands[i] == 0:
                raise ZeroDivisionError("BBands is Zero : Zero Division Error")
            bb_rate = (self.one_year_data['results'][i]['c'] - self.bbands[i]) / self.bbands[i] * 100
            bb_rate = round(bb_rate, 2)
            bbands_rate.append(bb_rate)
        self.bbands_rate = bbands_rate

    def get_increase(self):
        """
        Calculates daily stock price increase percentages based on historical stock data.

        Sets the 'increase_list' attribute with the calculated percentages.
        """
        increase_list = []
        for i in range(0, len(self.one_year_data['results'])):
            increase = (self.one_year_data['results'][i]['c'] - self.one_year_data['results'][i]['o']) / \
                       self.one_year_data['results'][i]['o'] * 100
            increase = round(increase, 2)
            increase_list.append(increase)
        self.increase_list = increase_list

    def get_scatter_plot(self):
        """
        Generates data for a scatter plot based on stock shake and Bollinger Bands.

        Returns:
        tuple: Four lists (x_red, y_red, x_green, y_green) for plotting.

        """
        x_red = []
        y_red = []
        x_green = []
        y_green = []
        for i in range(0, len(self.stock_shake) - 21):
            if self.one_year_data['results'][i + 21]['c'] > self.one_year_data['results'][i + 21]['o']:
                x_green.append(self.stock_shake[i + 20])
                y_green.append(self.bbands_rate[i])
            else:
                x_red.append(self.stock_shake[i + 20])
                y_red.append(self.bbands_rate[i])
        return x_red, y_red, x_green, y_green

    def muti_regression(self):
        """
        Performs multiple linear regression and provides a probability prediction.

        Returns:
        str: Prediction message indicating the probability of making a profit or losing money.

        Raises:
        - ValueError: If there is insufficient data for regression testing.
        """
        x = []
        if len(self.stock_shake) < 21:
            raise ValueError("stock_shake list not long enough for muti_regression test")
        for i in range(0, len(self.bbands_rate)):
            x.append([self.bbands_rate[i], self.stock_shake[i + 20]])
        x = x[:-1]
        if len(self.increase_list) < 22:
            raise ValueError("increase_list not long enough for muti_regression test")
        y = self.increase_list[21:]
        x_bbands_rate_stock_shake = np.array(x)
        y_increase = np.array(y)
        regressor = LinearRegression()
        regressor.fit(x_bbands_rate_stock_shake, y_increase)
        x_predict = np.array(x[-1]).reshape(1, -1)
        result = []
        for i in x:
            i_x = np.array(i).reshape(1, -1)
            y_predict = regressor.predict(i_x)
            if y_predict >= 0:
                result.append(1)
            else:
                result.append(0)
        y_predict = regressor.predict(x_predict)
        if y_predict >= 0:
            return "This stock has a 60% probability of making a profit on the next trading day"
        else:
            return "This stock has a 60% probability of losing money on the next trading day"

