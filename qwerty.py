import nltk
from googlesearch import search
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from globalVariables import MDegree
from globalVariables import BDegree

stop_words = set(stopwords.words('english'))
token_list =[]

def samelinechecker(txt):
    # print("LINE IS : "+txt)
    collegename = ""
    result = ""

    tokenized = sent_tokenize(txt)
    # print (tokenized)
    for i in tokenized:
        # print(i)
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        # print(tagged[0])

    # print(tagged)
    token_list = ""
    for elem in tagged:
        #print(elem[0])
        token_list = token_list+elem[0]+" "

    # print(token_list)

    # for url in search(token_list,stop=10):
    #     if "ac.in" in url or "edu.in" in url:
    #         # print(url)
    #         collegename = token_list
    collegename = token_list

    for degree in MDegree:
        if degree in txt.lower():
            result = degree
            break
    for degree in BDegree:
        if degree in txt.lower():
            result = degree
            break

    return result , collegename

if __name__ == '__main__':
    print(samelinechecker("BTech in Computer Science with 64% in 2014, From Arya College of Engg. &I.T, Jaipur"))

