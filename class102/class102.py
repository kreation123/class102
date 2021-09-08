import cv2
import random
import time
import dropbox
startTime=time.time ()
def takeShapShot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName='img' +str(number)+'.png'

        cv2.imwrite(imageName,frame)
        startTime =time .time
        result = False
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uplodeFile(imageName):
    accesstoken='sl.A4EhZrwzWQ7FmRGdOtOShqNz72GcV4a55OyKRyXRJUi4Aeqkx8XsiEqAAtxue9TdKAw5GCwlNfyunThqzHlYh-ViorMMEilw2GoSpwgX-nwG4uxpaM-vEFbedqIvFFi7xQ46A_o'
    file= imageName
    fileFrom = file
    fileto ="/TestFolder/"+imageName
    dbx = dropbox.DropBox(accesstoken)
    with open(fileFrom,'rb') as f:
        dbx.files_uplode(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeShapShot()
            uplodeFile(name)
main()