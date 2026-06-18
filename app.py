import streamlit as st
import pandas as pd
from classifier import analyze_senti, topic_classification

def make_list(labs):
    return labs.split(',')

#text box for sentence input
sentence = st.text_area("Enter a sentence for analyzing")

#text box for labels
labels= st.text_area("Write your labels, sepearated by comma")

#button to submit and trigger function
if st.button("Submit"):
    st.write("Sentiment Analysis Result:")
    st.write(analyze_senti(sentence))
    st.write("Topic Classification Results:")
    topic_result = topic_classification(sentence, make_list(labels))
    st.write(topic_result)

    #display results in a nice format
    st.bar_chart(dict(zip(topic_result['labels'], topic_result['scores']))) 