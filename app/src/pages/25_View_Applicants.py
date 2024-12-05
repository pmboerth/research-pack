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

    response = requests.get(f"http://api:4000/a/applications/o{position_id}")

    if response.status_code == 200:
        applications = response.json()
        
        if applications:
            for application in applications:
                student_id = application.get('ApplicantId', 'No Student ID')
                application_id = application.get('ApplicationId', 'No Application ID')
                application_status = application.get('ApplicationStatus', 'No Status')
                created_at = application.get('CreatedAt', 'No Date')

                # Fetch student information based on student ID
                result1 = requests.get(f'http://api:4000/s/students/s{student_id}').json()
                student_name = result1[0].get('FirstName', 'No First Name') + ' ' + result1[0].get('LastName', 'No Last Name')
                student_email = result1[0].get('Email', 'No Email')
                student_major = result1[0].get('Major', 'No Major')
                student_year = result1[0].get('Year', 'No Year')
                student_type = result1[0].get('StudentType', 'No Type')
                research_interest = result1[0].get('ResearchInterest', 'No Interest')
                
                st.markdown(f"""
                    <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                        <h3 style="margin-bottom: 10px; color: #90AEAD;">{student_name}</h3>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Email: </strong>{student_email}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Major: </strong>{student_major}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Year: </strong>{student_year}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Type: </strong>{student_type}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Research Interests: </strong>{research_interest}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Submitted At: </strong>{created_at}</p>
                    </div>
                """, unsafe_allow_html=True)
    
if st.button("Back"):
    st.switch_page('pages/22_Posted_Positions.py')   
        



