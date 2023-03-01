# Finding_Location_of_Bounding_Box
This repository is created to help idenitfing the location of the bounding boxes on an image. As we looked into the training data for custom objecte detection in YOLO, there appeared confusion in some of the images. Some of the annotations provided by the person labelling bounding boxes were wrongfully labelled. This repository draws bounding boxes from the annotation files on the respective image.

## Bounding box from YOLO annotations
The [check_bounding_box_yolo.py](https://github.com/TahmidTowsifAhmed/Finding_Location_of_Bounding_Box/blob/main/check_bounding_box_yolo.py) script drwas bounding boxes on the images with simple application of OpenCV. Put the location of the image in line 3 and annotation in line 5. Then running the script will save a new image in the present working directory, which will have the bounding boxes drawn around the objects based on the annotations.
