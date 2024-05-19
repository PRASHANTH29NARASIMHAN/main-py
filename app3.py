import streamlit as st
import pandas as pd
st.title('CRIMINAL DETECTION')
from PIL import Image
with Image.open('https://drive.google.com/file/d/1aUc_XtCjoy1Zv-ZsJbucBr-XY45UhEiX/view?usp=sharing') as img:
    img.show()
query = st.text_input('Enter the name of the criminal')
query = st.number_input('Enter the crimeId of the criminal')
start_date = st.date_input('Crime committed date', value=pd.Timestamp('2021-01-01'))
num_tweets = st.number_input('Number of cases filed on the crminal', min_value=1, max_value=1000)
submit = st.button('Search for crminal details')
