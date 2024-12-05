# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="🧠")


#### ------------------------ Role of undergraduate_student ------------------------
def UndergraduateStudentHome():
    st.sidebar.page_link(
        "pages/00_Undergraduate_Home.py", label="Undergraduate Home", icon="0️⃣"
    )

def ResearchOpportunities():
    st.sidebar.page_link(
        "pages/01_All_Opportunities.py", label="Research Opportunities", icon="1️⃣"
    )

def SeePosts():
    st.sidebar.page_link("pages/02_See_Posts.py", label="See Posts", icon="2️⃣")
    
def MakePost():
    st.sidebar.page_link("pages/03_Make_Post.py", label="Make Post", icon="3️⃣")
    
def UpdateStudentInfo():
    st.sidebar.page_link("pages/04_Update_Student_Information.py", label="Update Profile", icon="4️⃣")


## ------------------------ Role of graduate_student ------------------------
def GraduateStudentHome():
    st.sidebar.page_link("pages/10_Graduate_Home.py", label="Graduate Home", icon="0️⃣")


## ------------------------ Role of professor --------------------------------
def ProfessorHome():
    st.sidebar.page_link("pages/20_Professor_Home.py", label="Professor Home", icon="0️⃣")
    
## ------------------------ Role of admin -------------------------------------
def AdminHome():
    st.sidebar.page_link("pages/30_Admin_Home.py", label="Admin Home", icon="0️⃣")
    
def AdminResearchOpportunities():
    st.sidebar.page_link(
        "pages/31_All_Opps_Admin.py", label="Research Opportunities", icon="1️⃣")
    
def AllStudents():
    st.sidebar.page_link("pages/32_All_Students_Admin.py", label="Students", icon="2️⃣")
    

def GenerateReport():
    st.sidebar.page_link("pages/33_Generate_Report.py", label="Reports", icon="3️⃣")
    
def AdminUpdateStudentInfo():
    st.sidebar.page_link("pages/34_Update_Student.py", label="Update Student", icon="4️⃣")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/northeastern.png", use_container_width=True)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()
        AboutPageNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "undergraduate_student":
            UndergraduateStudentHome()
            ResearchOpportunities()
            SeePosts()
            MakePost()
            UpdateStudentInfo()

        # If the user role is graduate_student, show the corresponding pages
        if st.session_state["role"] == "graduate_student":
            GraduateStudentHome()

        # If the user is an professor, give them access to the professor pages
        if st.session_state["role"] == "professor":
            ProfessorHome()
            
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "admin":
            AdminHome()
            AdminResearchOpportunities()
            AllStudents()
            GenerateReport()
            AdminUpdateStudentInfo()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            if "student_id" in st.session_state:
                del st.session_state["student_id"]
            if "professor_id" in st.session_state:
                del st.session_state["professor_id"]
            if "admin_id" in st.session_state:
                del st.session_state["admin_id"]
            st.switch_page("Home.py")
