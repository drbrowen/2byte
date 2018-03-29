# Define the bus parameters here.

import RPi.GPIO as GPIO
import time

class BitBus:
    def __init__(self):
        # data bits are LSB (Least Significant Bit, or bit 0) first
        # addr are LSB
        self.databits = [4,17,18,27,22,23,24,25]
        self.addrbits = [10,9]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.set_read_mode()
    
    def set_addr(self,a):
        if(a == 0):
            GPIO.output(self.addrbits[1],0)
            GPIO.output(self.addrbits[0],1)
        elif(a == 1):
            GPIO.output(self.addrbits[0],0)
            GPIO.output(self.addrbits[1],1)
        else:
            print("Address must be 0 or 1")

    def clear_addr(self):
        GPIO.output(self.addrbits,0)
            
    def read_all_bits(self):
        retval = 0
        i=0
        for bits in self.databits:
            retval += GPIO.input(bits)<<i
            i += 1

        return retval

    def set_write_mode(self):
        for addr in self.addrbits:
            GPIO.setup(addr,GPIO.IN)
        for bits in self.databits:
            GPIO.setup(bits,GPIO.OUT)

    def set_read_mode(self):
        for bits in self.databits:
            GPIO.setup(bits,GPIO.IN)
        for addr in self.addrbits:
            GPIO.setup(addr,GPIO.OUT)
            GPIO.output(addr,0)
        
            
    def do_read(self,addr):
        if(addr != 0 and addr != 1):
            raise ValueError('Allowed addresses are 0 and 1')
        self.set_read_mode()
        time.sleep(.001)
        self.set_addr(addr)
        time.sleep(.001)
        retval = self.read_all_bits()
        time.sleep(.001)
        self.clear_addr()
        return retval

    def cleanup(self):
        GPIO.cleanup()


