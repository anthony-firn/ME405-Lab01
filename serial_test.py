import serial

ser = serial.Serial('COM3', 9600) # Establish the connection

print(ser.name)

while True :
    read = input("$")
    ser.write(read.encode() + b'\r\n')
    read = ser.readline()
    while read != '':
        print(read)
        read = ''
        read = ser.readline()
