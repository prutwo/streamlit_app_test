import streamlit
import pandas

streamlit.title('Jacks Healthy Diner')

streamlit.header('Breakfast menu')
streamlit.text('Blueberry Oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Scrambled Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add a picklist for the fruit
streamlit.multiselect("Pick your fruit:", list(my_fruit_list.index),['Strawberries'])

#display the table
streamlit.dataframe(my_fruit_list)

