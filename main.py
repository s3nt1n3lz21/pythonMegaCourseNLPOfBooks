import re
from nltk.corpus import stopwords

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
