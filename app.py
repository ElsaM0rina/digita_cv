import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV Elsa| "
PAGE_ICON = ":smile:"
NAME = "Elsa Morina"
DESCRIPTION = """
Data Scientist  & AI Engineer in the making.
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
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects", "page lecture_12"])

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

elif page == "Projects":
    st.title("Project Frontend 1")
    st.write(f"""
    This project is a full-stack software application designed to solve real-world problems through an intuitive user interface and efficient backend architecture. It incorporates modern development practices, scalable design patterns, and secure data management to deliver a reliable and user-friendly experience. The application includes features such as user authentication, data processing, responsive design, and API integration. The project demonstrates proficiency in software development, database management, system design, and deployment workflows while emphasizing code quality, maintainability, and performance optimization.
    """)
    st.write("\n")
    st.title("Project Frontend 2")
    st.write(f"""
    This project is a full-stack software application designed to solve real-world problems through an intuitive user interface and efficient backend architecture. It incorporates modern development practices, scalable design patterns, and secure data management to deliver a reliable and user-friendly experience. The application includes features such as user authentication, data processing, responsive design, and API integration. The project demonstrates proficiency in software development, database management, system design, and deployment workflows while emphasizing code quality, maintainability, and performance optimization.
    """)

elif page == "page lecture_12":
    st.title("Lecture 12 - SQL")
    st.write(f"""
    SQL Basics

SQL stands for Structured Query Language. It is used to communicate with relational databases. With SQL, you can create databases and tables, insert data, read data, update existing data, delete data, and manage relationships between tables.

The most common SQL command is SELECT, which is used to retrieve data from a table.

Example:

SELECT column_name
FROM table_name
WHERE condition;

Important SQL commands include SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, ALTER TABLE, and DROP TABLE.

SQL also includes clauses such as WHERE for filtering, ORDER BY for sorting, GROUP BY for grouping results, and JOIN for combining data from multiple tables.

SQL constraints help control the data stored in a database. Common constraints include PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and CHECK.

Star Schema and Snowflake Schema

Star schema and snowflake schema are database designs used mainly in data warehouses.

A star schema has one central fact table connected directly to several dimension tables. The fact table usually stores measurable business data, such as sales amount or quantity sold. The dimension tables store descriptive data, such as customer, product, time, or location information.

A star schema is simple, easy to understand, and fast for reporting because it requires fewer joins. However, it may contain repeated data because dimension tables are usually not fully normalized.

A snowflake schema is a more normalized version of the star schema. In a snowflake schema, dimension tables are split into smaller related tables. This reduces data redundancy and saves storage space, but it also makes queries more complex because more joins are required.

In simple terms, a star schema is better for speed and simplicity, while a snowflake schema is better for reducing duplicated data and improving organization.

Database Normalization

Database normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It usually involves splitting large tables into smaller related tables and connecting them with keys.

The goal of normalization is to make sure each piece of data is stored in the correct place and only stored once when possible.

Normalization helps prevent common database problems called anomalies. An insertion anomaly happens when you cannot add data because other unrelated data is missing. An update anomaly happens when the same data exists in many places and must be updated multiple times. A deletion anomaly happens when deleting one piece of data accidentally removes other important information.

Normalization improves consistency, reduces duplicated data, and makes databases easier to maintain.

Normal Forms

Normal forms are levels of normalization.

First Normal Form, or 1NF, means that each column should contain atomic values. This means each field should store only one value, not a list of values.

Second Normal Form, or 2NF, means the table must already be in 1NF, and every non-key column must depend on the whole primary key.

Third Normal Form, or 3NF, means the table must already be in 2NF, and non-key columns should not depend on other non-key columns.

BCNF, or Boyce-Codd Normal Form, is a stronger version of 3NF. It requires every determinant to be a candidate key.

Fourth Normal Form, or 4NF, deals with removing multivalued dependencies.

Fifth Normal Form, or 5NF, deals with complex join dependencies.

In most practical database design, 1NF, 2NF, and 3NF are the most commonly used.

Slowly Changing Dimensions

Slowly Changing Dimensions, or SCDs, are used in data warehouses to manage changes in dimension data over time.

A dimension contains descriptive information, such as customer name, address, product category, or employee department. Sometimes this information changes slowly over time. For example, a customer may move to a new address, or an employee may change departments.

SCDs define how these changes should be stored.

Type 0 means the value never changes. Historical values are kept fixed.

Type 1 means the old value is overwritten with the new value. No history is kept.

Type 2 means a new row is added each time a change happens. This keeps full history.

Type 3 means a new column is added to store limited previous information, such as previous address.

Type 4 means historical data is stored in a separate history table.

Type 5 combines mini-dimensions with Type 1 behavior.

Type 6 is a hybrid approach that combines Type 1, Type 2, and Type 3.

SCDs are useful because they allow businesses to track history, analyze changes over time, and keep accurate reports. However, they can also make databases larger and more complex.

SQL Relationships

SQL relationships describe how tables are connected to each other. These relationships are usually created using primary keys and foreign keys.

A primary key uniquely identifies each row in a table. A foreign key is a column in one table that refers to the primary key of another table.

There are three main types of relationships in SQL: one-to-one, one-to-many, and many-to-many.

A one-to-one relationship means one row in one table is connected to one row in another table. For example, one user may have one user profile.

A one-to-many relationship means one row in one table can be connected to many rows in another table. For example, one department can have many employees.

A many-to-many relationship means many rows in one table can be connected to many rows in another table. For example, many students can enroll in many courses. This type of relationship needs a junction table, also called a linking table, to connect the two tables.

Overall Summary

These topics are all connected to database design and data management.

SQL is the language used to create, manage, and query relational databases. Relationships explain how tables are connected. Normalization explains how to organize tables properly and reduce duplicated data. Star schema and snowflake schema explain how data warehouses are designed for reporting and analysis. Slowly Changing Dimensions explain how data warehouses manage historical changes in descriptive data.

A simple way to remember them is:

SQL is the language used to work with databases.

Relationships connect tables together.

Normalization organizes data cleanly.

Star and snowflake schemas organize data warehouses.

Slowly Changing Dimensions track changes over time.""")

