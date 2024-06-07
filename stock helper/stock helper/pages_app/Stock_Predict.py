"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - Stock_Predict.py
View, page apps for final project
"""
import streamlit as st
import models.function_help
import pandas as pd


def render_predict_input():
    """
    Render the input section for the Predict Page.

    Displays a header, an input field for stock selection, and a selection box for available stocks.

    Updates the 'predict_name' attribute in the session_state with the selected stock name.
    """

    st.header("Predict Page:chart_with_upwards_trend:")
    stock_list = models.function_help.get_stock_list()
    stock_name = st.text_input("Please enter the name of the stock you want to predict ex: AAPL", "")

    if stock_name:
        matching_stock = [stock for stock in stock_list if stock_name.upper() in stock]
        stock_predict_name = st.selectbox("Please select the stock", matching_stock)
        st.session_state['predict_name'] = stock_predict_name


def render_predict_show(x_red, y_red, x_green, y_green,predict_result):
    """
    Render the prediction result and scatter charts.

    Parameters:
    - x_red (list): X-axis values for stocks with predicted loss.
    - y_red (list): Y-axis values for stocks with predicted loss.
    - x_green (list): X-axis values for stocks with predicted profit.
    - y_green (list): Y-axis values for stocks with predicted profit.
    - predict_result (str): Result message from the prediction.

    Displays a subheader for the prediction result and two scatter charts showing relationships
    between Three-day Rate of Change and Bollinger Bands Percentage for stocks with predicted loss
    and profit.

    """

    st.subheader("Predict Result", divider='rainbow')
    st.write(predict_result)
    st.write("\n")
    st.write("\n")

    data_1 = {'Three-day Rate of Change': x_red, 'Bollinger Bands Percentage': y_red}
    data_2 = {'Three-day Rate of Change': x_green, 'Bollinger Bands Percentage': y_green}
    scatter_df_1 = pd.DataFrame(data=data_1)
    scatter_df_2 = pd.DataFrame(data=data_2)
    st.subheader('The relationship between Three-day Rate of Change and Bollinger Bands Percentage when Stock Loss',
                 divider='rainbow')
    st.scatter_chart(
        scatter_df_1,
        x='Three-day Rate of Change',
        y='Bollinger Bands Percentage',
        size=20,
        color='#FF0000',
    )
    st.subheader('The relationship between Three-day Rate of Change and Bollinger Bands Percentage when Stock Profit',
                 divider='rainbow')
    st.scatter_chart(
        scatter_df_2,
        x='Three-day Rate of Change',
        y='Bollinger Bands Percentage',
        size=20,
        color='#00FF00',
    )
