'''
this file only used for black and white image 
the target object would be colored with black
otherwise make the image reversed

created 09.26 seunghwanly
'''

import os
from PIL import Image


def get_anotation(image_path):
    img = Image.open(image_path).convert('RGB')
    # get width and height
    w = img.size[0]
    h = img.size[1]

    pix = img.load()

    # get y position
    top_y, bottom_y = h + 1, 0
    # get x position
    right_x, left_x = 0, w + 1

    # find the arguments
    for i in range(w):
        for j in range(h):
            if sum(pix[i, j]) == 0:  # the condition where it finds the black
                if top_y > j: top_y = j
                if bottom_y < j: bottom_y = j
                if right_x < i: right_x = i
                if left_x > i: left_x = i

    # set attributes
    x_center = ((left_x + right_x) / 2) / w
    y_center = ((top_y + bottom_y) / 2) / h

    width = abs(right_x - left_x) / w
    height = abs(top_y - bottom_y) / h

    # <x_center> <y_center> <width> <height> - float values relative to width and height of image, it can be equal from (0.0 to 1.0]
    return (x_center, y_center, width, height)


# returns in alphabetical order
def get_directories(root_dir):
    result = []
    # find parent directories
    directories = os.listdir(root_dir)
    candidates = []
    for directory in directories:
        if len(directory) == 1: candidates.append(directory)
    candidates.sort()
    # add with sub items
    for candidate in candidates:
        curr_dir = root_dir + '/' + candidate
        items = os.listdir(curr_dir)
        for item in items:
            result.append(curr_dir + '/' + item)

    return result


def create_txt_file(root_dir, image_path):
    to_class = image_path[len(root_dir) + 1]
    file_name = image_path[len(root_dir) + 3:image_path.index('.png')]
    
    x_c, y_c, w, h = get_anotation(image_path)
    to_file = f'{ord(to_class) - 65} {x_c} {y_c} {w} {h}'
    
    f = open(f'{root_dir}/{to_class}/{file_name}.txt', 'w+')
    f.write(to_file)
    f.close()

    print(f'{root_dir}/{to_class}/{file_name}.txt --> DONE')


if __name__ == "__main__":
    root_dir = '/Users/iseunghwan/Downloads/dataset'
    tasks = get_directories(root_dir)
    for task in tasks:
        create_txt_file(root_dir, task)
    print('done')
