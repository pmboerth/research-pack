import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

position_data = st.session_state.get('update_position', {})

if position_data:
    position_id = position_data['position_id']
    research_title = position_data['research_title']
    research_area = position_data['research_area']
    research_description = position_data['research_description']
    department_id = position_data['department_id']
    skill_id = position_data['skill_id']

    st.title(f'Update {research_title} Position')
 
    new_research_title = st.text_input("Enter a new Research Position Title:", value=research_title,key=f"new_research_title{position_id}")
    new_research_area = st.text_input("Enter a new Research Area:", value=research_area, key=f"new_research_area{position_id}")
    new_research_description = st.text_area("Enter a new Description of the Postion:", value=research_description, key=f"new_research_description{position_id}")
    new_skill_id = st.text_input("Enter a new Skill ID:", value=skill_id, key=f"new_skill_id{position_id}")

    if st.button("Update",
                    type="primary"):

            update = {
                "name": new_research_title,
                "research_area": new_research_area,
                "description": new_research_description,
                "skill_id": new_skill_id
            }

            response = requests.put(f"http://api:4000/o/opportunities/p{position_id}", json=update)

            if response.status_code == 200:
                st.success(f"Successfully updated: {research_title}.")
            else:
                st.error(f"Failed to update: {response.text}")
else:
    st.error("No position data found. Please go back and select a position to update.")

if st.button("Back"):
    st.switch_page('pages/22_Posted_Positions.py')

        



