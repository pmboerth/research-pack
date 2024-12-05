import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Students')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# Initialize state to track whether the button was pressed
if 'show_students' not in st.session_state:
    st.session_state['show_students'] = False

# Button to fetch and display all students
if st.button('See All Students', type='primary'):
    st.session_state['show_students'] = True

# Check if we should display students
if st.session_state['show_students']:
    response = requests.get('http://api:4000/s/students')
    
    if response.status_code == 200:
        results = response.json()
        
        if results:
            for student in results:
                student_id = student.get('StudentId')
                student_firstname = student.get('FirstName', 'No First Name')
                student_lastname = student.get('LastName', 'No Last Name')
                student_email = student.get('Email', 'No Email')
                student_skillid = student.get('SkillId', 'No Skill ID')
                student_departmentid = student.get('DepartmentId', 'No Department ID')
                student_interest = student.get('ResearchInterest', 'No Research Interest')
                student_year = student.get('Year', 'No Year')
                student_major = student.get('Major', 'No Major')
                student_type = student.get('StudentType', 'No Student Type')

                st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px;">
                        <h3>{student_firstname} {student_lastname}</h3>
                        <p><strong>Email:</strong> {student_email}</p>
                        <p><strong>Skill:</strong> {student_skillid}</p>
                        <p><strong>Department:</strong> {student_departmentid}</p>
                        <p><strong>Interest:</strong> {student_interest}</p>
                        <p><strong>Year:</strong> {student_year}</p>
                        <p><strong>Major:</strong> {student_major}</p>
                        <p><strong>Type:</strong> {student_type}</p>
                    </div>
                """, unsafe_allow_html=True)

                if st.button(f"Delete {student_firstname} {student_lastname}", key=f"delete_{student_id}"):
                    delete_response = requests.delete(f'http://api:4000/s/students/s{student_id}')
                    
                    if delete_response.status_code == 200:
                        st.success(f"Successfully deleted {student_firstname} {student_lastname}.")
                        st.session_state['show_students'] = True  # Keep the list visible
                    else:
                        st.error(f"Failed to delete {student_firstname} {student_lastname}. Please try again.")
        else:
            st.warning("No Students available.")
    else:
        st.error("Failed to fetch students.")

# Back button
if st.button("Back"):
    st.session_state['show_students'] = False
    st.switch_page('pages/30_Admin_Home.py')