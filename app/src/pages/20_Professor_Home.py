import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Display welcome message with user's first name
st.title('Welcome Professor Chen!')

# Buttons to navigate to other pages
if st.button('Post Research Position', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Post_Position.py')

if st.button('View My Posted Research Positions', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Posted_Positions.py')

if st.button('View All Student Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_All_Applications.py')