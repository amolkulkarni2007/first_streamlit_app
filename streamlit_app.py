import streamlit

streamlit.header("Fruityvice Fruit Advice!")
streamlit.title('My parents new healthy Diner')

streamlit.header('🥣  Breakfast Menu')
streamlit.text(' 🐔  Omlete')
streamlit.text('🥗 Smoothie')
streamlit.text('🥑🍞 Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect('Pick some fruits:' , list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruis_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruis_to_show)

streamlit.header("Fruityvice Fruit Advice!")

#New section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

# convert the json to table format
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the table format
streamlit.dataframe(fruityvice_normalized)
