
import cv2
import matplotlib.pyplot as plt

# Reference image containing a watch
watch = cv2.imread(r"C:\Users\reddy\Downloads\watch.jpg")

# Image in which the watch must be recognized
img = cv2.imread(r"C:\Users\reddy\Downloads\test.jpg")

if watch is None or img is None:
    print("Image not found. Check both image paths.")
else:
    gray1 = cv2.cvtColor(watch, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1000)

    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    if des1 is None or des2 is None:
        print("No features detected")
    else:
        matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING, crossCheck=True
        )
        matches = matcher.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        result = cv2.drawMatches(
            watch, kp1, img, kp2, matches[:30],
            None, flags=2
        )

        plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.title("Watch Feature Matching")
        plt.axis("off")
        plt.show()

        if len(matches) >= 10:
            print("Possible watch match detected")
        else:
            print("Watch match not confirmed")

