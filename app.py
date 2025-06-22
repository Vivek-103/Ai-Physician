import streamlit as st
from utils import listen_to_user, speak
from PIL import Image
import google.generativeai as genai 


genai.configure(api_key="********************")  
model = genai.GenerativeModel("*****")  

st.title("AI Physician - Voice-Based Medical Assistant")

st.markdown("### Step 1: Describe Your Problem (Voice Input)")
if st.button("Start Recording"):
    user_query = listen_to_user()
    st.success(f"You said: {user_query}")

    st.session_state.user_query = user_query

uploaded_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

if st.button("Consult Doctor"):
    query = st.session_state.get("user_query", "")
    inputs = [query]
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        inputs.append(image)
    response = model.generate_content(inputs)
    answer = response.text

    st.markdown("### Prescription")
    st.write(answer)
    speak(answer)
