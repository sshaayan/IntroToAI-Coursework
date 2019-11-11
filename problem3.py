import csv
from sklearn import svm
from sklearn import linear_model
from sklearn import neighbors
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


#outputs the scores for an SVM with linear kernel
def SVM_Linear(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = svm.SVC(kernel = "linear", C = 5)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["svm_linear", bestTrainScore, testScore]
	return outputRow


#outputs the scores for an SVM with polynomial kernel
def SVM_Polynomial(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = svm.SVC(kernel = "poly", C = 1, degree = 6, gamma = 0.5)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["svm_polynomial", bestTrainScore, testScore]
	return outputRow


#outputs the scores for an SVM with RBF kernel
def SVM_RBF(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = svm.SVC(kernel = "rbf", C = 100, gamma = 1)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["svm_rbf", bestTrainScore, testScore]
	return outputRow


#outputs the scores for logistic regression
def log_regression(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = linear_model.LogisticRegression(C = 100)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["logistic", bestTrainScore, testScore]
	return outputRow


#outputs the scores for k-nearest neighbors
def kNearest(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = neighbors.KNeighborsClassifier(n_neighbors = 1, leaf_size = 5)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["knn", bestTrainScore, testScore]
	return outputRow


#outputs the scores for Decision Trees
def decision_tree(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = tree.DecisionTreeClassifier(max_depth = 5, min_samples_split = 2)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["decision_tree", bestTrainScore, testScore]
	return outputRow


#outputs the scores for a Random Forest
def random_forest(X_train, X_test, y_train, y_test):
	X_train_folds = [[], [], [], [], []]
	y_train_folds = [[], [], [], [], []]

	for row in range(0, 400):
		if row < 80:
			X_train_folds[0].append(X_train[row])
			y_train_folds[0].append(y_train[row])
		elif row < 160:
			X_train_folds[1].append(X_train[row])
			y_train_folds[1].append(y_train[row])
		elif row < 240:
			X_train_folds[2].append(X_train[row])
			y_train_folds[2].append(y_train[row])
		elif row < 320:
			X_train_folds[3].append(X_train[row])
			y_train_folds[3].append(y_train[row])
		else:
			X_train_folds[4].append(X_train[row])
			y_train_folds[4].append(y_train[row])

	clf = RandomForestClassifier(max_depth = 20, min_samples_split = 2)

	for k in range(0, 5):
		clf.fit(X_train_folds[k], y_train_folds[k])

	bestTrainScore = clf.score(X_train_folds[4], y_train_folds[4])
	testScore = clf.score(X_test, y_test)

	outputRow = ["random_forest", bestTrainScore, testScore]
	return outputRow


#imports the data and splits it into training, validation, and test sets
data = []
ifile = open("input3.csv", "rU")
with ifile:
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)

featureA_array = []
featureB_array = []
label_array = []

for row in range(1, len(data)):
	featureA_array.append(float(data[row][0]))
	featureB_array.append(float(data[row][1]))
	label_array.append(float(data[row][2]))

dataLength = 500

X = []
for row in range(0, dataLength):
	newPoint = [featureA_array[row], featureB_array[row]]
	X.append(newPoint)

X_train, X_test, y_train, y_test = train_test_split(X, label_array, test_size = 0.2)


#trains and tests the data and outputs the score
output = []
output.append(SVM_Linear(X_train, X_test, y_train, y_test))
output.append(SVM_Polynomial(X_train, X_test, y_train, y_test))
output.append(SVM_RBF(X_train, X_test, y_train, y_test))
output.append(log_regression(X_train, X_test, y_train, y_test))
output.append(kNearest(X_train, X_test, y_train, y_test))
output.append(decision_tree(X_train, X_test, y_train, y_test))
output.append(random_forest(X_train, X_test, y_train, y_test))

ofile = open("output3.csv", "w")
with ofile:
	writer = csv.writer(ofile)

	for row in output:
		writer.writerow(row)
