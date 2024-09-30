# ocr_utils.py

import easyocr
import numpy as np

# Initialize the EasyOCR reader for Hindi and English
reader = easyocr.Reader(['hi', 'en'])


def extract_text(image_np):
    """
    Extract text from a NumPy array image using EasyOCR.

    Parameters:
    - image_np: NumPy array representation of the image.
    Returns:
    - full_text: Extracted text as a single string.
    """
    extracted_text = reader.readtext(image_np, detail=0)
    full_text = " ".join(extracted_text)
    return full_text
