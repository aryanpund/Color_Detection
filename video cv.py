import cv2
cap = cv2.VideoCapture("D:/Backup 2024/DCIM/VN20220911_125244.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

