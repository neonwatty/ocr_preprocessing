import cv2
import math
import numpy as np
from PIL import Image
from typing import Tuple
from deskew import determine_skew


def deskew_img(image: np.ndarray) -> np.ndarray:
    try:
        angle = determine_skew(image)
        old_width, old_height = image.shape[:2]
        angle_radian = math.radians(angle)
        width = abs(np.sin(angle_radian) * old_height) + abs(
            np.cos(angle_radian) * old_width
        )
        height = abs(np.sin(angle_radian) * old_width) + abs(
            np.cos(angle_radian) * old_height
        )

        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        rot_mat[1, 2] += (width - old_width) / 2
        rot_mat[0, 2] += (height - old_height) / 2
        return cv2.warpAffine(
            image,
            rot_mat,
            (int(round(height)), int(round(width))),
            borderValue=(0, 0, 0),
        )
    except:
        return image


def convert_img(img: "Image") -> np.ndarray:
    # img_orig = Image.open(img_path)
    img = np.array(img)
    return img


def normalize_img(img: np.ndarray) -> np.ndarray:
    return cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)


def denoise_img(img: np.ndarray) -> np.ndarray:
    return cv2.bilateralFilter(img, 5, 55, 60)


def grayscale_img(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def threshold_img(img: np.ndarray, threshold_val: int) -> np.ndarray:
    _, img_thresh = cv2.threshold(img, threshold_val, 255, 1)
    return img_thresh
