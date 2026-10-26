
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

    plt.imshow(tophat, cmap="gray")
    plt.title("Top Hat Operation")
    plt.axis("off")
    plt.show()
