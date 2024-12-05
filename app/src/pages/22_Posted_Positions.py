import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('My Posted Research Positions')

ownerID = st.session_state['professor_id']

response = requests.get("http://api:4000/opportunities/o{ownerID}")

if response.status_code == 200:
    results = response.json()

    if results:
        for position in results:
            research_title = position.get['research_title', 'No Title']
            professor_id = position.get['professor_id', 'No ID']
            research_area = position.get['research_area', 'No Area']
            research_description = position.get['research_description', 'No Description']
            department_id = position.get['department_id', 'No Department']
            skill_id = position.get['skill_id', 'No Skill']

            prof_name_result = requests.get(f'http://api:4000/professors/p{professor_id}').json()
            professor_firstname = prof_name_result[0].get('FirstName', 'No First Name')
            professor_lastname = prof_name_result[0].get('LastName', 'No Last Name')
            professor_name = f'Professor {professor_firstname} {professor_lastname}'

            # Display each post using styled HTML
            st.markdown(f"""
                <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                    <h3 style="margin-bottom: 10px; color: #90AEAD;">{research_title}</h3>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Group:</strong> {professor_name}</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Student:</strong> {research_area}</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Created At:</strong> {department_id}</p>
                    <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Created At:</strong> {skill_id}</p>
                    <p style="margin-bottom: 12px; color: #D1D7DC;">{research_description}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No posts found for the selected group.")
else:
    st.error(f"Error: {response.status_code}, {response.text}")



if st.button("Back"):
    st.switch_page('pages/20_Professor_Home.py')

        



