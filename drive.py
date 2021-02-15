import sys
import os
import csv
import time

class Collector:

    def __init__(self, fileName='data/data.csv'): #pass in the file name
        file = open(fileName, 'a')
        self.writer = csv.writer(file)
        print('s')

    def write(self, direction):
        self.writer.writerow(direction)

class Controller:

    def set_motors(self, left_speed, left_dir, right_speed, right_dir):
        print('s')
        #self.left_pwm.ChangeDutyCycle(left_go * 100)
        #GPIO.output(self.LEFT_DIR_PIN, left_dir)
        #self.right_pwm.ChangeDutyCycle(right_go * 100)
        #GPIO.output(self.RIGHT_DIR_PIN, right_dir)

    def forward(self, seconds, speed):
        self.set_motors(speed, 0, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        self.set_motors(0, 0, 0, 0)

    def reverse(self, seconds, speed):
        self.set_motors(speed, 1, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def left(self, seconds, speed):
        self.set_motors(speed, 0, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds, speed):
        self.set_motors(speed, 1, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()