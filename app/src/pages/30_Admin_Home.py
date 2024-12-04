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

if st.button('Delete uncompliant Research Opportunities', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_Delete_Opportunity.py')

if st.button('See all Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_All_Students.py')

if st.button('Remove ineligible Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/34_Remove_Student.py')

if st.button('Generate reports on student engagement', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/35_Generate_Report.py')

if st.button('Update Student profiles', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/36_Update_Student.py')