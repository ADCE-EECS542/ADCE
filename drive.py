import sys
import os
import csv
import time

# import RPI.GPIO as GPIO
# import GPIO as GPIO
motorFront1 = 50
motorFront2 = 50
data = []


class Collector:

    def write(self):  # write stored data into file for return purpose
        with open("data/data.txt", "w") as txt_file:
            for line in data:
                txt_file.write(" ".join(line))


class Controller:

    def setMotors(self, motor1, motor2, seconds):  # motors variable, and time hold

        while seconds:
            time.sleep(1)
            print(seconds)
            seconds -= 1
            # GPIO.output(self.MotorFront1, motor1)
            # GPIO.output(self.MotorFront2, motor2)
        # GPIO.output(self.MotorFront1, 0)
        # GPIO.output(self.MotorFront2, 0)


def main():
    Ctr = Controller()
    Clt = Collector()
    f = open("data/route.txt", "r")
    for i in f:  # slicing string
        if i[0] == 'w':
            Ctr.setMotors(motorFront1, motorFront2, int(i[2:]))
            print(i[2:])
        data.append(i)
    print(data[2:])
    Clt.write()


main()

#
