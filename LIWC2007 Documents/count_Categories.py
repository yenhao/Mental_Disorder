from __future__ import division, unicode_literals
import csv
import operator
import math
from textblob import TextBlob as tb
from decimal import *
from nltk.corpus import stopwords



def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)




phsycologicalWords = csv.reader(open("LIWC2007cats.dic",'rb'), delimiter = chr(9))
wordsToOutput = csv.writer(open("category_Word_Count.csv",'wb'), delimiter = chr(9)) 

frontnumber1 = 1
my_dict ={}
category_List = {}

count = 0
for word in phsycologicalWords:
	#category_List[word]

	for w in word[1:]:
		#print w,
		if w != "":
			if w not in category_List:
				category_List[w] = []
				
			count+=1
			category_List[w].append(word[0])

		#if w!= "" and word[0] not in category_List[w]:	
			
			
	my_dict [word[0]] = count


	#print count	
	count = 0	
	#print "\n"
print(category_List)

'''
for key,value in sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True):
	#print key,value
	wordsToOutput.writerow([str(key),str(value)])


bloblist = []
bloblistcategory =[]

countdoc= 0

for key,value in category_List.items():
	doc = tb(' '.join(value))
	countdoc+=1
	#print doc
	bloblist.append(doc)
	bloblistcategory.append(key)
	#print doc
#print countdoc	
#print bloblist[0]
countwords = 0
frontnumber1 = 1

#tfidftop20 = csv.writer(open("TFIDF_top_20.csv",'wb'), delimiter = chr(9)) 
#tfidftop50 = csv.writer(open("TFIDF_top_50.csv",'wb'), delimiter = chr(9)) 
#tfidftop100 = csv.writer(open("TFIDF_top_100.csv",'wb'), delimiter = chr(9)) 
#tfidftop200 = csv.writer(open("TFIDF_top_200.csv",'wb'), delimiter = chr(9))
all = csv.writer(open("all.csv",'wb'), delimiter = chr(9))
storewords = []


for i, blob in enumerate(bloblist):
	#print ("Top words in document:"),bloblistcategory[i]

	scores = {word: tfidf(word, blob, bloblist) for word in blob.split(" ")}

	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	#print sorted_words
	for word, score in sorted_words:
		#countwords+=1
		#print word
		#break
		if word not in storewords:
			storewords.append(word)
		#print("\tWord: {}, TF-IDF: {}".format(word, round(score, 7)))
		#tfidftop20.writerow([str(frontnumber1),str(word)])

for wd in storewords:
	#all.writerow([str(frontnumber1),str(wd)])
	countwords+=1
	#print wd

print countwords

'''
