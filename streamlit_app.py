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

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choise = streamlit.text_input("What fruit would you like infromation about?")
  streamlit.write('The use entered', fruit_choise)
if not fruit_choise:
  streamlit.error("Please select a fruit to get information")
else
  #New section to display fruityvice api response
  #import requests
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
  #streamlit.text(fruityvice_response.json())

  # convert the json to table format
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # display the table format
  streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()


streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)


#my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur=my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row=my_cur.fetchone()
#streamlit.text("The fruit load list contains:")
#stremlit.text(my_data_row)

fruits_to_add=streamlit.text_input("What fruit would you like to add?")

streamlit.write("Thanks for adding fruit : " , fruits_to_add)

my_cur.execute("insert into fruit_load_list values('from_streamlit')")
