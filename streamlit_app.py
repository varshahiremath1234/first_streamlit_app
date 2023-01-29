import streamlit
import pandas
import requests
import snowflake.connector


streamlit.header('Breakfast Favourites')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🍠Kale, Spinach & Rocket Smoothie')
streamlit.text('🌯Hard-Boiled Free-Range Egg')
streamlit.text('🍪🥑Avacado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits here:",list(my_fruit_list.index),['Pear','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruity Vice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

