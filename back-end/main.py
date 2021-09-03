import serial
from time import sleep
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get('KEYTHINGS')
write_url = f"https://api.thingspeak.com/update?api_key={key}"
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.5)

arduino.write(bytes('S','ascii'))
sleep(3)

def write_read(option):
  arduino.write(bytes(option,'ascii'))
  sleep(1)
  data = arduino.readline()
  sleep(5)
  return data.decode("utf-8")

while True:
  try:
    temp = write_read('C')
    lux = write_read('L')
    params = {"field1":temp,"field2":lux}
    print(temp)
    print(lux)  
    r = requests.get(url = write_url, params = params)
  except:
    print("wrong Value")