import cv2
import numpy as np
import os
from email.message import EmailMessage
import ssl
import smtplib
import requests

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['None', 'navin']
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
imgbg=cv2.imread('C:/Users/revan/PycharmProjects/face/trainer/a1.png')

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])


        if (confidence <= 50):
            id = names[1]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            email_sender = 'navinprasath21@gmail.com'
            email_password = 'qbmzyhrlpmjnoxzj'
            email_receiver = ['sanjayram.r2021ai@sece.ac.in','navinprasath.m2021ai@sece.ac.in','pramoth.kj2021ai@sece.ac.in']

            subject = 'UnAuthorized Access'
            body = """
             Some unauthorized person is accessing
             We need you to check it out.......!!!
            """

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            count = 0

            token = "6192670603:AAGmbNb34qBncleSrqlhXpgLXLHTipV8z_M"
            url = f"https://api.telegram.org/bot{token}"
            st="""🛑...EMERGENCY ALERT...🛑
                       UNAUTHORIZED FACE DETECTED
                       SECURITY BREACH....🧑🏼‍✈️"""

            params = {"chat_id": "2093355611", "text":st}
            r = requests.get(url + "/sendMessage", params=params)
            count+=1


        imgbg[150:150 + 480, 80:80 + 640] = img
        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', imgbg)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()