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
                student_name = result1[0].get('FirstName') + " " + result1[0].get('LastName')

                # Display each post using styled HTML
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                        <h3 style="margin-bottom: 5px; color: #4CAF50;">{post_title}</h3>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Group:</strong> {post_group}</p>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Student:</strong> {student_name}</p>
                        <p style="margin-bottom: 5px; color: #555;"><strong>Created At:</strong> {created_at}</p>
                        <p style="margin-bottom: 10px; color: #777;">{post_content}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No posts found for the selected group.")
    else:
        st.error(f"Error: {response.status_code}, {response.text}")



if st.button("Back"):
    st.switch_page('pages/00_Undergraduate_Home.py')
