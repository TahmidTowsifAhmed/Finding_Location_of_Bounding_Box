import cv2

image = cv2.imread ('path_to_image.jpg')

with open('path_to_annotation.txt', 'r') as f:
    annotations = f.readlines()
    
for annotation in annotations:
    x_center, y_center, width, height = map(float, annotation.split()[1:])
    x_min = int((x_center - width / 2) * image.shape[1])
    y_min = int((y_center - height / 2) * image.shape[0])
    x_max = int((x_center + width / 2) * image.shape[1])
    y_max = int((y_center + height / 2) * image.shape[0])
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite ('image.jpg', image)