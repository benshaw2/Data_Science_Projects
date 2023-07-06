def convertCSV(fileName):
    file=open(fileName,'r')
    lines=file.readlines()
    csvLines=[]

    for line in lines:
        line=line[1:-2]
        temp=line.split(' ')
        for value in temp:
            csvLine=value+','
        csvLine=csvLine[:-1]
        csvLines.append(csvLine)

    with open('csv.txt','w') as output:
        output.write("Daily Kos , The Guardian, Cnn, Fox NY post, The Blaze")
        for line in csvLines:
            print(line)
            output.write(line)
            print(':)')
def main():
    convertCSV('RepDemMatches.txt')