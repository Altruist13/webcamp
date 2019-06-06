import time
from datetime import datetime
import subprocess
import os

class camera:
    def rotate (self,n):
        while True:
        	os.system('fswebcam   --jpeg 50 --rotate self.n --save /home/pi/to_transmit/%H%M%S.jpg')
                time.sleep(60)
    def invert(self):
	while True:
        	os.system('fswebcam  -S 3 --jpeg 50 --invert --save /home/pi/to_transmit/%H%M%S.jpg')
		time.sleep(60)
    def greyscale(self):
	while True:
        	os.system('fswebcam  -S 3 --jpeg 50 --greyscale --save /home/pi/to_transmit/%H%M%S.jpg')
		time.sleep(60)
    def resolution(self,m ,n):
	while True:
        	os.system('fswebcam  -r self.m*self.n -S 3 --jpeg 50  --save /home/pi/to_transmit/%H%M%S.jpg')
		time.sleep(60)
    def default(self):
	while True:
        	os.system('fswebcam   --jpeg 50 --rotate self.n --save /home/pi/to_transmit/%H%M%S.jpg')
        	time.sleep(60)
        	os.system('fswebcam  -S 3 --jpeg 50 --invert --save /home/pi/to_transmit/%H%M%S.jpg')
 		time.sleep(60)
        	os.system('fswebcam  -S 3 --jpeg 50 --greyscale --save /home/pi/to_transmit/%H%M%S.jpg')
		time.sleep(60)
        	os.system('fswebcam  -r self.m*self.n -S 3 --jpeg 50  --save /home/pi/to_transmit/%H%M%S.jpg')
		time.sleep(60)

print("HEY ! ENTER THE TYPE OF PHOTOS YOU WANT")
c=input().split()
if(c[0]=="invert"):
    cam=camera()
    cam.invert()
        
elif(c[0]=="rotate"):
    cam=camera()
    cam.rotate(c[1])

elif(c[0]=="resolution"):
    cam=camera()
    cam.resolution(c[1],c[2])
        
elif(c[0]=="greyscale"):
    cam=camera()
    cam.greyscale()
      
else:
    cam=camera()
    cam.default()
        
