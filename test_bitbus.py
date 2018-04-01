#!/usr/bin/env python3

from BitBus import BitBus
import time

a = BitBus()

val = a.do_read(0)
print("Value = " + str(val))

time.sleep(1)

val = a.do_read(1)
print("Value = " + str(val))

time.sleep(1)

a.do_write(0x50)
time.sleep(2)

a.cleanup()
