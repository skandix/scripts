# reads out temp from serial
import serial

buffer = []

def getTemp():
    ser = serial.Serial('COM4', 9600, timeout=0)
    while 1:
        if ser.inWaiting() == long(5) or ser.inWaiting() == long(6) or ser.inWaiting() == long(4):
            #print "\nbytes", ser.inWaiting()
            val = ser.readline(ser.inWaiting())
            buffer.append(str(val))
        return buffer[-1]

for j in range(50):
    print getTemp()
