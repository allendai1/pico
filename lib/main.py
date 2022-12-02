from machine import Pin
import utime as time
from lib.dht import DHT11

dhtPIN = 0
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))

while True:
    print("Temperature: " + str(dhtSensor.temperature))
    print("Humidity: " + str(dhtSensor.humidity))

    time.sleep(1.5)