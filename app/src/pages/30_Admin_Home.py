import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Display welcome message with user's first name
st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Buttons to navigate to other pages
if st.button('See all Research Opportunities', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/31_All_Opps_Admin.py')

if st.button('See all Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_All_Student_Admin.py')

if st.button('Generate Reports on Student Engagement', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_Generate_Report.py')

if st.button('Update Student Profiles', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/34_Update_Student.py')