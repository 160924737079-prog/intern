import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 1. Page Configuration
st.set_page_config(
    page_title="YOUR GUID INTERN ASSISTANT",
    page_icon="🏢",
    layout="centered"
)

# 2. Custom CSS for Premium Minimalist Light Background & Ultra-Visible Typography
st.markdown(
    """
    <style>
    /* Clean, bright, light abstract background */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Strong overlay to guarantee bright workspace visibility */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(255, 255, 255, 0.92); 
        z-index: -1;
    }

    /* Opaque Crisp White Container for Information Cards */
    .main-container {
        background-color: #ffffff !important;
        padding: 28px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        border: 1px solid #E2E8F0;
    }
    
    /* Header Typography Colors override for dark visibility */
    h1, h2, h3, [data-testid="stHeader"] {
        color: #1E3A8A !important; /* Rich Navy Blue */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700 !important;
    }
    
    /* Dynamic fallback for general app-text color overrides */
    .clean-text {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #0F172A !important; /* Slate Black text */
        line-height: 1.6;
        font-size: 1.05rem;
    }

    /* Strictly enforcing crisp text visibility on native Streamlit markdown components */
    .stMarkdown p, label, span, .stTextArea p {
        color: #1E293B !important; 
        font-weight: 550 !important;
    }

    /* Input Fields text color assurance */
    .stTextArea textarea {
        color: #0F172A !important;
        background-color: #ffffff !important;
        border: 1px solid #CBD5E1 !important;
    }

    /* CRUCIAL FIX: Forcing response text and markdown inside notifications/info blocks to be dark and visible */
    .stAlert, div[data-testid="stNotification"], div[data-testid="stMarkdownContainer"] p, div[data-testid="stMarkdownContainer"] li {
        color: #0F172A !important;
        font-weight: 500 !important;
    }
    
    /* Ensuring inner element rendering inside warning/info boxes doesn't turn white */
    .stAlert p, .stAlert div {
        color: #0F172A !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Main UI Presentation
st.title("🏢 YOUR GUID INTERN ASSISTANT")

# Content card text setup
st.markdown(
    """
    <div class="main-container">
        <p class="clean-text" style="margin-bottom: 12px;"><strong>Welcome to the Intern Assistant!</strong> This chatbot is designed to assist you with tailored information and guidance related to internships. You can seamlessly ask questions about internship opportunities, the application process, and more.</p>
        <p class="clean-text">Please enter your query below, and the chatbot will provide you with relevant insights, techniques, and actionable suggestions to help you excel.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 4. User Input Section
question = st.text_area(
    "Enter your question here:",
    placeholder="Type your question about internships (e.g., resume tips, interview prep)...",
    height=150
)

# Button triggered action
if st.button("Ask Intern", use_container_width=True):
    if question.strip() == "":
        st.warning("Please type a question before submitting!")
    else:
        with st.spinner("Analyzing your query..."):
            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                temperature=0.0,
            )

            prompt = ChatPromptTemplate.from_template(
                """
                You are an INTERN Expert.

                Your job is to answer ONLY internship-related questions.

                Topics Include:
                - Internship Opportunities
                - Application Process
                - Resume and Cover Letter Tips
                - Interview Preparation
                - Networking and Professional Development
                - Career Growth
                - Industry Trends and Insights
                - Work-Life Balance
                - Company Culture
                - Mentorship and Guidance
                - Professional Etiquette
                - Professional Skills Development

                If the user asks anything outside of Internships, respond with the following message:
                "Sorry, I can only answer Internship-related questions. Please ask a question related to Internships."

                Question:
                {question}

                Provide:
                1. A clear and concise answer to the user's question.
                2. If the question is not related to internships, respond with the exact message above.
                3. Techniques, tips, and best practices for securing and excelling in internships.
                """
            )
            
            chain = prompt | llm
            response = chain.invoke({"question": question})
            
            # Distinctive Response UI Box
            st.markdown("### 📋 Response:")
            st.info(response.content)