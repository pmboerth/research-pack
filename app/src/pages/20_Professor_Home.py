import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Professor Chen!')

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