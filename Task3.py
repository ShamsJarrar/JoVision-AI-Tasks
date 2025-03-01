import cv2
import numpy as np
import pandas as pd
import os


test_image_path = "./Resources/task3/000099.jpg"
test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

# To find finger coordinates
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'X: {x}, Y: {y}')

# if test_image is not None:
#     right_half = test_image[:, test_image.shape[1] // 2:]  # Get right half of the image
#     cv2.imshow('Right Half - Click to get coordinates', right_half)
#     cv2.setMouseCallback('Right Half - Click to get coordinates', click_event)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

coordinates = {
    'thumb': (147, 247, 200, 232),
    'finger1': (121, 145, 3, 110),
    'finger2': (81, 104, 2, 112),
    'finger3': (49, 73, 1, 108),
    'finger4': (3, 25, 2, 112)
}

test_blue_area = test_image[:, test_image.shape[1] // 2 :]
THRESHOLD = np.mean(test_blue_area) * 1.55


images_path = "./Resources/task3"
data = []

def get_line_color(image):
    bottom_area = image[-3]
    color = np.mean(bottom_area)
    return 1 if color > 100 else 0

def check_pressure(image):
    line_color = get_line_color(image)
    pressure = []
    
    if line_color == 0 :
        pressure = [0, 0, 0, 0, 0]
    else:
        blue_area = image[:, image.shape[1] // 2:]
        for key, (y1, y2, x1, x2) in coordinates.items():
            finger_area = blue_area[y1:y2, x1:x2]
            isTherePressure = np.any(finger_area >= THRESHOLD)
            pressure.append(1 if isTherePressure else 0)
    return pressure

for file in os.listdir(images_path):
    cur_image_path = os.path.join(images_path, file)
    image = cv2.imread(cur_image_path, cv2.IMREAD_GRAYSCALE)

    image_data = check_pressure(image)
    data.append([file] + image_data)

cols = ['ImageName', 'thumb', 'finger1', 'finger2', 'finger3', 'finger4']
df = pd.DataFrame(data, columns=cols)
df.to_excel("./Resources/task3_data.xlsx", index=False)

print("Images Processed! Check task3_data.xlsx to find the result!")