import streamlit as st
from transformers import pipeline
st.title("Sentiment Analysis")
st.write("This application is a Streamlit dashboard to analyze the sentiment of Text.")
text = st.text_area("Enter your text:", "Type here...")
if st.button("Analyze"):
    classifier = pipeline("text-classification", model = "roberta-large-mnli")
    st.text("Sentiment: " + str(classifier(text)))
    #classifier(text)
