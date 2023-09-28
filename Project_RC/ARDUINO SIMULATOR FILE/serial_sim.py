# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:03:41 2023

@author: Naveen William
"""
import os
import time
import random
import serial
from serial import SerialException

try:
    port = int(input("Enter COM Port: "))
    serial_port = f"COM{port}"
    ser = serial.Serial(serial_port, 9600, timeout=0.050)
except SerialException:
    os.system('cls')
    print(f"{serial_port} Port Not Found")
    exit(0)


def intro():
    for i in range(5):
        print(f"Serial comm starting in {i}s")
        time.sleep(1)
        os.system('cls')


def Dist():
    avg = random.randint(24, 40)
    for _ in range(1):
        dist = random.randint(10, avg)
        dist = str(dist)
    return dist


def loop():
    i = 0
    i_in = 180

    while i <= 180:
        n = str(i)
        time.sleep(0.03)
        distance = Dist()
        console_out = f"{n},{distance}."
        print(f"Sending: {console_out}")
        ser.write(n.encode())
        ser.write(",".encode())
        ser.write(distance.encode())
        ser.write(".".encode())
        i += 1

    while i_in > 0:
        n_in = str(i_in)
        time.sleep(0.03)
        distance = Dist()
        console_out = f"{n_in}.{distance}."
        print(f"Sending: {console_out}")
        ser.write(n_in.encode())
        ser.write(",".encode())
        ser.write(distance.encode())
        ser.write(".".encode())
        i_in -= 1


try:
    if __name__ == "__main__":
        intro()
        print("\nSerial Communication Started on COMM45")
        while True:
            loop()
except KeyboardInterrupt:
    os.system('cls')
    print("Serial communication Stopped")
    exit(0)
