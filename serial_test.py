import serial

from matplotlib import pyplot

ser = serial.Serial('COM3', 9600) # Establish the connection

print(ser.name)

splittingList = []
graphingList = []
xValues = []
yValues = []

while True :
    line = input("$")
    ser.write(line.encode() + b'\r\n')
    line = ser.readline()

    while line != b'end\r\n':
        #print(line)
        line = ''
        line = ser.readline()

        #parse
        try :
            removeSpaces = str(line.rstrip())
            #print("removed spaces: " + str(removeSpaces))
            splittingLines = removeSpaces.split(",")
            splittingLines[0] = splittingLines[0][2:]
            splittingLines[1] = splittingLines[1][1:-1]
            #print("splitting lines: " + str(splittingLines))
            splittingList.append(splittingLines[:2])
        except :
            print("splitting lines sucks")
            pass

    print("graphing" + str(splittingList))
    for values in splittingList:
        tempList = []  
        try:
            for value in values:
                tempList.append(float(value))
            graphingList.append(tempList)
        except ValueError:
            print("except")
            pass

    print("graphing list " + str(graphingList))
    for xyvalues in graphingList:
        xValues.append(xyvalues[0])
        yValues.append(xyvalues[1])
        
    pyplot.plot (xValues, yValues, 'g--')
    pyplot.xlabel ("Time (seconds)")
    pyplot.ylabel ("Tick Angle ()")
    pyplot.title ("Time Vs Ticks")   
