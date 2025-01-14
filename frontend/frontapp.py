import streamlit as st
import requests

# Title and description
st.title("CodeSense - Sentiment Analysis")
st.write("Enter text below to analyze its sentiment.")

# Input text field
text_input = st.text_area("Input Text", placeholder="Type your text here...")

# Analyze button
if st.button("Analyze Sentiment"):
    if text_input.strip():
        with st.spinner("Connecting to backend..."):
            try:
                # Send the input text to the Flask API
                response = requests.post(
                    "http://127.0.0.1:5000/analyze",  # Ensure Flask is running locally
                    json={"text": text_input},
                )

                # Check the response status
                if response.status_code == 200:
                    result = response.json()
                    st.success("Analysis Complete!")
                    st.write(f"**Sentiment:** {result[0]['label']}")
                    st.write(f"**Confidence Score:** {round(result[0]['score'], 2)}")
                else:
                    st.error(
                        f"Error from backend (Status {response.status_code}): {response.text}"
                    )
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter some text to analyze.")
