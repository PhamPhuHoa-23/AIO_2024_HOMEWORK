import numpy as np
import cv2


def compute_diffirence(bg_img, input_img):
    return cv2.cvtColor(bg_img - input_img, cv2.COLOR_BGR2GRAY)


def compute_binary_mask(diffirence_single_channel):
    return np.where(diffirence_single_channel > 0, 1, 0)


def replace_background(bg1_image, bg2_image, ob_image):
    diffirence_single_channel = compute_diffirence(bg1_image, ob_image)

    binary_mask = compute_binary_mask(diffirence_single_channel)

    binary_mask = cv2.merge([binary_mask, binary_mask, binary_mask])

    output = np.where(binary_mask == 1, ob_image, bg2_image)

    return output


if __name__ == '__main__':
    bg1_image = cv2.imread('GreenBackground.png')
    bg1_image = cv2.resize(bg1_image, (678, 381))

    ob_image = cv2.imread('Object.png', 1)
    ob_image = cv2.resize(ob_image, (678, 381))

    bg2_image = cv2.imread('NewBackground.jpg')
    bg2_image = cv2.resize(bg2_image, (678, 381))

    result = replace_background(bg1_image=bg1_image, bg2_image=bg2_image, ob_image=ob_image)

    cv2.imshow(result, 'Change Background')
