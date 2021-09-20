from pyfirmata import Arduino, util

board = Arduino("COM3") #specify COM3 port as serial port

portreada = board.get_pin('a:0:i') #select analog zero pin

it = util.Iterator(board)
it.start()  

def getSensorValue():
    value = portreada.read() #read a sensor value
    return value #return a sensor value
    

