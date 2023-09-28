import os
import time
import random
import serial

ser = serial.Serial("COM45", 9600, timeout=0.050)


def ser_com_gen():
    while True:
        integer = random.randint(10, 50)
        int_f = str(integer)
        string = f"{int_f}\n"
        print(f"Sending: {int_f}")
        ser.write(str.encode(string, encoding='utf-8'))
        time.sleep(0.03)


try:
    if __name__ == "__main__":
        ser_com_gen()
except KeyboardInterrupt:
    os.system('cls')
    print("Stopped generating serial traffic")
    exit(0)
