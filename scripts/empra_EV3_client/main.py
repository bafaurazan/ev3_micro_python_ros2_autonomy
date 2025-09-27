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
    # Tworzymy socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((SERVER_IP, SERVER_PORT))
        request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(path, SERVER_IP)
        s.send(request.encode())
        response = s.recv(1024).decode()
        return response
    except Exception as e:
        print("Błąd połączenia:", e)
        return ""
    finally:
        s.close()

while True:
    # Pobieramy komendę z serwera
    response = http_get("/command")
    # weź ostatnią linię i usuń spacje
    command = float(response.strip().splitlines()[-1])

    motor_a.dc(command)  # obraca o 90 stopni od bieżącej pozycji
    motor_b.dc(command)



    time.sleep(0.001)  # czekamy 1 sekundę przed kolejnym GET
