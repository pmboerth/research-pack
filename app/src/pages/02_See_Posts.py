import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Find Posts By Group')

selected_option = st.selectbox("Choose an Group:", ["Engineering", "Computer Science", 
                                                    "Science", "Health Science", "Social Science", "Business"])

if st.button("Submit",
             type='primary'):
    response = requests.get(f'http://api:4000/p/posts/{selected_option}')
    
    if response.status_code == 200:
        results = response.json()

        if results:
            for post in results:
                post_title = post.get('PostTitle', 'No Title')
                post_content = post.get('PostContent', 'No Content Available')
                creator_id = post.get('CreatorId', 'Unknown')
                created_at = post.get('CreatedAt', 'No Date Available')
                updated_at = post.get('UpdatedAt', 'No Date Available')
                post_type = post.get('PostType', 'Unknown')
                post_group = post.get('PGroup', 'Unknown')
                
                result1 = requests.get(f'http://api:4000/s/students/s{creator_id}').json()
                student_name = result1[0].get('FirstName', 'Unknown') + " " + result1[0].get('LastName', '')

                # Display each post using styled HTML
                st.markdown(f"""
                    <div style="border: 1px solid #3D4A59; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #3D4A59;">
                        <h3 style="margin-bottom: 10px; color: #90AEAD;">{post_title}</h3>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Group:</strong> {post_group}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Student:</strong> {student_name}</p>
                        <p style="margin-bottom: 8px; color: #D1D7DC;"><strong>Created At:</strong> {created_at}</p>
                        <p style="margin-bottom: 12px; color: #D1D7DC;">{post_content}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No posts found for the selected group.")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")



if st.button("Back"):
    st.switch_page('pages/00_Undergraduate_Home.py')
