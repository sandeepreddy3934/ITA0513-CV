
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Error: Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated)
    plt.title("270 Degree Clockwise")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
