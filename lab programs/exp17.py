
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Error: Image not found")
else:
    cv2.putText(img, "WATERMARK",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imwrite("watermarked_image.jpg", img)

    result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(result)
    plt.title("Watermarked Image")
    plt.axis("off")
    plt.show()
