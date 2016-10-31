file = open("nucdata.txt","r")
filewrite = open("cleandata.json","w")

mainList = file.readlines()

result1 = []
result2 = []
result3 = []
result4 = []

maxmag = 0
minmag = 100000

listSort = []
index = 1

for i in range(0,len(mainList)):

	line = mainList[i].split()
	for j in range(0,len(line)):
		element = line[j]
		year = line[0]

		if("." in element):
			if(element[-1] == "N" or element[-1] == "S"):
				lat = element
				lon = line[j+1]
				mag = line[j-1]

				if("-" in mag):
					t = mag.split("-")
					low = float(t[0])
					high = float(t[1])
					mag = low + ((high-low)/2)
				else:
					try: 
						mag = float(mag)
					except:
						mag = 50.0
						
				##Convert Coordinates to decimal
				if(lat[-1] == "N"):
					try:
						lat = float(lat[0:-1])
					except:
						continue
				else: 
					try:
						lat = -float(lat[0:-1])
					except:
						continue
				if(lon[-1] == "E"):
					try:
						lon = float(lon[0:-1])
					except:
						continue
				else:
					try:
						lon = -float(lon[0:-1])
					except:
						continue

				if(mag > maxmag):
					maxmag = mag
				if(mag < minmag):
					minmag = mag

				listT = []
				listX = []
					
				listT.append(lat)
				listT.append(lon)
				listT.append(mag)
				listT.append(index)

				listX.append(lat)
				listX.append(lon)
				listX.append(0)
				listX.append(0)

				listSort.append(listT)

				if(int(year[0:2]) < 65):
					result1.append(listT)
					result2.append(listX)
					result3.append(listX)
					result4.append(listX)


				elif(int(year[0:2]) < 75):
					result1.append(listX)
					result2.append(listT)
					result3.append(listX)
					result4.append(listX)

				elif(int(year[0:2]) < 85):		
					result1.append(listX)
					result2.append(listX)
					result3.append(listT)
					result4.append(listX)

				else:
					result1.append(listX)
					result2.append(listX)
					result3.append(listX)
					result4.append(listT)
	
				index+=1



listSort.sort(key=lambda x: x[2])

for i in range(len(listSort)):
	id = listSort[i][3]
	listSort[i][2] = i*  (1.0/ len(listSort))


	for j in range(len(result1)):
		if(result1[j][3] == id):
			result1[j][2] = listSort[i][2]
	for j in range(len(result2)):
		if(result2[j][3] == id):
			result2[j][2] = listSort[i][2]
	for j in range(len(result3)):
		if(result3[j][3] == id):
			result3[j][2] = listSort[i][2]
	for j in range(len(result4)):
		if(result4[j][3] == id):
			result4[j][2] = listSort[i][2]
		

resultA = []
resultB = []
resultC = []
resultD = []

for i in range(len(result1)):
	resultA.extend(result1[i][0:3])
	resultB.extend(result2[i][0:3])
	resultC.extend(result3[i][0:3])
	resultD.extend(result4[i][0:3])


bigString = "["
bigString += " [\"1\", "
bigString += str(resultA[0:])#list(resultN[0]))#resultN[0][0:3*len(resultN[0])//3])
bigString += "], [\"2\", "
bigString += str(resultB[0:])#str(list(resultN[1]))#str(resultN[1][0:3*len(resultN[1])//3])
bigString += "], [\"3\", "
bigString += str(resultC[0:])#str(list(resultN[2]))#str(resultN[2][0:3*len(resultN[2])//3])
bigString += "], [\"4\", "
bigString += str(resultD[0:])#str(list(resultN[2]))#str(resultN[2][0:3*len(resultN[2])//3])
bigString += "]]"

filewrite.write(bigString)


filewrite.close()
file.close()