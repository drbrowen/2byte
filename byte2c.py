import smbus
import time

bus = smbus.SMBus(1)

class byte2c:
    def __init__(self):
        self.addr      = 0x24
        self.regwrite  = 0x14
        self.iodir     = 0x00

        self.clock = 0
        self.outbit = 0
        self.outbyte = 0
        self.onbit = 0

        self.bus = smbus.SMBus(1)

        #self.bus.write_byte_data(self.addr,0x05,0x00)
        #self.bus.write_byte_data(self.addr,0x0a,0x10)
        self.bus.write_byte_data(self.addr,self.iodir,0x00)
        self.bus.write_byte_data(self.addr,self.iodir+1,0x00)
        self.bus.write_byte_data(self.addr,self.regwrite,0x00)
        self.bus.write_byte_data(self.addr,self.regwrite+1,0x00)
        
    def set_out_bit(self):
        if(self.onbit>=0):
            self.bus.write_byte_data(self.addr,self.regwrite,1<<self.onbit)
        else:
            self.bus.write_byte_data(self.addr,self.regwrite,0)

    def clock_up(self):
        if(self.clock == 1):
            return

        self.clock = 1
        self.onbit -= 1
        self.write_control()

    def clock_down(self):
        if(self.clock == 0):
            return
        
        self.clock = 0
        self.write_control()
        if(self.onbit == 0):
            self.onbit = -1
            self.set_out_bit()


    def set_write_byte(self,byte):
        self.outbyte = byte
        self.onbit = 8

    
    def write_control(self):
        if(self.onbit>=0):
            self.outbit = (self.outbyte >> self.onbit) & 1
        else:
            self.outbit = 1

        self.bus.write_byte_data(self.addr,self.regwrite+1,self.outbit*128 + self.clock*64)
        self.set_out_bit()
        
            
    def reset(self):
        self.bus.write_byte_data(self.addr,self.regwrite,0x00)
        self.bus.write_byte_data(self.addr,self.regwrite+1,0x00)
        self.outbit = -1
