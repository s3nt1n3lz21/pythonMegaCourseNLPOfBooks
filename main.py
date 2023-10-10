import re
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

english_stopwords = stopwords.words("english")

def is_not_stopword(x):
    return x not in english_stopwords

with open("miracle_in_the_andes.txt", "r", encoding="utf-8") as file:
    book = file.read()
    pattern = re.compile("Chapter [0-9]+")
    chapters = re.findall(pattern, book)
    # print(chapters)

    # Get the sentences that contain the word 'love'
    pattern = re.compile("[A-Z0-9][^.]*[Ll]ove[^.]*.")
    sentences = re.findall(pattern, book)
    # print(sentences)
    # print(len(sentences))

    # What are the most used words
    pattern = re.compile("[a-zA-Z]+")
    words = re.findall(pattern, book.lower())
    words_filtered = filter(is_not_stopword, words)

    words_dict = dict()
    for word in words_filtered:
        number_occurences = words_dict.get(word)
        if number_occurences:
            words_dict[word] = number_occurences + 1
        else:
            words_dict[word] = 1

    sorted_words_dict = sorted(words_dict.items(), key=lambda x:x[1])
    # print(sorted_words_dict)

    # What are the most positive and negative chapters
    analyser = SentimentIntensityAnalyzer()

    pattern = re.compile("Chapter [0-9]+")
    chapters = re.split(pattern, book)
    chapters = chapters[1:]
    scores = [analyser.polarity_scores(chapter) for chapter in chapters]
    print(scores)
    positive_scores = [score.get('pos') for score in scores]
    negative_scores = [score.get('neg') for score in scores]

    figure = px.line(x=range(1,11), y=positive_scores, labels={"x": "Chapter", "y": "Score"})
    st.plotly_chart(figure)
    figure = px.line(x=range(1, 11), y=negative_scores, labels={"x": "Chapter", "y": "Score"})
    st.plotly_chart(figure)