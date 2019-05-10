def ExtractDataOfInterest(s):
	L = []
	with open(s, 'r') as f:
		for line in f:
			if not line.startswith("Date"):
				line = line.replace("\n", "")
				A = line.split(",")
				date = A[0]
				high = float(A[2])
				L.append([date, high])
		return L 

def StockPriceChange(new, old):
	return 100.0*(new-old)/old

def PreparedData(Data):
	L = []
	for i in range(len(Data)-1):
		current_date = Data[i+1][0]
		old_high = Data[i][1]
		new_high = Data[i+1][1]
		change = StockPriceChange(new_high, old_high)
		L.append([current_date, new_high, change])
	return L

def WritePreparedDataToFile(s, PreparedData):
	with open(s, 'w') as f:
		for i in range(len(PreparedData)):
			data = PreparedData[i][0]
			high = PreparedData[i][1]
			change = PreparedData[i][2]
			f.write("%s, %f, %f \n" % (date, high, change))


def main():
	Data = ExtractDataOfInterest("NDAQ-Daily-3months.csv")
	PreparedData = PreparedData(Data)
	WritePreparedDataToFile("processed_data.csv", PreparedData)
main()