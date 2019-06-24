import time
import datetime
import os
import subprocess

import azure
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

block_blob_service = BlockBlobService(account_name='your_account_name' , account_key='your_key')

class camera:
    def __init__(self,n=None,m=None):
        self.n = n
        self.m = m
    
    def default(self):
        while True:
            f=datetime.datetime.now()
            os.system(('fswebcam -F 20 -S 3 --jpeg 50 --no-banner --save /home/pi/Downloads/redirect/{}').format(f.strftime("%H%M%S")))
            block_blob_service.create_blob_from_path('hydroponics','{}'.format(f.strftime("%H%M%S")),'/home/pi/Downloads/redirect/{}'.format(f.strftime("%H%M%S")),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            os.system(('fswebcam  -F 20 -S 3 --jpeg 50 --no-banner --rotate 90 --save /home/pi/to_transmit/%H%M%S.jpg'))
            block_blob_service.create_blob_from_path('hydroponics','{}'.format(f.strftime("%H%M%S")),'/home/pi/Downloads/redirect/{}'.format(f.strftime("%H%M%S")),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            os.system('fswebcam  -F 20 -S 3 --jpeg 50 --no-banner --invert --save /home/pi/to_transmit/%H%M%S.jpg')
            block_blob_service.create_blob_from_path('hydroponics','{}'.format(f.strftime("%H%M%S")),'/home/pi/Downloads/redirect/{}'.format(f.strftime("%H%M%S")),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            os.system('fswebcam  -F 20 -S 3 --jpeg 50 --no-banner --greyscale --save /home/pi/to_transmit/%H%M%S.jpg')
            block_blob_service.create_blob_from_path('hydroponics','{}'.format(f.strftime("%H%M%S")),'/home/pi/Downloads/redirect/{}'.format(f.strftime("%H%M%S")),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            os.system(('fswebcam  -F 20 -r 1900*1080 --no-banner -S 3 --jpeg 50  --save /home/pi/to_transmit/%H%M%S.jpg'))
            block_blob_service.create_blob_from_path('hydroponics','{}'.format(f.strftime("%H%M%S")),'/home/pi/Downloads/redirect/{}'.format(f.strftime("%H%M%S")),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)

cam=camera()
cam.default()
        

