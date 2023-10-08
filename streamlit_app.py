import streamlit
streamlit.title('My parents new healthy Diner')

streamlit.header('🥣  Breakfast Menu')
streamlit.text(' 🐔  Omlete')
streamlit.text('🥗 Smoothie')
streamlit.text('🥑🍞 Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list=pandas.read("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
