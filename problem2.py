import csv
import numpy


#adjusts the weights using gradient descent
def gradientDescent(alpha, firstArray, secondArray, labelArray, weightArray):
	zeroethDescent = 0
	firstDescent = 0
	secondDescent = 0

	for i in range(0, dataLength):
		zeroethDescent += weightArray[0] + (weightArray[1] * firstArray[i]) + (weightArray[2] * secondArray[i]) - labelArray[i]
		firstDescent += (weightArray[0] + (weightArray[1] * firstArray[i]) + (weightArray[2] * secondArray[i]) - labelArray[i]) * firstArray[i]
		secondDescent += (weightArray[0] + (weightArray[1] * firstArray[i]) + (weightArray[2] * secondArray[i]) - labelArray[i]) * secondArray[i]

	zeroethDescent = (zeroethDescent * alpha) / dataLength
	firstDescent = (firstDescent * alpha) / dataLength
	secondDescent = (secondDescent * alpha) / dataLength

	weightArray[0] -= zeroethDescent
	weightArray[1] -= firstDescent
	weightArray[2] -= secondDescent

	return weightArray


#read the data from the input and place it into a 2D Array
data = []

ifile = open("input2.csv", "rb")
with ifile:   
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)


#get the amount of data, or rows
dataLength = len(data)


#convert each string value into a float value
for row in range(0, dataLength):
	for x in range(0, 3):
		data[row][x] = float(data[row][x])


#find the mean and standard deviation for both features
firstArray = []
secondArray = []
for row in range(0, dataLength):
	firstArray.append(data[row][0])
	secondArray.append(data[row][1])

firstNumArray = numpy.array(firstArray)
secondNumArray = numpy.array(secondArray)

firstMean = numpy.mean(firstNumArray)
secondMean = numpy.mean(secondNumArray)
firstStd = numpy.std(firstNumArray)
secondStd = numpy.std(secondNumArray)


#scale each value for each feature and set each mean to 0
for row in range(0, dataLength):
	firstArray[row] = (firstArray[row] - firstMean) / firstStd
	secondArray[row] = (secondArray[row] - secondMean) / secondStd


#sets up all the array with y values
labelArray = []
for row in range(0, dataLength):
	labelArray.append(data[row][2])


#run the algorithm to find the best weights and write them to the output file
ofile = open("output2.csv", "w")
with ofile:
	alphaValues = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
	writer = csv.writer(ofile)
	for alpha in alphaValues:
		weightArray = [0, 0, 0]
		for x in range(0, 100):
			weightArray = gradientDescent(alpha, firstArray, secondArray, labelArray, weightArray)

		outputArray = [alpha, 100, weightArray[0], weightArray[1], weightArray[2]]
		writer.writerow(outputArray)

	newAlpha = 0.07
	weightArray = [0, 0, 0]
	for x in range(0, 100):
		weightArray = gradientDescent(newAlpha, firstArray, secondArray, labelArray, weightArray)

	outputArray = [newAlpha, 100, weightArray[0], weightArray[1], weightArray[2]]
	writer.writerow(outputArray)
