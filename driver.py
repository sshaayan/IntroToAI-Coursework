import pandas as pd
import os
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
import unicodedata
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer




#removes stopwords from a string
def removeStopWords(text):
	textList = text.split()
	newText = [word for word in textList if word.lower() not in stopWords]
	result = " ".join(newText)

	return result


rowNum = 0

#extracts data from text files and organizes them into one csv file
def imdb_data_preprocess(inpath, outpath, score):
	global rowNum

	ofile = open(outpath, "a")

	if os.stat(outpath).st_size == 0:
		header = ["row_number", "text", "polarity"]
		with ofile:
			writer = csv.writer(ofile)
			writer.writerow(header)

	reviews = []
	for filename in os.listdir(inpath):
		if filename == ".DS_Store":
			continue
		newPath = inpath + filename
		newIFile = open(newPath, "rU")
		with newIFile:
			row = newIFile.read().replace("\\", "")
			row = row.replace("<br /><br />", "")
			newRow = removeStopWords(row)
			reviews.append(newRow)

		newIFile.close()

	ofile = open(outpath, "a")
	with ofile:
		writer = csv.writer(ofile)
		for text in reviews:
			nextRow = [rowNum, text, score]
			writer.writerow(nextRow)
			rowNum += 1

	ofile.close()


#creates a unigram model from the given text data
def unigram(textData):
	uniCV = CountVectorizer(analyzer = 'word', ngram_range = (1, 1), vocabulary = vocab)
	uniModel = uniCV.fit_transform(textData)
	return uniModel


#creates a bigram model from the given text data
def bigram(textData):
	biCV = CountVectorizer(analyzer = 'word', ngram_range = (1, 2), vocabulary = vocab)
	biModel = biCV.fit_transform(textData)
	return biModel


#creates tfidf unigram model from the given text data
def tfidf_unigram(textData):
	tfidfUniCV = TfidfVectorizer(analyzer = "word", ngram_range = (1, 1), vocabulary = vocab)
	tfidfUniModel = tfidfUniCV.fit_transform(textData)
	return tfidfUniModel


#creates tfidf bigram model from the given text data
def tfidf_bigram(textData):
	tfidfBiCV = TfidfVectorizer(analyzer = 'word', ngram_range = (1, 2), vocabulary = vocab)
	tfidfBiModel = tfidfBiCV.fit_transform(textData)
	return tfidfBiModel


#creates a tf-idf model from either a unigram or a bigram model
def tf_idf(model):
	transformer = TfidfTransformer(norm = "l1")
	newModel = transformer.fit_transform(model)
	return newModel


stopWords = []
sw_ifile = open("stopwords.en.txt", "rU")
with sw_ifile:
	for line in sw_ifile:
		addLine = line.replace("\n", "")
		stopWords.append(str(addLine))
sw_ifile.close()

output = "imdb_tr.csv"
negative = "../resource/lib/publicdata/aclImdb/train/neg/"
positive = "../resource/lib/publicdata/aclImdb/train/pos/"

imdb_data_preprocess(negative, output, 0)
imdb_data_preprocess(positive, output, 1)

trainText = []
trainY = []
tr_ifile = open(output, "rU")
with tr_ifile:
	reader = csv.reader(tr_ifile)
	next(reader, None)
	for row in reader:
		trainText.append(row[1])
		trainY.append(row[2])
tr_ifile.close()

trainUnigram = unigram(trainText)
trainBigram = bigram(trainText)
trainUniTF = tfidf_unigram(trainText)
trainBiTF = tfidf_bigram(trainText)

unigram_clf = SGDClassifier(loss = "hinge", penalty = "l1")
unigram_clf.fit(trainUnigram, trainY)

bigram_clf = SGDClassifier(loss = "hinge", penalty = "l1")
bigram_clf.fit(trainBigram, trainY)

unigramTf_clf = SGDClassifier(loss = "hinge", penalty = "l1")
unigramTf_clf.fit(trainUniTF, trainY)

bigramTf_clf = SGDClassifier(loss = "hinge", penalty = "l1")
bigramTf_clf.fit(trainBiTF, trainY)

#test the classifiers on the test data
testText = []
te_ifile = open("../resource/asnlib/public/imdb_te.csv", "rU")
with te_ifile:
	reader = csv.reader(te_ifile)
	next(reader, None)
	for row in reader:
		newRow = ''.join(e for e in row[1] if e.isalnum() or e == " " or e == ".")
		testText.append(newRow)
te_ifile.close()

testUnigram = unigram(testText)
uni_testY = unigram_clf.predict(testUnigram)

testBigram = bigram(testText)
bi_testY = bigram_clf.predict(testBigram)

testUniTF = tfidf_unigram(testText)
uniTf_testY = unigramTf_clf.predict(testUniTF)

testBiTF = tfidf_bigram(testText)
biTf_testY = bigramTf_clf.predict(testBiTF)

#print the results to their respective text files
uni_ifile = open("unigram.output.txt", "a")
with uni_ifile:
	for label in uni_testY:
		uni_ifile.write(str(label) + "\n")
uni_ifile.close()

uniTF_ifile = open("unigramtfidf.output.txt", "a")
with uniTF_ifile:
	for label in uniTf_testY:
		uniTF_ifile.write(str(label) + "\n")
uniTF_ifile.close()

bi_ifile = open("bigram.output.txt", "a")
with bi_ifile:
	for label in bi_testY:
		bi_ifile.write(str(label) + "\n")
bi_ifile.close()

biTF_ifile = open("bigramtfidf.output.txt", "a")
with biTF_ifile:
	for label in biTf_testY:
		biTF_ifile.write(str(label) + "\n")
biTF_ifile.close()