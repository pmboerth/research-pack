import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is our CS 3200 Course Project app called Research Pack.  

    The goal of this app to allow for students and professors alike to find opportunities or people with interests in opportunities at Northeastern. 
    This app will simplify the talent search process within research projects and promote greater collaboration! 

    Stay tuned for more information and features to come!
    """
        )
