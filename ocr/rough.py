# # this cell takes in an image and roughs it up to better illustrate how pre-processing steps improve image clarity below
# from PIL import Image
# import numpy as np
# import os
# import cv2

# # load in image
# img_path = 'data/input/seal.jpg'
# image = cv2.imread(img_path)
# image = image/(np.std(image))
# image += np.mean(image)

# # add noise to image
# row,col,channels= image.shape
# mean = 0
# var = 0.1
# sigma = var**0.5
# gauss = np.random.normal(mean,sigma,(row,col,channels))
# gauss = gauss.reshape(row,col,channels)
# image = image + gauss

# # rotate image
# pil_image = Image.fromarray(np.uint8(image))
# pil_image = pil_image.rotate(25) 
# pil_image

# img_path = "data/input/seal_rotated.png"
# pil_image.save(img_path)