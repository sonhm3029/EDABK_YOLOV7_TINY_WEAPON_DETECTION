# Import packages
import cv2
 
# Lists to store the bounding box coordinates
top_left_corner=[]
bottom_right_corner=[]
 
# function which will be called on mouse input
def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables 
  global top_left_corner, bottom_right_corner
  # Mark the top left corner when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]    
    # Draw the rectangle
    print(top_left_corner, bottom_right_corner)
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Window",image)
 
# Read Images
image = cv2.imread("background_1.jpg")
print(image.shape)
# Make a temporary image, will be useful to clear the drawing
temp = image.copy()
# Create a named window
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)
 
k=0
# Close the window when key q is pressed
while k!=113:
  # Display the image
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  # If c is pressed, clear the window, using the dummy image
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Window", image)
 
cv2.destroyAllWindows()

# # import PIL module
# from PIL import Image

# # Front Image
# filename = 'assets/img/knife_1.png'

# # Back Image
# filename1 = 'background_1.jpg'

# # Open Front Image
# frontImage = Image.open(filename)

# # Open Background Image
# background = Image.open(filename1)

# # Convert image to RGBA
# background.show()
# frontImage = frontImage.convert("RGBA")

# # Convert image to RGBA
# background = background.convert("RGBA")

# # Calculate width to be at the center
# width = (background.width - frontImage.width) // 2

# # Calculate height to be at the center
# height = (background.height - frontImage.height) // 2

# # Paste the frontImage at (width, height)
# background.paste(frontImage, (width, height), frontImage)

# # Save this image
# background.save("new.png", format="png")
