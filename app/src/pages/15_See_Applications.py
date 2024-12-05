import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('View Applications for a Research Opportunity')

# Input field for Opportunity ID
opportunity_id = st.text_input("Enter an Opportunity ID:")

if st.button("View Applications", type="primary"):
    # Check if the opportunity ID is valid
    response_opportunity = requests.get(f'http://api:4000/o/opportunities/p{opportunity_id}')
    
    if response_opportunity.status_code == 200:
        opportunity_data = response_opportunity.json()
        opportunity_name = opportunity_data[0].get('Name', 'No Opportunity Name')

        st.subheader(f'Applications Submitted for: {opportunity_name}')

        # Fetch all applications for the specified opportunity ID
        response = requests.get(f'http://api:4000/a/applications/o{opportunity_id}')
        if response.status_code == 200:
            applications = response.json()

            if applications:
                for application in applications:
                    student_id = application.get('StudentId', 'No Student ID')
                    status = application.get('ApplicationStatus', 'No Status')
                    created_at = application.get('CreatedAt', 'No Date Available')

                    # Fetch student details based on Student ID
                    student_response = requests.get(f'http://api:4000/s/students/s{student_id}')
                    if student_response.status_code == 200:
                        student_data = student_response.json()
                        if student_data:
                            student_name = student_data[0].get('FirstName', 'Unknown') + ' ' + student_data[0].get('LastName', 'Unknown')
                        else:
                            student_name = "No applications found for this opportunity."
                    else:
                        student_name = "Unknown Student"

                    # Display each application using styled HTML
                    st.markdown(f"""
                        <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                            <h3 style="margin-bottom: 10px; color: #90AEAD;">Applicant: {student_name}</h3>
                            <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Student ID:</strong> {student_id}</p>
                            <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Status:</strong> {status}</p>
                            <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Submitted at:</strong> {created_at}</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No applications found for this opportunity.")
        else:
            st.error(f"Failed to retrieve applications: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a valid Opportunity ID to view the applications.")
        
# Back button to return to the home page
if st.button("Back"):
    st.switch_page('pages/10_Graduate_Home.py')