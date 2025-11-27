# boot.py -- minimal boot for POC
import pyb, os, micropython, time

# power hold
pwr = pyb.Pin("B15", pyb.Pin.OUT)
pwr.on()

leds = [pyb.LED(i) for i in range(1,5)]

def pwrcb(e):
    micropython.schedule(poweroff, 0)

def poweroff(_):
    for led in leds:
        led.toggle()
    os.sync()
    time.sleep_ms(300)
    pwr.off()
    time.sleep_ms(300)
    for led in leds:
        led.toggle()

pyb.ExtInt(pyb.Pin('B1'), pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_NONE, pwrcb)

pyb.main("addresses.py")
