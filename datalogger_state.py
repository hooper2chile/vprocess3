
import os, time



DIR = "/home/pi/vprocess2/"

while True:
    f = open(DIR + "datalogger_state.txt", 'a')
    now = time.strftime("%H:%M:%S")
    dia = time.strftime("%d/%m/%y")
    f.write("Estoy encendido a las: " + now + ", del dia: "+ dia  + '\n')
    f.close()
    time.sleep(60)
