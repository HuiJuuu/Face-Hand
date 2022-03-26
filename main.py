from cvzone.FaceDetectionModule import FaceDetector
import cv2

#cam 불러오는 거
cap = cv2.VideoCapture(0)

# 얼굴관련 해서 만든 모델, 머신러닝(데이터)
# 인풋 -> 모델 -> 아웃풋
detector = FaceDetector()

while True:
    success, img = cap.read()

    #img를 imput으로 넣어준다
    img, bboxs = detector.findFaces(img)

    #만약 bboxs가 있으면 center 점 찍어주는 작업
    if bboxs:
        #bboxInfo - "id", "bbox", "score", "center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (225, 0, 255), cv2.FILLED)
    cv2.imshow("Image", img)
    # q버튼 누르면 나가기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()