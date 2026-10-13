
import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Error: Image not found")
else:
    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize to bigger size
    bigger = cv2.resize(img, None, fx=2, fy=2,
                        interpolation=cv2.INTER_LINEAR)

    # Resize to smaller size
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_AREA)

    # Display images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(bigger)
    plt.title("Bigger Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(smaller)
    plt.title("Smaller Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
