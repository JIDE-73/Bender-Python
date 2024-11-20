import serial
import time

# Configura el puerto serie y la velocidad (debe coincidir con el de tu Arduino)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 según tu sistema

def write_to_arduino(data):
    arduino.write(data.encode())
    print(f"Sent: {data}")

def read_from_arduino():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        print(f"Received: {data}")
        return data

try:
    while True:
        user_input = input("Enter command for Arduino: ")
        write_to_arduino(user_input)
        time.sleep(0.1)  # Esperar antes de leer
        read_from_arduino()
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    arduino.close()
