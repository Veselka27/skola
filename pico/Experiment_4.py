from machine import Pin, PWM
from time import sleep

ButtonA = Pin(0, Pin.IN, Pin.PULL_DOWN)
ButtonB = Pin(1, Pin.IN, Pin.PULL_DOWN)

Buzzer = PWM(Pin(15))
Buzzer.duty_u16(32767)
Frequency = 200

def ButtonIRQHandler(pin):
    global Frequency
    if pin == ButtonA:
        if Frequency < 2000:
            sleep(0.2)
            Frequency += 50
    elif pin == ButtonB:
        if Frequency > 100:
            sleep(0.2)
            Frequency -= 50
    print(Frequency)

ButtonA.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)
ButtonB.irq(trigger = Pin.IRQ_RISING, handler = ButtonIRQHandler)

while True:
    Buzzer.freq(Frequency)

# Pin 0 > ButtonA > Pin 36
# Pin 1 > ButtonB > Pin 36
# Pin 15 > Buzzer > Pin 38