import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('See all Research Opportunities', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_All_Opportunities.py')

if st.button('Delete Research Opportunities', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')

if st.button('See all Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')

if st.button('Remove ineligible Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')

if st.button('Generate reports on student engagement', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')

if st.button('Update Student profiles', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_See_Posts.py')