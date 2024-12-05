import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('View a Students List of Applications')

student_id = st.text_input("Enter a Students ID:")

if st.button("View Applications",type="primary"):
    # Check if the student ID is valid
    response_student = requests.get(f'http://api:4000/s/students/s{student_id}')

    if response_student.status_code == 200:
        student_data = response_student.json()
        student_name = student_data[0].get('FirstName', 'No First Name') + ' ' + student_data[0].get('LastName', 'No Last Name')

        st.title(f'Applications Submitted by {student_name}')

        response = requests.get(f'http://api:4000/a/applications/s{student_id}')
        if response.status_code == 200:
            result = response.json()

            if result:
                for application in result:
                    status = application.get('ApplicationStatus', 'No Status')
                    position_id = application.get('PositionId', 'No Position ID')
                    created_at = application.get('CreatedAt', 'No Date Available')

                    result1 = requests.get(f'http://api:4000/o/opportunities/p{position_id}').json()
                    position_name = result1[0].get('Name', 'No Position Name')

                    # display each post using styled HTML
                    st.markdown(f"""
                        <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                            <h3 style="margin-bottom: 10px; color: #90AEAD;">{position_name}</h3>
                            <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Status:</strong> {status}</p>
                            <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Submitted at:</strong> {created_at}</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No posts found for that student.")
        else:
            st.error(f"Failed to retrieve applications: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a valid student ID to view their applications.")

if st.button("Back"):
    st.switch_page('pages/20_Professor_Home.py')