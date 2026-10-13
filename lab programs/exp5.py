
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    for color, name in zip(colors, names):
        hist = cv2.calcHist([img], [colors.index(color)],
                            None, [256], [0, 256])
        plt.plot(hist, color=color, label=name)

    plt.title("Color Histogram")
    plt.xlabel("Color Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.show()

analyze_histogram(r"C:\Users\reddy\Downloads\tinea.jpg")
