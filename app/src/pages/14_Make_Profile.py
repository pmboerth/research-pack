import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Add the sidebar navigation
SideBarLinks()

# Set the header for the page
st.title('Create Graduate Student Profile')

# Input fields for student profile details
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
skill_id = st.number_input("Skill ID", min_value=1, step=1)
department_id = st.number_input("Department ID", min_value=1, step=1)
research_interest = st.text_input("Research Interest")
year = st.number_input("Year", min_value=1, step=1)
major = st.text_input("Major")
student_type = st.selectbox("Student Type", ["Graduate"])

# Submit button to create the student profile
if st.button("Create Profile", type="primary"):
    if first_name and last_name and email and skill_id and department_id and research_interest and year and major:
        # Prepare the data to send to the API
        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "skill_id": skill_id,
            "department_id": department_id,
            "research_interest": research_interest,
            "year": year,
            "major": major,
            "student_type": student_type
        }

        # Send the POST request to the backend to add the student
        response = requests.post("http://api:4000/s/students", json=student_data)

        if response.status_code == 200:
            st.success("Graduate Student Profile successfully created!")
        else:
            st.error(f"Failed to create profile: {response.status_code} - {response.text}")
    else:
        st.warning("Please fill out all the required fields.")
        
# Back button to return to the home page
if st.button("Back"):
    st.switch_page('pages/10_Graduate_Home.py')