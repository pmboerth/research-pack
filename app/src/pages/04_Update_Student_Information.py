import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Update Student Information')

# Alex's StudentId will never change and is always 1
student_id = st.session_state['student_id']

# Input fields for updating student information
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
skill_id = st.number_input("Skill ID", min_value=1, step=1)
department_id = st.number_input("Department ID", min_value=1, step=1)
research_interest = st.text_input("Research Interest")
year = st.number_input("Year", min_value=1, step=1)
major = st.text_input("Major")
student_type = st.selectbox("Student Type", ["Undergraduate", "Graduate"])

# Update student information if button is clicked
if st.button("Update Student", type="primary"):
    if not student_id:
        st.error("Student ID is required.")
    else:
        payload = {}
        if first_name:
            payload["first_name"] = first_name
        if last_name:
            payload["last_name"] = last_name
        if email:
            payload["email"] = email
        if skill_id:
            payload["skill_id"] = skill_id
        if department_id:
            payload["department_id"] = department_id
        if research_interest:
            payload["research_interest"] = research_interest
        if year:
            payload["year"] = year
        if major:
            payload["major"] = major
        if student_type:
            payload["student_type"] = student_type
            
        if not payload:
            st.warning("Please provide at least one field to update.")
        else:
            url = f"http://api:4000/s/students/s{student_id}"
            response = requests.put(url, json=payload)

            if response.status_code == 200:
                st.success(f"Successfully updated student {student_id}.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

# Button to go back to the home page
if st.button("Back"):
    st.switch_page('pages/00_Undergraduate_Home.py')

