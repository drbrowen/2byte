from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def blank():
    return render_template('index.html')

@app.route('/<ID>')
def readbits(ID):
    if(ID == '0'):
        sampledata = int('0x55',16)
        print("Data set to 0x55")
    else:
        sampledata = int('0xaa',16)
        print("Data set to 0xaa")
        
    bitdata = [sampledata & 0x80, sampledata & 0x40 , sampledata&0x20, sampledata&0x10, sampledata&0x08, sampledata&0x04, sampledata&0x02, sampledata&0x01]

    return render_template('index.html',bits=bitdata)

if __name__ == '__main__':
   app.run()


