
import cv2
import time
import datetime

cap = cv2.VideoCapture(1)

if cap.isOpened == False:
    print('CapError')

while(True):
    ret, frame = cap.read()

    if ret is None:
        print('フレーム取得できません')
        break
    #cv2.imshow('Cap_parking', frame)
    cur_time = datetime.datetime.now()
    img_name = "./Pictures/{0:%Y%m%d_%H%M%S}.jpg".format(cur_time)


    cv2.imwrite(img_name, frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(120)

cap.release()
cv2.destroyAllWindows()
