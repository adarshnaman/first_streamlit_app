import streamlit
import pandas
import requests

#streamlit.title("My mom's new healthy dinner")

#streamlit.header('Breakfast Menu')
#streamlit.text('Omega 3 & Blueberry Oatmeal')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg')

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#my_fruit_list = my_fruit_list.set_index('Fruit')


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
