import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Research Opportunities')

# Add a button to use get all the research opportunities
results = requests.get('http://api:4000/o/opportunities').json()
  
# If there are results, format the opportunities and display them
if results:
    for opportunity in results:
        opportunity_id = opportunity.get('PositionId', 'No Id')
        position_name = opportunity.get('Name', 'No Title')
        research_area = opportunity.get('ResearchArea', 'No Research Area')
        description = opportunity.get('Description', 'No description available.')
        department_id = opportunity.get('DepartmentId', 'No Department')
        professor_id = opportunity.get('OwnerId', 'No Professor')
        created_at = opportunity.get('CreatedAt', 'No Date Available')
        
        result1 = requests.get(f'http://api:4000/d/departments/d{department_id}').json()
        department_name = result1[0].get('Name', 'No Name')
        
        result2 = requests.get(f'http://api:4000/pr/professors/p{professor_id}').json()
        professor_name = result2[0].get('FirstName') + " " + result2[0].get('LastName')
        
        # this HTML and CSS was generated by ChatGPT
        st.markdown(f"""
            <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                <h3 style="margin-bottom: 10px; color: #90AEAD;">{position_name}</h3>
                <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Research Area:</strong> {research_area}</p>
                <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Department:</strong> {department_name}</p>
                <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Professor:</strong> {professor_name}</p>
                <p style="margin-bottom: 12px; color: #D1D7DC;">{description}</p>
                <p style="margin-bottom: 6px; color: #D1D7DC;"><strong>Created At:</strong> {created_at}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Delete {position_name}", type="primary", key=f"delete_o{opportunity_id}"):
            response = requests.delete(f'http://api:4000/o/opportunities/p{opportunity_id}')
            
            if response.status_code == 200:
                st.success(f"Successfully deleted: {position_name}")
            else:
                st.error("Error when deleting opportunity, please verify input is correct")    
else:
    st.warning("No research opportunities")

# Button to go back to the home page
if st.button("Back"):
    st.switch_page('pages/30_Admin_Home.py')