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
if st.button('Find Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Find_Students.py')

if st.button('Find Research', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Find_Research.py')

if st.button('Make a Post', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Make_Post.py')

if st.button('Update Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Make_Profile.py')

if st.button('See Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_See_Applications.py')

if st.button('Add Comment', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_Add_Comment.py')
