"""
An example of how to extract a bag of models from given data.
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

count = CountVectorizer()
docs = np.array([
'The sun is shining',
'The weather is sweet',
'The sun is shining and the weather is sweet'])

bag = count.fit_transform(docs)
print(count.vocabulary_)		#this returns a directory

#to print the feature vectors
print(bag.toarray())


"""
Implementing term frequency-inverse document frequency

	tf-idf(i,d) = tf(i,d) x idf(t,d)

	td(i,d) = term frequency
	idf(t,d) = 	log(n/1+df(t,d))	---> inverse document frequency

				==> df(t,d) --> no. of documents d that contain the term t

	====> Basically as the number of occurrences of a word increases, its value in giving meaningful information decreases

"""

tfidf = TfidfTransformer()
np.set_printoptions(precision=2)
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())
