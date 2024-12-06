import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Add the sidebar navigation
SideBarLinks()

# Set the header for the page
st.title('Update Graduate Student Profile')

response = requests.get('http://api:4000/s/students/s2').json()

FirstName = response[0].get('FirstName', 'No First Name')
LastName = response[0].get('LastName')
Email = response[0].get('Email')
SkillId = response[0].get('SkillId')
DepartmentId = response[0].get('DepartmentId')
ResearchInterest = response[0].get('ResearchInterest')
Year = response[0].get('Year')
Major = response[0].get('Major')
StudentType = response[0].get('StudentType')

# Input fields for student profile details
first_name = st.text_input("First Name", value=FirstName)
last_name = st.text_input("Last Name", value=LastName)
email = st.text_input("Email", value=Email)
skill_id = st.number_input("Skill ID", min_value=1, step=1, value=SkillId)
department_id = st.number_input("Department ID", min_value=1, step=1, value=DepartmentId)
research_interest = st.text_input("Research Interest", value=ResearchInterest)
year = st.number_input("Year", min_value=1, step=1, value=Year)
major = st.text_input("Major", value=Major)
student_type = st.selectbox("Student Type", ["Graduate"])

# Submit button to create the student profile
if st.button("Update Profile", type="primary"):
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

    # Send the PUT request to the backend to update the student
    response = requests.put(f"http://api:4000/s/students/s{st.session_state['student_id']}", json=student_data)

    if response.status_code == 200:
        st.success("Graduate Student Profile successfully updated!")
    else:
        st.error(f"Failed to update profile: {response.status_code} - {response.text}")
        
# Back button to return to the home page
if st.button("Back"):
    st.switch_page('pages/10_Graduate_Home.py')