from machine import Pin
import time

pul1 = Pin (28, Pin.IN)
pul2 = Pin (27, Pin.IN)
azul = Pin (1, Pin.OUT) 
amarillo = Pin (2, Pin.OUT)

while 1:
  if pul1.value() == 1:
    azul.value(1)
  else: 
    azul.value(0)

  if pul2.value() == 1 and amarillo.value() == 0:
    amarillo.value(1)
    time.sleep_ms(500)
    
  elif pul2.value() == 1 and amarillo.value() == 1:
    amarillo.value(0)
    time.sleep_ms(500)  