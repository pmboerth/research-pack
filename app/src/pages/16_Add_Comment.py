import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Create a New Comment')

# Input fields for comment details
post_id = st.number_input("Enter the Post ID you want to add a Comment to:", min_value=1, step=1)
comment_content = st.text_area("Enter the Comment Content:")

# Submit comment if fields are filled and call the API
if st.button("Submit Comment", type="primary"):
    if post_id and comment_content:
        comment = {
            "post_id": post_id,
            "owner_id": st.session_state['student_id'],
            "comment_content": comment_content
        }
        
        response = requests.post(f"http://api:4000/c/comments/p{post_id}", json=comment)
        
        if response.status_code == 200:
            st.success("Comment successfully added!")
        else:
            st.error("Failed to add comment, please verify correct inputs")
    else:
        st.warning("Please fill out all required fields.")

# Button to go back to the home page
if st.button("Back"):
    st.switch_page('pages/10_Graduate_Home.py')