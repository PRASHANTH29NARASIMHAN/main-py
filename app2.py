import streamlit as st
st.title('Twitter Scraper using snscraper')
query = st.text_input('Enter a keyword or hashtag')
start_date = st.date_input('Start date', value=pd.Timestamp('2021-01-01'))
end_date = st.date_input('End date', value=pd.Timestamp.now())
num_tweets = st.number_input('Number of tweets to scrape', min_value=1, max_value=1000)
submit = st.button('Scrape tweets')
