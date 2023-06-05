import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title("My mom's new healthy dinner")

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit choice to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
expect URLError as e:
  streamlit.error()
  
streamlit.text(fruityvice_response)
    
streamlit.write('The user entered ', fruit_choice)





streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
