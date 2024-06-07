"""
Ziqi Mao
CS 5001
Dec 07,2023
2023 Fall Semester
Final - app.py
Control, homepage for final project
"""
import streamlit as st
from pages_app import Stock_Check, Stock_Predict
from models.Final_stock_class import Stock
from models.Final_predict_class import Predict
import models.function_help
import datetime


def main():
    try:
        st.set_page_config(
            page_title="Home Page",
            page_icon="👋",
            layout="centered",
            initial_sidebar_state="auto",
            menu_items=None
        )
        placeholder = st.empty()
        placeholder.markdown(
            """
            ## Welcome to Dm Stock Predict App 👋
            This software is used to help stock traders.\n
            👈 Select a function you need from the sidebar
            ### What this app can do?
            - Query daily stock data
            - Predict whether a stock will grow or fall on the next trading day
    
            ### Data Sources
            - The data sources is come from polygon.io (https://api.polygon.io/v2/)
        """
        )

        ## Navigation
        app_dict = ['Stock Check','Stock Predict']
        st.sidebar.title("Navigation")
        choose = st.sidebar.selectbox('Select an option', app_dict)
        if st.sidebar.button('Go') and choose is not None:
            if choose == 'Stock Check':
                st.session_state['page'] = 'Stock Check'
            elif choose == 'Stock Predict':
                st.session_state['page'] = 'Stock Predict'

        if 'page' in st.session_state:
            if st.session_state['page'] == 'Stock Check':
                placeholder.empty()
                Stock_Check. render_stock_input()

                if 'stock_name' in st.session_state.keys() and 'stock_date' in st.session_state.keys():
                    stock_name = st.session_state['stock_name']
                    stock_date = st.session_state['stock_date']
                    button = st.button('Show')
                    if button and stock_name != None and stock_date is not None:
                        year, month, day = models.function_help.get_date_for_compare(stock_date)
                        if not datetime.date(year,month,day) <= datetime.date.today():
                            st.error("Please entering a date before the current date")
                        if not datetime.date(year,month,day).weekday() <= 5:
                            st.error("The date you entered is not a trading day, please enter a date from Monday to Friday")
                        stock = Stock(stock_name, stock_date)
                        increase_rate = stock.get_profit_rate()
                        Stock_Check.render_show(stock_name, stock.close_price, stock.open_price, stock.high_value, stock.low_value, increase_rate)


            elif st.session_state['page'] == 'Stock Predict':
                placeholder.empty()
                Stock_Predict.render_predict_input()
                if 'predict_name' in st.session_state.keys():
                    stock_predict_name = st.session_state['predict_name']

                if st.button('Predict') and stock_predict_name is not None:
                    stock = Predict(stock_predict_name)

                    stock.get_one_year_data()
                    stock.get_stock_shake()
                    stock.get_bbands()
                    stock.get_bbands_rate()
                    stock.get_increase()
                    predict_result = stock.muti_regression()
                    x_red, y_red, x_green, y_green = stock.get_scatter_plot()
                    Stock_Predict.render_predict_show(x_red, y_red, x_green, y_green, predict_result)

    except FileNotFoundError as fnf:
        print("File Not Found: ", fnf)
    except TypeError as te:
        print("Type Error: ", te)
    except ValueError as ve:
        print("Value Error: ", ve)
    except PermissionError as pe:
        print("Permission Error: ", pe)
    except ZeroDivisionError as zd:
        print("ZeroDivisionError: ", zd)


if __name__ == "__main__":
    main()