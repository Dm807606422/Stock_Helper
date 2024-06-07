"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - Stock_Check.py
View, page apps for final project
"""
import streamlit as st
import models.function_help


def render_stock_input():
    """
    Render the input section for the Stock Check Page.

    Displays a header, an input field for stock selection, and a selection box for available stocks.
    Additionally, prompts the user to input a date.

    Updates the 'stock_name' and 'stock_date' attributes in the session_state based on user input.
    """

    st.header("Stock Check Page:100:")
    stock_list = models.function_help.get_stock_list()
    input_name = st.text_input("Please enter the name of the stock ex: AAPL", "")
    matching_stock = [stock for stock in stock_list if input_name.upper() in stock]
    if input_name:
        stock_name = st.selectbox("Please select the stock", matching_stock)
        stock_date = st.date_input("Please enter the date you want to pages_app ex:2023-01-05", value=None)
        stock_date = str(stock_date)
        st.session_state['stock_name'] = stock_name
        st.session_state['stock_date'] = stock_date


def render_show(stock_name,close_price,open_price,high_value,low_value,increase_rate):
    """
    Render the stock information display.

    Parameters:
    - stock_name (str): Ticker symbol of the stock.
    - close_price (float): Closing price of the stock on the specified date.
    - open_price (float): Opening price of the stock on the specified date.
    - high_value (float): Highest price of the stock on the specified date.
    - low_value (float): Lowest price of the stock on the specified date.
    - increase_rate (float): Increase rate of the stock on the specified date.

    Displays metrics for open price, close price, high price, low price, and increase rate in a 2x2 grid.

    Raises:
    - ValueError: If stock_name is not provided.
    """
    if not stock_name:
        raise ValueError("Please input correct name")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Open Price", f"{open_price}$", f"{increase_rate}%")
    col2.metric("Close Price", f"{close_price}$")
    col3.metric("High Price", f"{high_value}$")
    col4.metric("Low price", f"{low_value}$")
