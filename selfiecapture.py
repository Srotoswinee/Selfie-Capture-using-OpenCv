import cv2
import os
def capture_selfie_on_key_press():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    save_dir = 'selfies'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    selfie_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('Selfie Capture', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') and len(faces) > 0:
            selfie_count += 1
            selfie_filename = os.path.join(save_dir, f'selfie_{selfie_count}.png')
            cv2.imwrite(selfie_filename, frame)
            print(f'Selfie saved as {selfie_filename}')
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    capture_selfie_on_key_press()
