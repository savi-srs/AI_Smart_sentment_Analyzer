import streamlit as st
import google.generativeai as genai
import os

# 1. CLOUD ENGINE CONFIGURATION
# Local testing fallback variable. 
# REMINDER: Clear this out before pushing code to public repositories!
#API_KEY = "YOUR_GOOGLE_AI_STUDIO_KEY" 
API_KEY = st.secrets["API_KEY"]


genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. WEB USER INTERFACE (STREAMLIT DASHBOARD)
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="😊")
st.title("😊 Smart Sentiment Analyzer")
st.markdown("Instantly evaluate and classify the underlying human emotion within written text or customer feedback.")

# Multiline text block input container
user_text = st.text_area("Paste the text or customer feedback you want to analyze here:", height=200)

# 3. CORE PROCESSING PIPELINE
if st.button("Analyze Sentiment"):
    if not user_text:
        st.warning("Please enter some text before running the sentiment analysis engine!")
    else:
        with st.spinner("Decoding linguistic patterns and evaluating emotions..."):
            # The System Prompt defines the strict behavioral bounds for the model
            prompt = f"""
            You are an elite customer experience data scientist. Analyze the emotional tone of the provided text.
            
            TEXT TO EVALUATE:
            "{user_text}"
            
            Provide the response using this exact structured layout:
            
            ### 🏷️ Sentiment Classification
            State ONLY one of the following labels along with its designated emoji:
            * **Positive** 😊
            * **Negative** 😞
            * **Neutral** 😐
            
            ### 🔍 Analysis Justification
            Provide a clear, brief explanation of why the text falls under that sentiment label. Point out specific words, phrasing, or tones that influenced the decision.
            """

            try:
                # Dispatch data payloads to Google cloud infrastructure
                response = model.generate_content(prompt)
                
                st.subheader("Analysis Insights")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An API connection error occurred: {e}")
