import streamlit as st
import requests
from PIL import Image

# App title
st.title("Smart News Summarizer and Presenter")
st.subheader("Your one-stop solution for summarized and engaging news updates")

# Sidebar for user preferences
st.sidebar.title("Preferences")
interests = st.sidebar.multiselect(
    "Select your interests:",
    ["Science", "Technology", "Politics", "Sports", "Entertainment", "Health"]
)
st.sidebar.write("You selected:", interests)

# Input: Allow user to search for news
search_query = st.text_input("Search for news topics (e.g., AI, Climate Change):", "")

# Button to fetch and summarize news
if st.button("Fetch News"):
    if search_query:
        st.write(f"Fetching news for: {search_query}")
        
        # Mockup news data (replace this with actual scraping/API calls)
        news_data = [
            {
                "title": "AI Revolution in 2025",
                "summary": "Artificial intelligence is transforming industries globally, from healthcare to transportation.",
                "image_url": "https://via.placeholder.com/150",
            },
            {
                "title": "Climate Change: A Call to Action",
                "summary": "Global leaders gather to discuss strategies for combating climate change.",
                "image_url": "https://via.placeholder.com/150",
            },
        ]

        for news in news_data:
            st.subheader(news["title"])
            st.image(news["image_url"], use_column_width=True)
            st.write(news["summary"])
            st.markdown("---")

    else:
        st.error("Please enter a search query.")

# Additional features
st.markdown("## Suggestions")

# Personalized Newsfeed
if st.checkbox("Personalized Newsfeed"):
    st.write("You will receive news tailored to your selected interests.")

# Audio Format Option
if st.checkbox("Enable Audio News Format"):
    st.write("Audio summaries will be available for the news articles.")

# Educational Mini Lessons
if st.checkbox("Include Educational Content"):
    st.write("Trending news will include brief educational insights.")

# Footer
st.markdown("---")
st.write("Powered by Django backend and Streamlit frontend.")
