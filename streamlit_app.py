import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header("Fruityvice Fruit Advice!")
streamlit.title('My parents new healthy Diner')

streamlit.header('🥣  Breakfast Menu')
streamlit.text(' 🐔  Omlete')
streamlit.text('🥗 Smoothie')
streamlit.text('🥑🍞 Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect('Pick some fruits:' , list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruis_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruis_to_show)


def get_fruityvice_data(this_fruit_choise):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choise)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
  

streamlit.header("View our fruit list - Add your favourites!")

try:
  fruit_choise = streamlit.text_input("What fruit would you like infromation about?")
  if not fruit_choise:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choise)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()


streamlit.text("The fruit load list contains:")
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("select * from fruit_load_list")
  return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_row =get_fruit_load_list()
 my_cnx.close()
 streamlit.dataframe(my_data_row)


def insert_row_snowflake(new_fruit):
 with my_cnx.cursor() as my_cur:
  my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
  return "Thanks for ading " + new_fruit
  
add_my_fruit=streamlit.text_input("What fruit would you like to add?")
if streamlit.button("Add a Fruit to the list."):
 my_cnx =my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 back_from_function = insert_row_snowflake(add_my_fruit)
 streamlit.text(back_from_function)
