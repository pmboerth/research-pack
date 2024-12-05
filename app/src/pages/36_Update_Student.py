import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Edit Student Information')

# Add a field to input the student ID for editing
student_id = st.text_input("Enter Student ID to Edit")

if student_id:
    # Fetch the student's current information using the student ID
    response = requests.get(f'http://api:4000/s/students/s{student_id}')
    
    if response.status_code == 200:
        student = response.json()
        
        if student:
            student_firstname = student[0].get('FirstName', '')
            student_lastname = student[0].get('LastName', '')
            student_email = student[0].get('Email', '')
            student_skillid = student[0].get('SkillId', '')
            student_departmentid = student[0].get('DepartmentId', '')
            student_interest = student[0].get('ResearchInterest', '')
            student_year = student[0].get('Year', '')
            student_major = student[0].get('Major', '')
            student_type = student[0].get('StudentType', '')
            
            response1 = requests.get(f'http://api:4000/sk/skills/s{student_skillid}')
            skill_name = ''
            if response1.status_code == 200:
                skill_data = response1.json()
                skill_name = skill_data[0].get('Name', 'No Name')
        
            response2 = requests.get(f'http://api:4000/d/departments/d{student_departmentid}')
            department_name = ''
            if response2.status_code == 200:
                department_data = response1.json()
                department_name = department_data[0].get('Name', 'No Name')

            st.markdown(f"""
            <div style="border: 1px solid #2C3E50; padding: 18px; margin-bottom: 15px; border-radius: 10px; box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.15); background-color: #2C3E50;">
                <h3 style="margin-bottom: 10px; color: #76C7C0;">{student_firstname + ' ' + student_lastname}</h3>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Email:</strong> {student_email}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Skill:</strong> {skill_name}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Department:</strong> {department_name}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Interest:</strong> {student_interest}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Year:</strong> {student_year}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Major:</strong> {student_major}</p>
                <p style="margin-bottom: 6px; color: #ECF0F1;"><strong>Type:</strong> {student_type}</p>
            </div>
            """, unsafe_allow_html=True)

            # Edit the fields (make them input fields for updating)
            new_firstname = st.text_input("First Name", value=student_firstname)
            new_lastname = st.text_input("Last Name", value=student_lastname)
            new_email = st.text_input("Email", value=student_email)
            new_skillid = st.text_input("Skill ID", value=student_skillid)
            new_departmentid = st.text_input("Department ID", value=student_departmentid)
            new_interest = st.text_input("Research Interest", value=student_interest)
            new_year = st.text_input("Year", value=student_year)
            new_major = st.text_input("Major", value=student_major)
            new_type = st.text_input("Student Type", value=student_type)

            # Add a "Finish" button to submit the updated information
            if st.button("Update",
                         type="primary"):
                # Prepare the updated data
                updated_data = {
                    "first_name": new_firstname,
                    "last_name": new_lastname,
                    "email": new_email,
                    "skill_id": new_skillid,
                    "department_id": new_departmentid,
                    "research_interest": new_interest,
                    "year": new_year,
                    "major": new_major,
                    "student_type": new_type
                }

                # Send the PUT request to update the student information
                update_response = requests.put(f'http://api:4000/s/students/s{student_id}', json=updated_data)

                if update_response.status_code == 200:
                    st.success(f"Successfully updated information for {new_firstname} {new_lastname}.")
                else:
                    st.error("Failed to update student information. Please try again.")
        else:
            st.warning("No student found with that ID.")
    else:
        st.error("Failed to fetch student data. Please check the ID and try again.")
        
# Back button to return to admin home page
if st.button("Back"):
    st.switch_page('pages/30_Admin_Home.py')