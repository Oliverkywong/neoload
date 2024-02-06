# import cv2
from PIL import Image
import pytesseract
# from matplotlib import pyplot as plt
# import numpy as np

img_file = 'hw.jpg'

img = Image.open(img_file)

ocr = pytesseract.image_to_string(img)

print(ocr)

# img = cv2.imread(im_file)

# # cv2.imshow("orimg", img)
# # cv2.waitKey(0)

# def display(im_path):
#     dpi = 300
#     im_data = plt.imread(im_path)
#     print(im_data.shape)
#     # height, width, dept = im_data.shape
#     height, width = im_data.shape

#     figsize = width / float(dpi), height / float(dpi)

#     fig = plt.figure(figsize=figsize)
#     ax = fig.add_axes([0, 0, 1, 1])

#     ax.axis('off')
#     ax.imshow(im_data, cmap='gray')
#     plt.show()

# # inverted_image = cv2.bitwise_not(img)
# # cv2.imwrite('inverted.jpg', inverted_image)
# # display('inverted.jpg')
# def grayscale(img):
#     return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray = grayscale(img)
# # cv2.imwrite('gray.jpg', gray)
# # display('gray.jpg')

# thresh, im_bw = cv2.threshold(gray, 200, 230, cv2.THRESH_BINARY)
# # cv2.imwrite('bw.jpg', im_bw)
# # display('bw.jpg')

# def noise_removal(image):
#     kernel = np.ones((1,1), np.uint8)
#     image = cv2.dilate(image, kernel, iterations=1)
#     kernel = np.ones((1,1), np.uint8)
#     image = cv2.erode(image, kernel, iterations=1)
#     image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#     image = cv2.medianBlur(image, 3)
#     return (image)

# no_noise = noise_removal(im_bw)
# # cv2.imwrite('no_noise.jpg', no_noise)
# # display('no_noise.jpg')

# def thin_font(image):
#     image = cv2.bitwise_not(image)
#     kernel = np.ones((3,3), np.uint8)
#     image = cv2.erode(image, kernel, iterations=1)
#     image = cv2.bitwise_not(image)
#     return (image)

# eroded_image = thin_font(no_noise)
# cv2.imwrite('eroded_image.jpg', no_noise)
# display('eroded_image.jpg')