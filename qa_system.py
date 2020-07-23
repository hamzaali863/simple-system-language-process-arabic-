# -*- coding: utf-8 -*-
'''QA system.ipynb'''

# install farasa tools
pip install farasapy





import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from nltk.corpus import words
from nltk.corpus import stopwords
#use it one time with internet 
nltk.download('punkt')
nltk.download('words')
nltk.download('stopwords')

stop=stopwords.words("arabic")
from farasa.pos import FarasaPOSTagger
from farasa.ner import FarasaNamedEntityRecognizer
from farasa.diacratizer import FarasaDiacritizer
from farasa.segmenter import FarasaSegmenter
from farasa.stemmer import FarasaStemmer
#send request to google and get answer 
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
def googleSearch(query):
    g_clean = [] #this is the list we store the search results
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query) #this is the actual query we are going to scrape

    html = requests.get(url)
    
    soup = BeautifulSoup(html.text, 'lxml')
    spans = soup.find_all('span', {'dir' : 'rtl'})

    lines = [span.get_text() for span in spans]

    return lines
# how many 
def how_many():
    ss=" ".join(results)
    print("\n word tokenize: ", word_tokenize(ss))
    stem_words= []
    w=word_tokenize(ss)
    for a in w:
        if a in stop:
             continue 
        stem_words.append(a)
        stem_sent= " ".join(stem_words)
    
    stemmer = FarasaStemmer()
    sample=stem_sent
    stemmed = stemmer.stem(sample)
   # print("sample stemmed:",stemmed)
    pos_tagger = FarasaPOSTagger()

    pos_tagged = pos_tagger.tag(stemmed)
   # print("sample POS Tagged",pos_tagged)
    
    a=word_tokenize(pos_tagged)
    s=[]
    for n in a:

        if "NUM-MP" in n:
            print(n[:-7])
            t=n[:-7]
            s.append(t)
        if "NUM-MS"  in n:     
            print(n[:-7])
            t=n[:-7]
            s.append(t)
            
    fr= nltk.FreqDist(s)
    keymax= max(fr,key=fr.get)     
    se=''
    quet= word_tokenize(question)
    for i in quet:
        if "كم" in quet:
            quet.remove("كم")
        if "؟" in quet:
            quet.remove("؟")    
    for z in quet:
        se +=z +" "

    print(se +keymax)

def who_qu():
    s=" ".join(results)

    stem_words= []
  
    print("\n word tokenize: ", word_tokenize(s))
    w=word_tokenize(s)
    for a in w:

        if a in stop:
             continue 
        stem_words.append(a)
        stem_sent= " ".join(stem_words)
    #print(stem_sent)
    #part of speach
    named_entity_recognizer_interactive = FarasaNamedEntityRecognizer(interactive=True)
    named_entity_recognized_interactive = named_entity_recognizer_interactive.recognize(stem_sent)
    NER=named_entity_recognized_interactive
    print("sample named entity recognized (interactive):",NER)
    # terminate the object to save resources:
    named_entity_recognizer_interactive.terminate()
   
    ner_token=word_tokenize(NER)
    FR=[]
    for i in ner_token:
      if "/B-PERS" in i:
        #print(i[:-7])
        FR.append(i[:-7])

    fr= nltk.FreqDist(FR)
    keymax= max(fr,key=fr.get)
    quet= word_tokenize(question)
    
    se=''
    for i in quet:
        if "من" in quet:
            quet.remove("من")
        if "؟" in quet:
            quet.remove("؟")
    for z in quet:
        se +=z +" "

    print(se +keymax)
#where 
def where():
    s=" ".join(results)
   
    stem_words= []
  
    print("\n word tokenize: ", word_tokenize(s))
    w=word_tokenize(s)
    for a in w:

        if a in stop:
             continue 
        stem_words.append(a)
        stem_sent= " ".join(stem_words)


    pos_tagger = FarasaPOSTagger()
    sample= stem_sent
    pos_tagged = pos_tagger.tag(stem_sent)
    print("sample POS Tagged",pos_tagged)    
    print(stem_sent)
    #part of speach
    named_entity_recognizer_interactive = FarasaNamedEntityRecognizer(interactive=True)
    named_entity_recognized_interactive = named_entity_recognizer_interactive.recognize(pos_tagged)
    NER=named_entity_recognized_interactive
    print("sample named entity recognized (interactive):",NER)
    # terminate the object to save resources:
    named_entity_recognizer_interactive.terminate()
   
    ner_token=word_tokenize(NER)
    FR=[]
    for i in ner_token:
      if "/B-LOC" in i:
        #print(i[:-6])
        FR.append(i[:-6])

    quet= word_tokenize(question)
                
    print("////////////////")            
    www=[]
    for a in FR:
        if a not in quet:
            www.append(a)
            #print(a)
    print(www)
    fr= nltk.FreqDist(www)
    keymax= max(fr,key=fr.get)
   
    
    se=''
    for i in quet:
        if "اين" in quet:
            quet.remove("اين")
        if "؟" in quet:
            quet.remove("؟")
    for z in quet:
        se +=z +" "

    print(se +"في "+keymax)

question = input('Enter question: ')
results = googleSearch(question)

for result in results:
    print(result + "\n")

if 'من'  in question :
    print('who')
    who_qu()
if 'كم' in question:
    print("how_many")
    how_many()
if 'اين' in question:    
    print("where")
    where()

