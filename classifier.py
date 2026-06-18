from transformers import pipeline
analyzer= pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
classifier= pipeline("zero-shot-classification", model='facebook/bart-large-mnli')


def analyze_senti(data):
    return analyzer(data)

def topic_classification(data, labels):
    return classifier(data, labels)

# if __name__ == "__main__":
#     print(analyze_senti("I love learning new things."))
#     print(topic_classification("I love learning new things.", ["art", "learning", "studies"]))