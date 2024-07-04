<a href="https://colab.research.google.com/github/jermwatt/ocr_preprocessing/blob/main/ocr_preprocessing_walkthrough.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# OCR preprocessing app, walkthrough, and demo

Explore the commonly overlooked pre-processing steps that help make Optical Character Recognition (OCR) models work properly in practice.

This repository contains code, a walkthrough notebook (`ocr_preprocessing_walkthrough.ipynb`), and streamlit demo app for playing around with common ocr pre-processing steps, and seeing their resulting effects on ocr quality.

All processing - from the various pre-processing steps to the ocr itself (here using the popular / classic [tesseract](https://github.com/tesseract-ocr/tesseract) model - are performed locally.


## Installation instructions

To create a handy tool for your own memes pull the repo and install the requirements file

```python
pip install -r requirements.txt
```

## Starting the streamlit app

Start the streamlit app by pasting the following in your terminal

```python
python -m streamlit run ocr/app.py
```

##  Ocr your own images

Note: you can drag and drop any desired image directly into the streamlit app, and play around with how pre-processing steps effect the final ocr output.


