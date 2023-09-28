import os
import serial
import random
from serial import SerialException


def filter(input):
    num = []
    ch = ""
    if input == 0:
        pass
    else:
        for digit in input:
            if digit.isdigit():
                num.append(digit)
            else:
                pass
        ch = ch.join(num)
    return ch


def processing_data():
    print("")
    int_x = 0
    int_x_in = 180
    while int_x <= 180:
        p_data = ser.readline().decode(encoding='utf-8')
        if p_data.__contains__(" "):
            rand_int = random.randint(560, 500)
            pro_out = f"{int_x},{rand_int}."
            print(f"sending to processing random data: {pro_out}")
            proc_ser.write(str.encode(pro_out))
            int_x += 1
        elif p_data.__len__() > 0:
            p_filtered = filter(p_data)
            p_out = f"{int_x},{p_filtered}."
            print(f"sending to processing: {p_out}")
            proc_ser.write(str.encode(p_out))
            int_x += 1
        else:
            pass

    while int_x_in > 0:
        p_data = ser.readline().decode(encoding='utf-8')
        if p_data.__contains__(" "):
            rand_out = random.randint(456, 500)
            pro_out = f"{int_x_in},{rand_out}."
            print(f"Sending to processing random data: {pro_out}")
            proc_ser.write(str.encode(pro_out))
            int_x_in -= 1
        elif p_data.__len__() > 0:
            p_filtered = filter(p_data)
            p_out = f"{int_x_in},{p_filtered}."
            print(f"sending: {p_out}")
            proc_ser.write(str.encode(p_out))
            int_x_in -= 1
        else:
            pass


def try_read():
    try:
        print("Waiting for valid data")
        while True:
            data = ser.readline().decode(encoding='utf-8')
            if data.__contains__(" "):
                rand_int = random.randint(45, 50)
                print(f"Random: {rand_int}")
            elif data.__len__() > 0:
                filtered = filter(data)
                print(f"FILTERED: {filtered}")
            else:
                pass
    except SerialException:
        exit(0)


try:
    port = int(input("Enter COM Port: "))
    serial_port = f"COM{port}"
    ser = serial.Serial(serial_port, 9600, timeout=0.050)
except SerialException:
    os.system('cls')
    print(f"{serial_port} Port Not Found")
    exit(0)
try:
    port_p = int(input("Enter processing com port: "))
    serial_port_p = f"COM{port_p}"
    proc_ser = serial.Serial(serial_port_p, 9600, timeout=0.050)
except SerialException:
    os.system('cls')
    print("processing port not found")
    exit(0)

try:
    if __name__ == "__main__":
        print("Serial Communication Started")
        while True:
            processing_data()
except KeyboardInterrupt:
    os.system('cls')
    print("Serial communication Stopped")
    exit(0)
