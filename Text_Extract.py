
# coding: utf-8

# In[10]:

import cv2
import pytesseract
from PIL import Image

cam = cv2.VideoCapture(0)

cv2.namedWindow("Display medicine name..")

def return_text(text):
    return text

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Display medicine name..", frame)
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if not ret:
        break
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]    
        
    frame = gray
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
        text = pytesseract.image_to_string(Image.open(img_name))
        
        return_text(text)
        print(text)
        break
  
#         print("{} written!".format(text))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


# In[7]:

# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# im =Image.open("1.jpg")
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# text = pytesseract.image_to_string(Image.open("1.jpg"))
# print("T",text)

