import cv2

# Initialize the camera (0 is the default camera)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Could not open camera")
    exit()

# Capture a single frame
ret, frame = camera.read()

# Check if the frame was captured
if ret:
    # Save the image to a file
    image_path = "captured_image.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Image saved at {image_path}")
else:
    print("Failed to capture image")

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
