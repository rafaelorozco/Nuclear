file = open("nucdata.txt","r")
filewrite = open("cleandata.json","w")

mainStr = file.read()

mainList = mainStr.split()

result = []
maxmag = 0
minmag = 100000

for i in range(0,len(mainList)):
	element = mainList[i]

	if("." in element):
		if(element[-1] == "N" or element[-1] == "S"):
			lat = element
			lon = mainList[i+1]
			mag = mainList[i-1]

			if("-" in mag):
				t = mag.split("-")
				low = float(t[0])
				high = float(t[1])
				mag = low + ((high-low)/2)
			else:
				try: 
					mag = float(mag)
				except:
					continue
					

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


			result.append(lat)
			result.append(lon)
			result.append(mag)

#print maxmag
#print minmag
maxmag = 2000

tj = []
for i in range(2,len(result),3):
	result[i] = max(0.05,(result[i] - minmag) / (maxmag - minmag))

	#tj.append(result[i])
	#pass


#print max(tj)
#print min(tj)

#print g
#print result
print len(result)/3

print result[0:10]

bigString = "["
bigString += " [\"Day\", "
bigString += str(result)
bigString += "]]"

filewrite.write(bigString)


filewrite.close()
file.close()