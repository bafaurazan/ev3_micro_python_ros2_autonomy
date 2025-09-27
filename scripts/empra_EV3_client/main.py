#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import socket
import time

ev3 = EV3Brick()
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)

SERVER_IP = "192.168.10.2"  # IP laptopa
SERVER_PORT = 8081

def http_get(path="/"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((SERVER_IP, SERVER_PORT))
        request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(path, SERVER_IP)
        s.send(request.encode())
        response = s.recv(1024).decode()
        return response
    except Exception as e:
        print("Błąd połączenia:", e)
        return None
    finally:
        s.close()

while True:
    response = http_get("/command")

    if response:  # sprawdzamy czy coś przyszło
        try:
            # bierzemy ostatnią linię odpowiedzi
            command = float(response.strip().splitlines()[-1])
            command = command * 100
            
            # ustawiamy moc na oba silniki
            motor_a.dc(command)
            motor_b.dc(command)
        except Exception as e:
            print("Błąd parsowania odpowiedzi:", e)

    time.sleep(0.05)  # trochę większy odstęp (20 Hz zamiast 1000 Hz)