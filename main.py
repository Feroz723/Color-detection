import cv2
from util import get_limits
from PIL import Image

yellow = [0, 255, 255] #BGR
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)
    
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox() #bounding box for the color image


    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) #original frame, upper left corner, right corner, green color on shown object, thickness

    if not ret:
        print("Error: Failed to capture image.")
        break
    cv2.imshow('Video Feed', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Video capture stopped by user.")
        break

cap.release()
cv2.destroyAllWindows()
