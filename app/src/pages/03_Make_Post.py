import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Create a New Post')

# Input fields for post details
post_title = st.text_input("Enter a Post Title:")
post_content = st.text_area("Enter the Post Content:")
post_type = st.selectbox("Choose an Post Type:", ["Question", "Collaboration"])
post_group = st.selectbox("Choose a Post Group:", ["Engineering", "Computer Science", 
                                                   "Science", "Health Science", "Social Science", "Business"])

# Submit post if fields are filled and call the API
if st.button("Submit Post",
             type="primary"):
    if post_title and post_content:
        
        post = {
            "post_title": post_title,
            "post_content": post_content,
            "post_type": post_type,
            "group": post_group
        }
        
        response = requests.post("http://api:4000/p/posts", json=post)
        
        if response.status_code == 200:
            st.success("Post successfully added!")
        else:
            st.error(f"Failed to add post: {response.status_code} - {response.text}")
    else:
        st.warning("Please fill out all required fields.")

# Button to go back to the home page    
if st.button("Back"):
    st.switch_page('pages/00_Undergraduate_Home.py')

