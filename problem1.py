import csv


def calc_label(feature_1, feature_2):
	funcLabel = weights[2] + (feature_1 * weights[0]) + (feature_2 * weights[1])

	if funcLabel > 0:
		return 1
	return -1

weights = [0, 0, 0]

data = []

ifile = open("input1.csv", "rb")
with ifile:
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)

dataLength = len(data)

for row in range(0, dataLength):
	for x in range(0, 3):
		data[row][x] = int(data[row][x])

ofile = open("output1.csv", "w")
with ofile:
	writer = csv.writer(ofile)

	noConvergence = True
	while noConvergence:
		noConvergence = False

		for row in range(0, dataLength):
			label = calc_label(data[row][0], data[row][1])

			if data[row][2] * label <= 0:
				noConvergence = True

				weights[2] += data[row][2]
				weights[0] += data[row][2] * data[row][0]
				weights[1] += data[row][2] * data[row][1]

		if noConvergence:
			writer.writerow(weights)

ifile.close()
ofile.close()
