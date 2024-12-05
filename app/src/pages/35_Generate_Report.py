import logging
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks
import numpy as np

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Student Engagement Report')

# Add a button to fetch and display the report
if st.button('Generate Engagement Report'):
    # Get all departments
    departments_response = requests.get('http://api:4000/d/departments')
    
    if departments_response.status_code == 200:
        departments = departments_response.json()

        department_ids = [department.get('DepartmentId') for department in departments]
        department_names = [department.get('Name') for department in departments]

        engagement_report = []

        # For each department, get the number of applications per research opportunity
        for department_id, department_name in zip(department_ids, department_names):
            # Fetch research opportunities for the department
            opportunities_response = requests.get(f'http://api:4000/o/opportunities/d{department_id}')

            if opportunities_response.status_code == 200:
                opportunities = opportunities_response.json()

                for opportunity in opportunities:
                    opportunity_id = opportunity.get('OpportunityId')
                    
                    # Fetch applications for each research opportunity
                    applications_response = requests.get(f'http://api:4000/a/opportunity/{opportunity_id}/applications')

                    if applications_response.status_code == 200:
                        applications = applications_response.json()
                        num_applications = len(applications)
                    else:
                        num_applications = 0  # If no applications, set to 0

                    engagement_report.append({
                        'Department': department_name,
                        'Research Opportunity': opportunity.get('Title', 'No Title'),
                        'Number of Applications': num_applications
                    })
            
            else:
                st.warning(f"Could not fetch research opportunities for {department_name}")

        # Calculate range, average, median, min, and max for each department
        department_report = {}

        for record in engagement_report:
            department_name = record['Department']
            num_applications = record['Number of Applications']

            if department_name not in department_report:
                department_report[department_name] = []

            department_report[department_name].append(num_applications)

        # Prepare a summary with range, average, median, min, and max
        summary_data = []
        
        for department_name, applications in department_report.items():
            if applications:  # Only calculate if data exists
                average_applications = np.mean(applications)
                median_applications = np.median(applications)
                min_applications = min(applications)
                max_applications = max(applications)
                range_applications = max(applications) - min(applications)
            else:
                range_applications = average_applications = median_applications = min_applications = max_applications = 0

            summary_data.append({
                'Department': department_name,
                'Range of Applications': range_applications,
                'Average Applications': average_applications,
                'Median Applications': median_applications,
                'Min Applications': min_applications,
                'Max Applications': max_applications
            })

        # Display the summary in a table
        if summary_data:
            df_summary = pd.DataFrame(summary_data)
            st.write(df_summary)
        else:
            st.warning("No engagement data available.")

    else:
        st.error("Failed to fetch department data. Please try again.")

# Back button 