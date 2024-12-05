import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks(show_home=True)

st.write("# About this App")

st.markdown (
    """
    This app is called Research Pack, our CS 3200 Course Project.

    The goal of this app to allow for students and professors alike to find opportunities or people with interests in opportunities at Northeastern. 
    This app will simplify the talent search process within research projects and promote greater collaboration! 

    Students and professors can search and apply for opportunities as well as post and browse through posts about research opportunities on campus. 

    Stay tuned for more information and features to come!
    """
        )

