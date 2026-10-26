
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Error: Image not found")
else:
    h, w = img.shape[:2]

    # Select ROI
    x, y = w // 4, h // 4
    roi = img[y:y+h//4, x:x+w//4].copy()

    # Copy and paste ROI
    result = img.copy()
    rh, rw = roi.shape[:2]

    result[0:rh, 0:rw] = roi

    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("ROI Copy and Paste")
    plt.axis("off")
    plt.show()
