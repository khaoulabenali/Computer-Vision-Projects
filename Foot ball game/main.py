import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
#importing all images :
imgBackground=cv2.imread("pictures/background.png")
imgBackground = cv2.resize(imgBackground,( 1280,720))
imgGameOver=cv2.imread("pictures/game_over.jpg")
imgGameOver = cv2.resize(imgGameOver,( 1280,720))
imgBall=cv2.imread("pictures/ball.png",cv2.IMREAD_UNCHANGED)
print(imgBall.shape)
imgBall = cv2.resize(imgBall,( 64,64))
print(imgBall.shape)
imgBat1=cv2.imread("pictures/images.jpg",cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.resize(imgBat1,( 100,100))
imgBat2=cv2.imread("pictures/ball.png",cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.resize(imgBat2,( 100,100))
#Hand detector :
detector = HandDetector(detectionCon=0.8, maxHands=2)
#variables :
ballpos = [100,100]
speedx = 15
speedy = 15
gameOver = False
score = [0,0]
while True:
  _,img=cap.read()
  img = cv2.flip(img,1)
  # Find the hand and its landmarks
  hands, img = detector.findHands(img,flipType=False)  # with draw
  #overlaying the backgroun image :
  img = cv2.addWeighted(img,0.2,imgBackground,0.8,0)

  #check for hands :
  if hands :
    for hand in hands :
      x,y,w,h=hand["bbox"]
      h1,w1,_ = imgBat1.shape
      y1 = y-h1//2
      y1=np.clip(y1,20,600)


      if hand['type'] == "Left" :
        img = cv2.rectangle(img, (70, y1+50), (70,y1+110), (255,255,255), 5)
        #img = cvzone.overlayPNG(img, imgBat1, (50, y1))
        if 50< ballpos[0] <h1+70 and y1<ballpos[1]<y1+h1:
          speedx=-speedx
          ballpos[0]+=30
          score[0]+=1
      if hand['type'] == "Right" :
        img = cv2.rectangle(img, (1115, y1+50 ), (1115, y1 + 110), (255, 255, 255), 5)
        #img = cvzone.overlayPNG(img, imgBat2, (1115, y1))
        if 1115< ballpos[0] <h1+1115 and y1-10<ballpos[1]<y1+70:
          speedx=-speedx
          ballpos[0] -= 400
          score[1]+=1

  #Game over :
  if ballpos[0]<40 or ballpos[0]>1130:
    gameOver=True
  if gameOver:
    img = imgGameOver
    cv2.putText(img, str(score[0])+str("-")+str(score[1]), (580, 550), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
    cv2.putText(img, "Press R to play again!", (480, 600), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),2)
    cv2.putText(img, "Press Q to quit game!", (480, 650), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

  #if the game is not over yet move the ball
  else:
      #move the ball :
      if ballpos[1]>=650 or ballpos[1]<=20:
           speedy=-speedy
      ballpos[0] += speedx
      ballpos[1] += speedy
      #draw the ball :
      img = cvzone.overlayPNG(img,imgBall,ballpos)
      cv2.putText(img,str(score[0]),(300,80),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),5)
      cv2.putText(img, str(score[1]), (900, 80), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
  cv2.imshow("Image",img)
  key = cv2.waitKey(1)
  if key == ord("r"):
    ballpos = [100, 100]
    speedx = 15
    speedy = 15
    gameOver = False
    score = [0, 0]
    imgGameOver = cv2.imread("pictures/game_over.jpg")
    imgGameOver = cv2.resize(imgGameOver, (1280, 720))
  if key == ord("q"):
    break

