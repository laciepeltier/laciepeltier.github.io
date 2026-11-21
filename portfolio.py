import streamlit as st
from typing import List, Dict


# PAGE SETUP

st.set_page_config(
    page_title="My Portfolio",
    page_icon=":wave:",
    layout="wide",
    menu_items={
        "Get Help": "https://www.example.com/help",
        "Report a bug": "https://www.example.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!"
    }    
)

# sample content
PROFILE = {
    "name": "Lacie Peltier",
    "role": "Data Scientist",
    "tagline": "Turning data into actionable insights.",
    "location": "New York, NY",
    "email": "lacie.peltier@example.com",
    "linkedin": "https://www.linkedin.com/in/laciepeltier",
    "github": "example.com/laciepeltier",

}

SKILLS: List[dict] = [
    {"name": "Python", "level": "Advanced"},
    {"name": "SQL", "level": "Intermediate"},
    {"name": "Machine Learning", "level": "Intermediate"},
]

EXPERIENCE: List[dict] = [
    {
        "company": "Tech Solutions Inc.",
        "role": "Data Scientist",
        "duration": "Jan 2020 - Present",
        "description": "Developed   ",
    }
]
PROJECTS: List[dict] = [
    {
        "name": "Customer Churn Prediction",
        "description": "Built a machine learning model to predict customer churn.",
        "technologies": ["Python", "scikit-learn", "Pandas"],
        "link": "lahdahdie.com",
    }
]
EDUCATION: List[dict] = [
    {
        "institution": "University of Data Science",
        "degree": "Master of Science in Data Science",
        "duration": "2018 - 2020",
    }
]

with st.sidebar:
    st.title("Welcome to My Portfolio")
    st.write("I am a professional i swear")

    st.markdown("""
    **Contact Information:**
    - Email: [lacie.peltier@example.com](mailto:lacie.peltier@example.com)
    - LinkedIn: [Lacie Peltier](https://www.linkedin.com/in/laciepeltier)
    - GitHub: [laciepeltier](https://github.com/laciepeltier)
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.button("Download Resume", on_click=lambda: st.download_button(
        label="Download Resume",
        data="resume.pdf",
        file_name="resume.pdf",
        mime="application/octet-stream"
    ))

# HEADER
left, right = st.columns([3, 1])
with left:
    st.markdown(f"##### {PROFILE['name']}", width=150)
    st.markdown(f"###### {PROFILE['role']}")
    st.markdown(f"###### {PROFILE['tagline']}")
    st.markdown(f"**Location:** {PROFILE['location']}")
    st.markdown(f"**Email:** {PROFILE['email']}")

st.markdown("<br>", unsafe_allow_html=True)

#tabs

tabs = st.tabs(["About", "Experience", "Projects", "Education"])

with tabs[0]:
    st.header("About Me")
    st.write("I am a passionate data scientist with experience in machine learning, data analysis, and visualization. I enjoy turning complex data into actionable insights.")  

with tabs[1]:
    st.header("Experience")
    for exp in EXPERIENCE:
        st.subheader(f"{exp['role']} at {exp['company']}")
        st.write(f"**Duration:** {exp['duration']}")
        st.write(f"**Description:** {exp['description']}")

with tabs[2]:
    st.header("Projects")
    for proj in PROJECTS:
        st.subheader(proj['name'])
        st.write(f"**Description:** {proj['description']}")
        st.write(f"**Technologies:** {', '.join(proj['technologies'])}")
        st.write(f"**Link:** [Project Link]({proj['link']})")

with tabs[3]:
    st.header("Education")
    for edu in EDUCATION:
        st.subheader(f"{edu['degree']} at {edu['institution']}")
        st.write(f"**Duration:** {edu['duration']}")    

        
