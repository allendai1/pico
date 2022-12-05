from machine import Pin
import utime as time
from lib.dht import DHT11


dhtPIN = 0
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))






while True:
    tempF = (dhtSensor.temperature * (9 / 5)) + 32 
    temp = dhtSensor.temperature
    # print("Temperature: " + str(temp))
    print("Humidity: " + str(dhtSensor.humidity))
    

    time.sleep(2)