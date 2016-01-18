import os 
import time 
import sys


FRAMES = 14
FPS_IN = 10
FPS_OUT =  10


TIMEBETWEEN = 1
FILMLENNGTH =  float( FRAMES / FPS_IN )

os.system("cd 192.168.1.106:8000")
#aqui agt vai pro diretorio do server e salva lá ja  oia ai q doidera :B
os.system("avconv -r %s -i image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=1600:1200,scale=320:240 coisinhas.mp4" % (FPS_IN, '%3d', FPS_OUT))
