#!/usr/bin/env python3

from byte2c import byte2c
import time

i2c = byte2c()
time.sleep(1)

i2c.set_write_byte(0x5a)

for i in range(8):
    i2c.clock_up()
    time.sleep(.5)
    i2c.clock_down()
    time.sleep(.5)
