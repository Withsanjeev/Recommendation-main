# app.py
import streamlit as st
import requests

# Streamlit Web App
st.title('Job Recommendation System')

# Input from user
title = st.selectbox('Search Job', ['Software Engineer', 'Data Scientist', 'Product Manager'])  # Example job titles

# Fetch recommendations from FastAPI backend
if st.button('Get Recommendations'):
    # URL for FastAPI backend (ensure FastAPI is running on port 8000)
    api_url = f"http://127.0.0.1:8000/recommend/?title={title}"
    
    try:
        # Make the GET request to the FastAPI server
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if we have recommended jobs
            jobs = data.get("recommended_jobs")
            if jobs:
                st.write("Recommended Jobs:")
                for job in jobs:
                    st.write(f"- {job}")
            else:
                st.write("No recommendations found.")
        else:
            st.write(f"Error: {response.status_code}")
    except Exception as e:
        st.write(f"Error connecting to the API: {e}")
