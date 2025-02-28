from machine import Pin, ADC, PWM
from time import sleep

buzzer = PWM(Pin(15))
buzzer.freq(500)

pot = ADC(Pin(4))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  pot_value = round(pot.read()*3.3/4095,3)
  print(pot_value)
  sleep(0.1)
  
  if pot_value>=1.5:
      buzzer.duty_u16(5000)
  else:
      buzzer.duty_u16(0)

      