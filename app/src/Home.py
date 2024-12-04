##################################################
# This is the main/entry-point file for our project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('ResearchPack')
st.write('\n\n')
st.write('### Hi! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

if st.button("Act as Alex Bellingham, an Undergraduate Student", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'undergraduate_student'
    st.session_state['first_name'] = 'Alex'
    st.session_state['student_id'] = 1
    st.switch_page('pages/00_Undergraduate_Home.py')

if st.button('Act as Jeff Sturrow, a PhD Student', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'graduate_student'
    st.session_state['first_name'] = 'Jeff'
    st.session_state['student_id'] = 2
    st.switch_page('pages/10_Graduate_Home.py')

if st.button('Act as Emily Chen, an Associate Professor', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'professor'
    st.session_state['first_name'] = 'Emily'
    st.session_state['professor_id'] = 1
    st.switch_page('pages/20_Professor_Home.py')

if st.button('Act as Carl Jackson, a Department Administrator',
             type = 'primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'Carl'
    st.session_state['admin_id'] = 1
    st.switch_page('pages/30_Admin_Home.py')




