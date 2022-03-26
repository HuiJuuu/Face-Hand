import cv2
from cvzone.HandTrackingModule import HandDetector
#https://google
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
cx, cy, w, h = 100, 100, 200, 200
while True:
    # 계속해서 이미지를 불러와서 영상을 보여준다.
    success, img = cap.read()
    #Find the hand and its landmarks
    #이미지 좌우반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img) #with draw
    # hands = detector.findHands(img, draw=False) #without draw

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 landmark points
        print(lmList1[8]) #Bounding box info x, y, w, h
        bbox1 = hand1["bbox"] #center of the hand cx, cy
        centerPoint1 = hand1['center']  #Handtype left or right
        handType1 = hand1['type']
        fingers1 = detector.fingersUp(hand1)
        l, _, _ = detector.findDistance((lmList1[8][0], lmList1[8][1]),(lmList1[12][0], lmList1[12][1]), img)
        if l < 50:
            if cx -w // 2 < bbox1[0] < cx +w //2 and cy-h//2 < bbox1[1] < cx +h//2:
                colorR = 0, 255, 0
                cx, cy = bbox1[0], bbox1[1]

        else:
            colorR = (255, 0, 255)
    #그냥 상자 그리기
    cv2.rectangle(img, (cx - w//2, cy-h//2), (cx +w//2, cy + h//2), colorR, cv2.FILLED)
    #display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2. destroyAllWindows()