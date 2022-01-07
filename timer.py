from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
n = 1


while n<=1800: 
    led.toggle()
    print("n= " , n) 
#     print("-------")
    n = n+1
    sleep(1)
    led.toggle()
    
