import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('🥣 Breakfast menu')
streamlit.text('🥗 Dosa, Idli and sambhar')
streamlit.text('🥑 Poha, Misla Pav & Kaju Shake')
streamlit.text('🐔 Eggs & Boliled chicken')
streamlit.text('🍞  Avocado Toast')

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list =pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.datafram(my_fruit_list)
