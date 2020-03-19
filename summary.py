from nltk import pos_tag,word_tokenize,ne_chunk,tree2conlltags,sent_tokenize,PorterStemmer
from nltk.corpus import stopwords
import bs4 as BeautifulSoup
import re
import requests
import urllib
import urllib.request
import html5lib
import nltk
import os
import re
import math
import operator
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from math import ceil
# nltk.download('averaged_perceptron_tagger')

Stopwords = set(stopwords.words('english'))
wordlemmatizer = WordNetLemmatizer()
def lemmatize_words(words):
    lemmatized_words = []
    for word in words:
       lemmatized_words.append(wordlemmatizer.lemmatize(word))
    return lemmatized_words
def stem_words(words):
    stemmed_words = []
    for word in words:
       stemmed_words.append(stemmer.stem(word))
    return stemmed_words
def remove_special_characters(text):
    regex = r'[^a-zA-Z0-9\s]'
    text = re.sub(regex,'',text)
    return text
def freq(words):
    words = [word.lower() for word in words]
    dict_freq = {}
    words_unique = []
    for word in words:
       if word not in words_unique:
           words_unique.append(word)
    for word in words_unique:
       dict_freq[word] = words.count(word)
    return dict_freq
def pos_tagging(text):
    pos_tag = nltk.pos_tag(text.split())
    pos_tagged_noun_verb = []
    for word,tag in pos_tag:
        if tag == "NN" or tag == "NNP" or tag == "NNS" or tag == "VB" or tag == "VBD" or tag == "VBG" or tag == "VBN" or tag == "VBP" or tag == "VBZ":
             pos_tagged_noun_verb.append(word)
    return pos_tagged_noun_verb
def tf_score(word,sentence):
    freq_sum = 0
    word_frequency_in_sentence = 0
    len_sentence = len(sentence)
    for word_in_sentence in sentence.split():
        if word == word_in_sentence:
            word_frequency_in_sentence = word_frequency_in_sentence + 1
    tf =  word_frequency_in_sentence/ len_sentence
    return tf
def idf_score(no_of_sentences,word,sentences):
    no_of_sentence_containing_word = 0
    for sentence in sentences:
        sentence = remove_special_characters(str(sentence))
        sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.split()
        sentence = [word for word in sentence if word.lower() not in Stopwords and len(word)>1]
        sentence = [word.lower() for word in sentence]
        sentence = [wordlemmatizer.lemmatize(word) for word in sentence]
        if word in sentence:
            no_of_sentence_containing_word = no_of_sentence_containing_word + 1
    idf = math.log10(no_of_sentences/no_of_sentence_containing_word)
    return idf
def tf_idf_score(tf,idf):
    return tf*idf
def word_tfidf(dict_freq,word,sentences,sentence):
    word_tfidf = []
    tf = tf_score(word,sentence)
    idf = idf_score(len(sentences),word,sentences)
    tf_idf = tf_idf_score(tf,idf)
    return tf_idf
def sentence_importance(sentence,dict_freq,sentences):
     sentence_score = 0
     sentence = remove_special_characters(str(sentence)) 
     sentence = re.sub(r'\d+', '', sentence)
     pos_tagged_sentence = [] 
     no_of_sentences = len(sentences)
     pos_tagged_sentence = pos_tagging(sentence)
     for word in pos_tagged_sentence:
          if word.lower() not in Stopwords and len(word)>1: 
                word = word.lower()
                word = wordlemmatizer.lemmatize(word)
                sentence_score = sentence_score + word_tfidf(dict_freq,word,sentences,sentence)
     return sentence_score





import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

inp = input("Summarise pdf or link?")
if inp=='pdf':
		filename=input("enter the path of the pdf:")
		#open allows you to read the file
		pdfFileObj = open(filename,'rb')
		#The pdfReader variable is a readable object that will be parsed
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		#discerning the number of pages will allow us to parse through all #the pages
		num_pages = pdfReader.numPages
		count = 0
		text = ""
		#The while loop will read each page
		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			text += pageObj.extractText()
		#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
		if text != "":
   				text = text
		#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
		else:
   				text = textract.process(text, method='tesseract', language='eng')
		tokenized_sentence = sent_tokenize(str(text))

		
		
			
if inp=='link':
	link_to_crawl=input("enter the link to be summarised:")
	f = requests.get(link_to_crawl)
	# print(f.content)
	con=str(f.content)
	x=re.findall("<p[^>]*>([^<]+)</p>",con)
	x=str(x)
	tokenized_sentence=sent_tokenize(x)



text = remove_special_characters(str(tokenized_sentence))
text = re.sub(r'\d+', '', text)
tokenized_words_with_stopwords = word_tokenize(text)
tokenized_words = [word for word in tokenized_words_with_stopwords if word not in Stopwords]
tokenized_words = [word for word in tokenized_words if len(word) > 1]
tokenized_words = [word.lower() for word in tokenized_words]
tokenized_words = lemmatize_words(tokenized_words)
word_freq = freq(tokenized_words)
input_user = int(input('Percentage of information to retain(in percent):'))
no_of_sentences = int(ceil(input_user * len(tokenized_sentence))/100)
print(no_of_sentences)	
c = 1
sentence_with_importance = {}
for sent in tokenized_sentence:
	sentenceimp = sentence_importance(sent,word_freq,tokenized_sentence)
	sentence_with_importance[c] = sentenceimp
	c = c+1
sentence_with_importance = sorted(sentence_with_importance.items(), key=operator.itemgetter(1),reverse=True)
cnt = 0
summary = []
sentence_no = []
for words_prob in sentence_with_importance:
   		if cnt < no_of_sentences:
   			sentence_no.append(words_prob[0])
   			cnt = cnt+1
   		else:
   			break
sentence_no.sort()
cnt = 1
for sentence in tokenized_sentence:
	if cnt in sentence_no:
		summary.append(sentence)
	cnt = cnt+1
summary = " ".join(summary)
print("\n")
print("Summary:")
summary=re.sub("(\\n)","",summary)
sents=summary.split(',')
for s in sents:
	print(s)
