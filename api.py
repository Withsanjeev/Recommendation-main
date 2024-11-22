# api.py
from fastapi import FastAPI
import pickle
import pandas as pd
from typing import List

# Load the recommendation data (df.pkl and similarity.pkl should be present in your directory)
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Create FastAPI instance
app = FastAPI()  # This should be defined in api.py

# Function to provide job recommendations based on a job title
def recommendation(title: str) -> List[str]:
    try:
        idx = df[df['Title'] == title].index[0]
        idx = df.index.get_loc(idx)
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:20]
        jobs = [df.iloc[i[0]].Title for i in distances]
        return jobs
    except Exception as e:
        return {"error": str(e)}

# Route for getting job recommendations
@app.get("/recommend/")
def recommend(title: str):
    try:
        recommended_jobs = recommendation(title)
        return {"recommended_jobs": recommended_jobs}
    except Exception as e:
        return {"error": str(e)}

# Root route to check if the server is running
@app.get("/")
def read_root():
    return {"message": "Job Recommendation API is running!"}
