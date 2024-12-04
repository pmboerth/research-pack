import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Research Opportunities')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# add a button to use get all the research opportunities
if st.button('See All Opportunities',
             type='primary',
             use_container_width=True):
  results = requests.get('http://api:4000/o/opportunities').json()
  st.dataframe(results)
