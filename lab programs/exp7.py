
import cv2

# Read the video
cap = cv2.VideoCapture(r"C:\Users\reddy\Videos\Screen Recordings\Screen Recording 2026-10-03 155403.mp4")

if not cap.isOpened():
    print("Error: Video not found!")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Slow motion
        cv2.imshow("Slow Motion", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Read video again for fast motion
cap = cv2.VideoCapture(r"C:\Users\reddy\Downloads\video.mp4")

if cap.isOpened():
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Fast motion: skip frames
        cv2.imshow("Fast Motion", frame)

        # Skip the next frame
        cap.grab()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
