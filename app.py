import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=my_key)


st.title("Talk to Agent")
st.write("This app demonstrates a conversational agent using Google Gemini. The agent can answer questions, provide information, and engage in a dialogue with the user.")

uder_input = st.text_input("Ask Your Question Here")
if st.button("Submit"):
    with st.spinner("Generating response..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=user_input
        )    
    st.write(response.text)