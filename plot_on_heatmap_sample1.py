import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

im = np.array(Image.open('Draft.png'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

print type(ax)
# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)

plt.show()


#https://stackoverflow.com/questions/21445005/drawing-rectangle-with-border-only-in-matplotlib
# from matplotlib import pyplot as plt
# from matplotlib.patches import Rectangle
# someX, someY = 0.5, 0.5
# fig,ax = plt.subplots()
# currentAxis = plt.gca()
# currentAxis.add_patch(Rectangle((someX - 0.1, someY - 0.1), 0.2, 0.2,
#                       alpha=1, facecolor='none'))
