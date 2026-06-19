## Hugging Face Sentiment/ Topic Classifier

* This project encompasses sentiment analyses and topic classification using hugging face models. The final program is displayed beautifully via a streamlit web application.

## What it does (sentiment + topic classification)

This project helps you put a sentiment on your entered text i.e POSITIVE/ NEGATIVE. On top of that it scores the labels you entered, with providing it a score and then present the findings in a bar chart. 

## Models used (with links)

This projects utilizes two models
* Sentiment Analysis (distilbert-base-uncased-finetuned-sst-2-english)
* Topic Classification (facebook/bart-large-mnli)

## How to run it locally

To run this project on your system first 'git clone <repo-url>' from the github. Extract it and I have used VS Code for my project. Then run the requirements.txt to download all the required packages by cmd 'pip install -r requirements.txt'. Then from the terminal run the project with a cmd streamlit run app.py

## Example outputs (your screenshots go here)

To check the performance of my project I had it run some examples
1. "The service was okay, nothing special but not bad either." shows a similar pattern with POSITIVE label and a ~93.3% score. Additionally we get to see how clearly the model identifies the labels and score them appropriately. 
![Sentiment analysis example](screenshots/service_senti.png)
![Sentiment analysis example](screenshots/service_labels.png)
![Sentiment analysis example](screenshots/service_graph.png)

To see the range and understanding of the model and test the zero shot classification we have used variety of examples to test our model. 
1. "The cricket match went into a thrilling final over before India won." shows clear labeling i.e. sports: 0.876, entertainment: 0.117, health: 0.003, technology: 0.003, politics: 0.001. Thrilled to see the results
![Sentiment analysis example](screenshots/cricket_eg.png)
![Sentiment analysis example](screenshots/cricket_graph.png)


## Known limitations (your neutral-sentiment observation goes here!)

The model that we are using here is only trained on 2 labels which is positive and negative. So a sentence with ambiguous feelings also receives a strong score. E.g. "Honestly not sure how I feel about the ending of that movie." gets NEGATIVE label with ~99.7% score. This is a known limitation of the base sentiment model, not the app.
![Sentiment analysis example](screenshots/movie_senti.png)