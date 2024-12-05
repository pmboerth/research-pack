import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.title('Post a Research Opportunity')

# Input fields for opportunity details
research_title = st.text_input("Enter a Research Position Title:")
professorid = st.session_state['professor_id']
research_area = st.text_input("Enter a Research Area:")
research_description = st.text_area("Enter a Description of the Postion:")
department_id = st.session_state['department_id']
skill_id = st.text_input("Enter a Skill ID:")

# Post opportunity if fields are filled and call the API
if st.button("Post Opportunity",
             type="primary"):
    if research_title and research_area and research_description and skill_id:
            
            post = {
                "name": research_title,
                "owner_id": professorid,
                "research_area": research_area,
                "description": research_description,
                "department_id": department_id,
                "skill_id": skill_id
            }
            
            response = requests.post("http://api:4000/o/opportunities", json=post)
            
            if response.status_code == 200:
                st.success("Research Opportunity successfully added!")
            else:
                st.error(f"Failed to add Research Opportunity: {response.status_code} - {response.text}")
    else:
        st.warning("Please fill out all required fields.")

# Button to go back to the home page    
if st.button("Back"):
    st.switch_page('pages/20_Professor_Home.py')
