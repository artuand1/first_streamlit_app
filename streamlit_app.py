import streamlit
streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🥗kale, spinach and smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥣Omega 3 and blueberry oatmeal')
streamlit.text('🍞Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


