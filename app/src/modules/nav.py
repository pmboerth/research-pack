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
    
def GraduateFindStudents():
    st.sidebar.page_link("pages/11_Find_Students.py", label="Students", icon="1️⃣")
    
def GraduateFindResearch():
    st.sidebar.page_link("pages/12_Find_Research.py", label="Research", icon="2️⃣")
    
def GraduateMakePost():
    st.sidebar.page_link("pages/13_Make_Post.py", label="Posts", icon="3️⃣")
    
def GraduateUpdateProfile():
    st.sidebar.page_link("pages/14_Make_Profile.py", label="Create Profile", icon="4️⃣")

def GraduateSeeApps():
    st.sidebar.page_link("pages/15_See_Applications.py", label="Applications", icon="5️⃣")
    
def GraduateAddComment():
    st.sidebar.page_link("pages/16_Add_Comment.py", label="Comments", icon="6️⃣")
    


## ------------------------ Role of professor --------------------------------
def ProfessorHome():
    st.sidebar.page_link("pages/20_Professor_Home.py", label="Professor Home", icon="0️⃣")
    
def ProfessorPostOpportunity():
    st.sidebar.page_link("pages/21_Post_Position.py", label="Post Position", icon="1️⃣")
    
def ViewMyOpps():
    st.sidebar.page_link("pages/22_Posted_Positions.py", label="View My Research Opportunities", icon="2️⃣")
    
def ViewStudentApps():
    st.sidebar.page_link("pages/23_All_Applications.py", label="View Applications", icon="3️⃣")
    
 
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

    # add a logo to the sidebar always
    st.sidebar.image("static/northeastern.png", use_container_width=True)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link and about link (the landing page)
        HomeNav()
        AboutPageNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If the user role is undergraduate_student, give them access to undergraduate pages
        if st.session_state["role"] == "undergraduate_student":
            UndergraduateStudentHome()
            ResearchOpportunities()
            SeePosts()
            MakePost()
            UpdateStudentInfo()

        # If the user role is graduate_student, give them access to graduate pages
        if st.session_state["role"] == "graduate_student":
            GraduateStudentHome()
            GraduateFindStudents()
            GraduateFindResearch()
            GraduateMakePost()
            GraduateUpdateProfile()
            GraduateSeeApps()
            GraduateAddComment()

        # If the user is an professor, give them access to the professor pages
        if st.session_state["role"] == "professor":
            ProfessorHome()
            ProfessorPostOpportunity()
            ViewMyOpps()
            ViewStudentApps()
            
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
