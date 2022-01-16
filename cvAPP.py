import cv2
import time
import random
startTime=time.time()
def TakeSnapShot():
    number = random.randint(1,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName='img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()
TakeSnapShot()
