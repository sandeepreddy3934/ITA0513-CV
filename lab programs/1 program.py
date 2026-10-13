import cv2
import numpy as np
img = np.zeros((250, 250, 3), dtype=np.uint8)
cv2.imshow("blackImage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
