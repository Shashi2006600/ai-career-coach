import streamlit as st

# Sample skill database
job_skills = {
    "Data Scientist": [
        "Python", "Machine Learning", "Statistics",
        "SQL", "Data Visualization"
    ],
    "AI Engineer": [
        "Python", "Deep Learning", "TensorFlow",
        "Machine Learning", "NLP"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Node.js"
    ]
}

st.title("AI Career Coach with Skill Gap Analysis")

name = st.text_input("Your Name")

target_role = st.selectbox(
    "Target Career Role",
    list(job_skills.keys())
)

user_skills = st.text_area(
    "Enter your skills (comma separated)"
)

if st.button("Analyze Skills"):

    user_skill_list = [
        skill.strip()
        for skill in user_skills.split(",")
        if skill.strip()
    ]

    required_skills = job_skills[target_role]

    matched = [
        skill for skill in required_skills
        if skill in user_skill_list
    ]

    missing = [
        skill for skill in required_skills
        if skill not in user_skill_list
    ]

    match_percentage = (
        len(matched) / len(required_skills)
    ) * 100

    st.subheader("Analysis Result")

    st.write(f"**Skill Match:** {match_percentage:.0f}%")

    st.write("### Skills You Have")
    st.write(matched)

    st.write("### Skill Gaps")
    st.write(missing)

    st.write("### Learning Roadmap")

    for skill in missing:
        st.write(f"📘 Learn {skill}")
#If you want to build an AI Career Coach with Skill Gap Analysis, a good approach is:
#Features
#User enters:
#Current skills
#Desired job role
#Experience level
AI analyzes:
Required skills for the target role
Missing skills (skill gap)
Learning recommendations
Displays:
Skill match percentage
Missing skills
Personalized learning roadmap
Simple Python (Streamlit) App
Python
Run the App
Install Streamlit:
Bash
pip install streamlit
Run:
Bash
streamlit run app.py
AI Enhancement (OpenAI Integration)
You can replace the fixed roadmap with AI-generated advice:
Python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = f"""
Current Skills: {user_skill_list}
Target Role: {target_role}
Missing Skills: {missing}

Create a 3-month learning roadmap.
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

roadmap = response.output_text
print(roadmap)
This turns the project into a full AI-powered career coach that gives personalized career guidance and skill-gap analysis.
