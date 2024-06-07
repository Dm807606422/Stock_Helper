"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - function_help.py
Models, help function for final project
"""
import requests


URL_GET_INFO = "https://api.polygon.io/v2/aggs/ticker/{stock_name}/range/1/{time_unit}/{from_time}/{to_time}?adjusted=true&sort=asc&limit=280&apiKey={api_key}"
API_KEY = "HxKUR5P_xh9LzvTLeGPyfw_JfmBp0Hbq"
URL_STOCK_LIST = 'https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?apiKey={api_key}'


def get_info(stock_name, from_time, to_time, time_unit="day"):
    """
    Retrieve aggregated stock information within a specified time range.

    Parameters:
    - stock_name (str): Ticker symbol of the stock.
    - from_time (str): Start date in the format "YYYY-MM-DD".
    - to_time (str): End date in the format "YYYY-MM-DD".
    - time_unit (str, optional): Time unit for aggregation (default is "day").

    Returns:
    dict: JSON data containing aggregated stock information.

    Raises:
    - TypeError: If input parameters are not of the expected types.
    - PermissionError: If there is an issue with the API request (non-200 status code).
    """
    if not isinstance(stock_name, str):
        raise TypeError("invalid stock_name")
    if not isinstance(from_time, str):
        raise TypeError("invalid from_time")
    if not isinstance(to_time, str):
        raise TypeError("invalid to_time")
    if not isinstance(time_unit, str):
        raise TypeError("invalid time_unit")
    response = requests.get(URL_GET_INFO.format(stock_name=stock_name, from_time=from_time, to_time=to_time, time_unit=time_unit, api_key=API_KEY))
    if response.status_code == 200:
        data = response.json()
        return data
    raise PermissionError(f"PermissionError: {response.status_code}")


def get_stock_list():
    """
    Retrieve a list of stock tickers.

    Returns:
    list: List of stock tickers.

    Raises:
    - PermissionError: If there is an issue with the API request (non-200 status code).
    """
    response = requests.get(URL_STOCK_LIST.format(api_key=API_KEY))
    stock_list = []
    if response.status_code == 200:
        data = response.json()
        stocks = data["tickers"]
        for stock in stocks:
            stock_list.append(stock['ticker'])
        return stock_list
    else:
        raise PermissionError(f"PermissionError: {response.status_code}")


def get_date_for_compare(date):
    """
    Convert a date string to a tuple of integers (year, month, day).

    Parameters:
    - date (str): Date in the format "YYYY-MM-DD".

    Returns:
    tuple: Tuple containing year, month, and day as integers.

    Raises:
    - TypeError: If input parameter is not of the expected type.
    """
    if not isinstance(date, str):
        raise TypeError("invalid date type")
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    return year, month, day
