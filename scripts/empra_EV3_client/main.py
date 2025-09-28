#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import socket
import time
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('cmd', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

ev3 = EV3Brick()
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_d = Motor(Port.D)

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hi')

while True:
    try:
        msg = mbox.read()
        # bierzemy ostatnią linię odpowiedzi
        # command = float(response.strip().splitlines()[-1])
        # command = command * 100
        parts = msg.split()
        linear_x = float(parts[0])
        angular_z = float(parts[1])
        print(linear_x)
        print(angular_z)
        # ustawiamy moc na oba silniki
        left = (linear_x - angular_z)/2 * 100
        right = (linear_x + angular_z)/2 * 100

        motor_a.dc(-left)
        motor_b.dc(left)
        motor_c.dc(-right)
        motor_d.dc(right)
        
    except Exception as e:
        print("Błąd parsowania odpowiedzi:", e)

    time.sleep(0.05)  # trochę większy odstęp (20 Hz zamiast 1000 Hz)