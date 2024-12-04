import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Find Posts By Group')

selected_option = st.selectbox("Choose an Group:", ["Engineering", "Computer Science", 
                                                    "Science", "Health Science", "Social Science", "Business"])

if st.button("Submit",
             type='primary'):
    response = requests.get(f'http://api:4000/p/posts/{selected_option}')
    
    if response.status_code == 200:
        # parse the response JSON
        results = response.json()   
        # display the results in a dataframe
        st.dataframe(results)
    else:
        st.error(f"Error: {response.status_code}, {response.text}")



if st.button("Back"):
    st.switch_page('pages/00_Undergraduate_Home.py')
