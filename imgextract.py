import cv2
import pytesseract

def extract1(path):
    eimg2 = cv2.imread(path)
    # eimg2 = cv2.resize(eimg2, None, fx=1, fy=1)

    box = pytesseract.image_to_data(eimg2)
    for x, b in enumerate(box.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(eimg2, (x, y), (w + x, h + y), (0, 0, 267), 2)
                cv2.putText(eimg2, b[11], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (50, 50, 267), 2)
    cv2.imshow('Result', eimg2)
    cv2.waitKey(0)