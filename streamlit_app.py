import streamlit
import pandas

streamlit.title('Jacks Healthy Diner')

streamlit.header('Breakfast menu')
streamlit.text('Blueberry Oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Scrambled Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

