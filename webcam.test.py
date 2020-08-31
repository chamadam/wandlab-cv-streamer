# -*- encoding: utf-8 -*-
#-------------------------------------------------#
# Date created          : 2020. 8. 18.
# Date last modified    : 2020. 8. 19.
# Author                : chamadams@gmail.com
# Site                  : http://wandlab.com
# License               : GNU General Public License(GPL) 2.0
# Version               : 0.1.0
# Python Version        : 3.6+
#-------------------------------------------------#

import cv2
import platform

src = 1

if platform.system() == 'Windows' :
    captrue = cv2.VideoCapture( src , cv2.CAP_DSHOW )
    
else :
    captrue = cv2.VideoCapture( src )

captrue.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captrue.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while captrue.isOpened():
    
    (grabbed, frame) = captrue.read()
    
    if grabbed:
        cv2.imshow('Wandlab Camera Window', frame)
 
        key = cv2.waitKey(1) & 0xFF
        if (key == 27): 
            break
 
captrue.release()
cv2.destroyAllWindows()