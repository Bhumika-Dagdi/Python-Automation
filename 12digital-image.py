import numpy as np
import cv2

# Create a black image (512x512, 3 color channels)
image = np.zeros((512, 512, 3), dtype=np.uint8)

# Fill the background with blue color (BGR format)
image[:] = (255, 0, 0)  # Blue background

# Draw a green rectangle (top-left to bottom-right)
cv2.rectangle(image, (300, 150), (200, 200), (0, 255, 0), thickness=3)

# Draw a red circle (center, radius, color)
cv2.circle(image, center=(350, 150), radius=75, color=(0, 0, 255), thickness=-1)

# Put some white text on the image
cv2.putText(image, 'My Name is Bhumika Dagdi!', (130, 300), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Show the image
cv2.imshow('Custom Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
