# EducationalAssistant
My final year project aims to help self-learners who use internet as their active source of knowledge. The project is expected to have 3 main modules namely:
<br>* Summarizing
<br>* Question answering
<br>* Integration of all learning platforms

## Summarising:
This part focuses on summarizing them for easy skimming over large contents.
### Input text:
<br>The system can get input text from pdfs by extracting text from them using PyPdf2 library and performing few cleansing to it.
<br>Similarly it can get inout from website links too. In order to cleanse the html format returned from webscraping, regular expressions are used.
### Summarizing Algorithm:
I have used TF-iDF algorithm to extract the most important setences.
<br>STEPS:
<br>- 1.Tokenise,Lemmatize and remove special characters.
<br>- 2.Take up noun and verb tokens which is basically the importance provider of a sentence.
<br>- 3.Find their frequencies.
<br>- 4.Calculate TF and IDF using the formulae.
![](/tfidf.png)
![](https://github.com/AthiraKarthe/EducationAssistant/blob/master/tfidf.jpg)
<br>-  5.Sort the sentences based on their importance score.
<br>- 6.Select the required percentage  of sentences from the sorted list.
<br>- 7.Return them in the order of their occurance.
<br>                                                   **TA-DA**:grin:
## Question answering:
It is a model that helps in identifying the answer to a question or doubt posed by the user. Inorder to do this, the system returns top results for the subjects(finds by PoS tagging) in the user query and searches for the best anwer from the documents retrieved. The question answering model can be trained with Stanford Question Answering dataset.
## Integration of all learning platforms
The idea is to bring in all the active courses in various MOOC platforms. This helps the users in keeping track of their active courses and schedule their day accordingly.
