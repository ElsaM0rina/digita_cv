import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV Elsa| "
PAGE_ICON = ":smile:"
NAME = "Elsa Morina"
DESCRIPTION = """
Data Scientist  in spatial-sensor data and data-driven decision-making.
"""

EMAIL = "elsamorina@example.com"
LINKEDIN_URL = "https://www.linkedin.com/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/Hello World.pdf"
profile_pic_file = "assets/images.jpg"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- Recent Computer Science graduate with a strong foundation in software development, data analytics, and machine learning.

- Hands-on experience working with Python, SQL, and modern data tools through professional and academic projects.

- Skilled in data analysis, visualization, and building machine learning solutions to support decision-making.

- Strong problem-solving, communication, and teaching abilities developed through industry and educational roles.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Technical Skills")
    st.write(
        """
- Python (Pandas, NumPy, Scikit-learn, FastAPI)
- SQL, DBT, Airflow
- PowerBI, Streamlit
- PostgreSQL, Snowflake, AWS
- Machine Learning & Data Analytics
"""
    )

    # --- Relevant Expereince ---
    st.write("\n")
    st.subheader("Relevant Experience")
    st.write("---")

    # --- EXP 1
    st.write("**Machine Learning Projects**")
    #st.write("11/2023 - 11/2024")
    st.write(
        """
- Developed classification and prediction models using Python and Scikit-learn.
- Performed data cleaning, feature engineering, and model evaluation.
- Applied machine learning techniques to solve real-world business problems.
"""
    )

    # --- EXP 2
    st.write("\n")
    st.write("**Data Analytics & Visualization**")
    #st.write("10/2021 - 08/2023")
    st.write(
        """
- Created interactive dashboards and reports using PowerBI and Streamlit.
- Analyzed large datasets to identify trends and generate actionable insights.
- Automated reporting processes using Python and SQL.
"""
    )

    # --- EXP 3
    st.write("\n")
    st.write("**Software Development Projects**")
    #st.write("05/2023 (Fixed-term)")
    st.write(
        """
- Built web applications and APIs using Python and FastAPI.
- Designed and managed relational databases using PostgreSQL.
- Worked with cloud and data platforms to support scalable applications.
"""
    )
    st.write("---")


elif page == "About":
    st.title("About Me")
    st.write("""
    Recent Computer Science graduate with a strong interest in data science, 
    machine learning, and software development. 
    Experienced in Python, SQL, data analysis, and dashboard development through academic projects, teaching, and industry experience. Passionate about using data-driven solutions to solve real-world problems and continuously expanding technical expertise.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
