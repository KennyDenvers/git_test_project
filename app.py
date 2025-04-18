import streamlit as st
import requests

st.title("🌍 ESG News Dashboard")

# Your NewsAPI key goes here 👇
API_KEY = "49cb9690aeb64263ae1ec76360766d19"

# Step 1: Define the URL for ESG-related news
url = (
    f"https://newsapi.org/v2/everything?"
    f"q=ESG OR sustainability OR CSRD&"
    f"sortBy=publishedAt&"
    f"language=en&"
    f"apiKey={API_KEY}"
)

# Step 2: Fetch the data
response = requests.get(url)
data = response.json()

# Step 3: Display first article title to confirm it works
if data["status"] == "ok" and data["articles"]:
    st.success("Connection successful!")
    st.write("Top headline:", data["articles"][0]["title"])
else:
    st.error("Failed to fetch news. Check your API key or limit.")
