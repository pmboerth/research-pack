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
  st.switch_page('pages/01_All_Opportunities.py')

if st.button('See Posts', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')
  
if st.button('Make a Post', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Make_Post.py')
  
if st.button('Update Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Update_Student_Information.py')
  

  
  
