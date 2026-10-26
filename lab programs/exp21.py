
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(opening, cmap="gray")
    plt.title("Opening")
    plt.axis("off")

    plt.show()
