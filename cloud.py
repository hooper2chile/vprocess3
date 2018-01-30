'''
    Google Drive cloud for Bioreactor.
    Macos and rasbian version.
    Application for synchronization.
'''

import os, sys, time, datetime, logging

logging.basicConfig(filename='/home/pi/vprocess3/log/cloud.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



TIME_SYNC = 180 #3600 #sync for 3600 [s] = 1 [hr]; 180 = 3 min
ID = '1sbAk593Hmgv75sXuyRFn_ObDC8j783Q7'


time.sleep(15)
gdrive = '/home/pi/vprocess3/config/./gdrive-linux-rpi'
DIR1   = ' ' #'/home/pi/vprocess2/config/'
DIR2   = '/home/pi/vprocess2/csv/'


while True:
    hora = time.strftime("Hora=%H:%M:%S__Fecha=%d-%m-%y")
    try:
        os.system(DIR1 + gdrive + ' sync upload ' + DIR2 + '.' + ' ' + ID)
        logging.info('sincronizado: ' + hora)
        f = open(DIR2+'gdrive_sync.txt','a+')
        f.write('sincronizado: ' + hora + ' \n')
        f.close()
        time.sleep(TIME_SYNC)

    except:
        logging.info('Fallo al subir a cloud:' + hora)
	time.sleep(TIME_SYNC)
