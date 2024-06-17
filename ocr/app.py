from ocr import ocr_base_dir
from ocr.preprocessing import (
    convert_img,
    normalize_img,
    grayscale_img,
    denoise_img,
    deskew_img,
    threshold_img,
)
from ocr.ocr_tesseract import process, process_with_detections
import streamlit as st
from PIL import Image, ImageFile
import io


ImageFile.LOAD_TRUNCATED_IMAGES = True
st.set_page_config(page_title="OCR preprocessing playground")
st.title("OCR preprocessing playground")

with st.container(border=True):
    checks = st.columns(4)
    with checks[0]:
        normalize = st.checkbox("normalize", value=True)
    with checks[1]:
        denoise = st.checkbox("denoise", value=True)
    with checks[2]:
        deskew = st.checkbox("deskew", value=True)
    with checks[3]:
        thresh = st.checkbox("threshold", value=True)
    slides = st.columns(1)
    with slides[0]:
        thresh_io = st.slider(
            min_value=0, max_value=255, value=200, label="threshold val"
        )

default_file = ocr_base_dir + "/data/input/seal_rotated.png"
uploaded_file = st.file_uploader("Choose an image file...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # with tempfile.TemporaryDirectory() as tmpdirname:
    # read in file name
    file = uploaded_file.read()
    bytes_data = uploaded_file.getvalue()
    img = Image.open(io.BytesIO(bytes_data))
else:
    img = Image.open(default_file)

# define columns
a, col0, b = st.columns([1, 20, 1])
col1, col2, col3 = st.columns([1, 1, 1])
col4, col5, col6 = st.columns([1, 1, 1])

if thresh_io:
    # convert image
    img = convert_img(img)
    with col2.container(border=True):
        st.image(img, output_format="auto", caption="original image")

    # normalize
    if normalize:
        img = normalize_img(img)
        with col4.container(border=True):
            st.image(img, output_format="auto", caption="normalized image")

    # denoise
    if denoise:
        img = denoise_img(img)

    # gray_img
    img = grayscale_img(img)
    with col5.container(border=True):
        st.image(img, output_format="auto", caption="grayscale image")

    # deskew
    if deskew:
        img = deskew_img(img)
        with col6.container(border=True):
            st.image(img, output_format="auto", caption="deskew image")

    # thresh
    if thresh:
        img = threshold_img(img, threshold_val=thresh_io)
        with col3.container(border=True):
            st.image(img, output_format="auto", caption="threshold image")

    # ocr the image and get back text
    ocr_text = process(img).replace("\n", " ").strip()
    with col0.container(border=True):
        st.text_area(
            value=ocr_text,
            placeholder="ocr'd text will be shown here",
            label="ocr text",
        )

    # ocr process
    img = process_with_detections(img)
    with col1.container(border=True):
        st.image(
            img, output_format="auto", caption="ocr image", clamp=True, channels="BGR"
        )
