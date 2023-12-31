import streamlit

streamlit.title("🥣 My Parents New Healthy Diner")
streamlit.header("🥗Breakfast menus")
streamlit.text("🐔Bread Omlet")
streamlit.text(" 🥑oats with boiled eggs")
streamlit.text("🍞Idli Shambhar")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

#####adding the below connector 
#########made the secrets changes
########query some data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit__load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

