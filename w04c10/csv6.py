import csv
with open('sample2.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)

print(sampleData)
sampleData[0][0] = "Robert"
csvFile = open('sample2.csv', 'w')
sampleWriter = csv.writer(csvFile)
sampleWriter.writerows(sampleData)
