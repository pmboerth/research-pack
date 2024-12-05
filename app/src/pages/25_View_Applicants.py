import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

application_data = st.session_state.get('view_applicants', {})

if application_data:
    position_id = application_data['position_id']
    research_title = application_data['research_title']
    research_area = application_data['research_area']
    research_description = application_data['research_description']
    department_id = application_data['department_id']
    skill_id = application_data['skill_id']

    st.title(f'View Applications for {research_title} Position')

    
 
    
        



