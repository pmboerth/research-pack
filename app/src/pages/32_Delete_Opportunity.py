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

# Display user greeting
st.write(f"### Hi, {st.session_state['first_name']}.")

# Fetch and display all research opportunities
if st.button('See All Research Opportunities', type='primary'):
    response = requests.get('http://api:4000/o/opportunities')
    
    if response.status_code == 200:
        opportunities = response.json()
        
        if opportunities:
            for opportunity in opportunities:
                opp_id = opportunity.get('OpportunityId', 'No ID')
                title = opportunity.get('Title', 'No Title')
                description = opportunity.get('Description', 'No Description')
                faculty = opportunity.get('FacultyName', 'No Faculty Name')
                department = opportunity.get('Department', 'No Department')
                
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                        <h3 style="margin-bottom: 5px; color: #4CAF50;">{title}</h3>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Description:</strong> {description}</p>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Faculty:</strong> {faculty}</p>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Department:</strong> {department}</p>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Opportunity ID:</strong> {opp_id}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Add a delete button for each opportunity
                if st.button(f"Delete {title}", key=f"delete_{opp_id}"):
                    delete_response = requests.delete(f'http://api:4000/research_opportunities/{opp_id}')
                    if delete_response.status_code == 200:
                        st.success(f"Successfully deleted {title}.")
                    else:
                        st.error(f"Failed to delete {title}. Please try again.")
        else:
            st.warning("No research opportunities available.")
    else:
        st.error("Failed to fetch research opportunities.")

# Back button to return to admin home page
if st.button("Back"):
    st.switch_page('pages/00_Admin_Home.py')