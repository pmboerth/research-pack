import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('My Posted Research Positions')

ownerID = st.session_state['professor_id']

response = requests.get(f"http://api:4000/o/opportunities/o{ownerID}")

if response.status_code == 200:
    results = response.json()

    if results:
        for position in results:
            research_title = position.get('Name', 'No Title')
            research_area = position.get('ResearchArea', 'No Area')
            research_description = position.get('Description', 'No Description')
            department_id = position.get('DepartmentId', 'No Department')
            skill_id = position.get('SkillId', 'No Skill')
            
            # Fetch department name based on department ID
            result1 = requests.get(f'http://api:4000/d/departments/d{department_id}').json()
            department_name = result1[0].get('Name', 'No Name')
    


            # Display each post using styled HTML
            st.markdown(f"""
                <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                    <h3 style="margin-bottom: 10px; color: #90AEAD;">{research_title}</h3>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Group:</strong> Emily Chen</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Student:</strong> {research_area}</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Department:</strong> {department_name}</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Required Skill:</strong> {skill_id}</p>
                    <p style="margin-bottom: 12px; color: #D1D7DC;">{research_description}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No posts found for the selected group.")
else:
    st.error(f"Error: {response.status_code}, {response.text}")



if st.button("Back"):
    st.switch_page('pages/20_Professor_Home.py')

        



