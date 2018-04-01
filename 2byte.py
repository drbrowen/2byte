#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from BitBus import BitBus
from byte2c import byte2c

app = Flask(__name__)

sampledata = 0

bb = BitBus()
i2c = byte2c()

@app.route('/')
def base_output():
    global sampledata
    bitdata = [sampledata & 0x80, sampledata & 0x40 , sampledata&0x20, sampledata&0x10, sampledata&0x08, sampledata&0x04, sampledata&0x02, sampledata&0x01]
    return render_template('index.html',bits=bitdata)

def serial_output():
    global sampledata
    bitdata = [sampledata & 0x80, sampledata & 0x40 , sampledata&0x20, sampledata&0x10, sampledata&0x08, sampledata&0x04, sampledata&0x02, sampledata&0x01]
    return render_template('index2.html',bits=bitdata)

@app.route('/<ID>')
def readbits(ID):
    global sampledata
    i2c.reset()
    sampledata = bb.do_read(int(ID))

    return base_output()

@app.route('/setinput/<ID>')
def setinput(ID):
    bb.set_addr(int(ID))
    return base_output()


@app.route('/readstate')
def readinput():
    global sampledata
    sampledata = bb.read_all_bits()
    return base_output()

@app.route('/freebus')
def freebus():
    bb.clear_addr()
    return base_output()

@app.route('/start_serial')
def startserial():
    global sampledata
    bb.do_write(sampledata)
    i2c.set_write_byte(sampledata)
    return serial_output()

@app.route('/clockup')
def clock_up():
    i2c.clock_up()
    return serial_output()

@app.route('/clockdown')
def clock_down():
    i2c.clock_down()
    return serial_output()
    
if __name__ == '__main__':
   app.run(host='0.0.0.0')



