import streamlit as st
import os
from google import genai
from dotenv import load_dotenv


# 1. Load local .env (Only works on your laptop)
load_dotenv()

# 2. THE FAIL-SAFE KEY CHECK
api_key = None

# First: Try the Web Secrets (Streamlit Cloud)
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    # If secrets.toml is missing (Local Dev), we ignore the error
    pass

# Second: If Web Secrets failed, check Local .env
if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

# Third: If both failed, check Session State (Manual User Input)
if not api_key and "user_api_key" in st.session_state:
    api_key = st.session_state.user_api_key

# 3. USER INPUT FALLBACK (The Friend Fix)
if not api_key:
    st.warning("🔑 Gemini API Key not found.")
    user_input = st.text_input("Please enter your API Key to continue:", type="password")
    if user_input:
        st.session_state.user_api_key = user_input
        st.rerun()
    else:
        st.info("You can get a free key at [Google AI Studio](https://aistudio.google.com)")
        st.stop()


# 4. INITIALIZE CLIENT
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Failed to initialize Gemini client: {e}")
    st.stop()



st.title("Talk to Your Chatbot! 🤖💬")
st.write("This app demonstrates a conversational agent using Google Gemini. The agent can answer questions, provide information and engage in a dialogue with the user. The agent will become autonomous with upgrades over time.")
user_input = st.text_input("Ask Your Question Here")
if st.button("Click Enter"):
    with st.spinner("Thinking for response..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=user_input
        )    
    st.write(response.text)