import pytesseract
import numpy as np
import copy
from pytesseract import Output
import cv2


def process(img: np.ndarray) -> str:
    text_from_thresh_img = pytesseract.image_to_string(
        img, lang="eng", config="--psm 3"
    )
    text_from_thresh_img = text_from_thresh_img.replace("\n", " ").strip()
    return text_from_thresh_img


def process_with_detections(img: np.ndarray) -> np.ndarray:
    plot_img = copy.deepcopy(img)
    plot_img_template = copy.deepcopy(img)
    d = pytesseract.image_to_data(plot_img, config="--psm 3", output_type=Output.DICT)
    if len(plot_img.shape) < 3:
        plot_img_template = np.zeros(plot_img.shape + (3,))
        plot_img_template[:, :, 0] = plot_img
        plot_img_template[:, :, 1] = plot_img
        plot_img_template[:, :, 2] = plot_img

    n_boxes = len(d["level"])
    for i in range(n_boxes):
        (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
        if w != plot_img_template.shape[1] and h != plot_img_template.shape[0]:
            text = d["text"][i]
            cv2.rectangle(plot_img_template, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                plot_img_template,
                text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 0, 255),
                3,
            )  # thank you --> https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
    return plot_img_template
