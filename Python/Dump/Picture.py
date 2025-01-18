from cv2 import *

# Initialize the camera (0 is typically the default camera)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Read a frame from the camera
ret, frame = camera.read()

# If a frame is captured successfully, save it as an image
if ret:
    cv2.imwrite("captured_image.jpg", frame)
    print("Picture taken and saved as 'captured_image.jpg'")
else:
    print("Error: Could not capture image.")

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
