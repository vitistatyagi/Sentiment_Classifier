import streamlit as st
import pandas as pd
from classifier import analyze_senti, topic_classification

def make_list(labs):
    return labs.split(',')

#heading and subheading
st.title("Sentiment Analysis and Topic Classification")
st.subheader("Get the sentiment of your senetence and classify into labels.")

#text box for sentence input
sentence = st.text_area("Enter a text you want to analyze")

#text box for labels
labels= st.text_area("Write your labels, separated by comma", placeholder="technology, sports, politics, art")

#button to submit and trigger function
if st.button("Submit"):
    st.write("Sentiment Analysis Result:")
    st.write(analyze_senti(sentence))
    st.write("Topic Classification Results:")
    topic_result = topic_classification(sentence, make_list(labels))
    st.write(topic_result)

    #display results in a nice format
    st.bar_chart(dict(zip(topic_result['labels'], topic_result['scores']))) 