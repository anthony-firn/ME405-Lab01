from matplotlib import pyplot

splittingList = []
graphingList = []
xValues = []
yValues = []

with open("eric.csv") as a_file:
    lines = a_file.readlines()
    for line in lines:
        removeSpaces = line.rstrip()
        splittingLines = removeSpaces.split(",")
        splittingList.append(splittingLines[:2])
    for values in splittingList:
        tempList = []  
        try:
            for value in values:
                tempList.append(float(value))
            graphingList.append(tempList)
        except ValueError:
            pass
    for xyvalues in graphingList:
        xValues.append(xyvalues[0])
        yValues.append(xyvalues[1])
        
    pyplot.plot (xValues, yValues, 'g--')
    pyplot.xlabel ("Time (fortnights)")
    pyplot.ylabel ("Height (furlongs)")
    pyplot.title ("Time Vs Height")   