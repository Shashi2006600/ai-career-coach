import os
import streamlit as st
from google import genai
from google.genai import types

# Initialize the Gemini Client
# It automatically picks up the GEMINI_API_KEY environment variable
try:
    client = genai.Client()
except Exception as e:
    st.error(f"Failed to initialize Gemini Client. Ensure GEMINI_API_KEY is set. Error: {e}")
    st.stop()

# Configure the Streamlit Page
st.set_page_config(
    page_title="AI Career Coach & Skill Gap Analyzer",
    page_icon="💼",
    layout="wide"
)

# App Header
st.title("💼 AI Career Coach & Skill Gap Analyzer")
st.markdown("""
    Upload your profile or paste your skills, define your target role, 
    and let the AI analyze your gaps and construct a learning roadmap.
""")

st.divider()

# Sidebar Configuration
st.sidebar.header("🎯 Target Goals")
target_role = st.sidebar.text_input(
    "Target Job Role", 
    placeholder="e.g., Data Scientist, DevOps Engineer, Full Stack Developer"
)

target_industry = st.sidebar.text_input(
    "Target Industry/Domain", 
    placeholder="e.g., FinTech, Healthcare, E-commerce"
)

# Layout: Two columns for input and output
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("📝 Your Profile Input")
    
    # Input Type Toggle
    input_method = st.radio(
        "Choose how to provide your current profile:",
        ["Paste Current Skills & Experience", "Upload Resume text"]
    )
    
    user_profile = ""
    if input_method == "Paste Current Skills & Experience":
        user_profile = st.text_area(
            "Paste your current skills, tools known, and brief experience:",
            height=300,
            placeholder="Skills: Python, SQL, Basic Machine Learning...\nExperience: 1 year as a Data Analyst..."
        )
    else:
        # For simplicity without needing heavy PDF parsing libraries like PyPDF2, 
        # we accept standard text/md files, or you can paste the text.
        uploaded_file = st.file_uploader("Upload your resume as a text file (.txt)", type=["txt"])
        if uploaded_file is not None:
            user_profile = uploaded_file.read().decode("utf-8")
            st.success("Resume text loaded successfully!")

    analyze_button = st.button("🚀 Analyze Skill Gap & Get Advice", type="primary")

with col2:
    st.subheader("📊 AI Coach Evaluation")
    
    if analyze_button:
        if not target_role:
            st.warning("Please specify a Target Job Role in the sidebar.")
        elif not user_profile.strip():
            st.warning("Please provide your current profile or skills text.")
        else:
            with st.spinner("Analyzing your profile against industry standards..."):
                
                # Construct a strict prompt enforcing structured breakdown
                prompt = f"""
                You are an expert AI Career Coach and Technical Recruiter. 
                Analyze the user's current profile against their desired target role.
                
                TARGET ROLE: {target_role}
                TARGET INDUSTRY: {target_industry if target_industry else 'General Tech/Relevant Industry'}
                
                USER PROFILE:
                \"\"\"
                {user_profile}
                \"\"\"
                
                Provide a structured response with the following markdown headers:
                1. ## 🎯 Core Match Assessment: Short summary of how close they are to the role.
                2. ## ❌ Critical Skill Gaps: Bullet points of missing technical skills, tools, or domain knowledge.
                3. ## 📈 Personalized 3-Step Learning Roadmap: A clear, actionable path to bridge the gap.
                4. ## 💼 Interview & Resume Tips: Tailored advice for this specific transition.
                """
                
                try:
                    # Using the standard gemini-2.5-flash model for fast, structured text analysis
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"An error occurred during generation: {e}")
    else:
        st.info("Fill out your target role and profile details, then click 'Analyze Skill Gap' to view your coaching insights.")
