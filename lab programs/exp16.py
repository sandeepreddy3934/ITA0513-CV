
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Error: Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    result = cv2.convertScaleAbs(cv2.addWeighted(
        cv2.convertScaleAbs(sobel_x), 0.5,
        cv2.convertScaleAbs(sobel_y), 0.5, 0
    ))

    plt.imshow(result, cmap="gray")
    plt.title("Sobel Edge Detection")
    plt.axis("off")
    plt.show()
