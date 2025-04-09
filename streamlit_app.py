# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
#import pandas as pd

# Title
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write("Choose the fruits in your custom smoothie!")

Name_on_order = st.text_input('Name on Smoothie:')
st.write("The Name of your smoothie is:", Name_on_order)

# Get the Snowflake session
session = get_active_session()



my_dataframe = session.table("Smoothies.public.FRUIT_OPTIONS").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_List = st.multiselect('Choose 5 Ingredients:',my_dataframe, max_selections=5)

if ingredients_List:
    #st.write(Ingredients_List)
    #st.text(Ingredients_List)

    ingredients_string = ''
    
    
    for fruits_chosen in ingredients_List:
        ingredients_string += fruits_chosen + ' '
        
    #st.write(ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,Name_on_order)
            values ('""" + ingredients_string + """' , '""" + Name_on_order + """'  );"""
    
    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    #if ingredients_string:
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered, ' + Name_on_order)
