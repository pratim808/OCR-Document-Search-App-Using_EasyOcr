
# OCR and Document Search Web Application Prototype (Using EasyOCR)

## Introduction
This project is a web-based prototype designed to perform Optical Character Recognition (OCR) on images containing text in both Hindi and English. The application allows users to upload an image, extract the text, and search for specific keywords within the extracted content. The goal is to demonstrate the functionality of OCR technology in a user-friendly web application.

## Technologies
The following technologies and libraries were used in this project:

- **Python**: Programming language used for development.
- **EasyOCR**: Library for performing OCR on images.
- **Streamlit**: Framework for building the web application interface.
- **Pillow**: Library for image processing.

## Requirements
To run this project, you will need the following libraries installed:

```plaintext
easyocr
streamlit
Pillow
```





## Project Structure



```

/OCR-Document-Search-App
│
├── app.py              # Main application file
├── ocr_utils.py        # Utility functions for OCR processing
└── requirements.txt     # List of required libraries

```
# How to Run the Application 

## 1.Clone the Repository:


```
git clone <repository-url>
```

## 2.Navigate to the Project Directory:


```
cd OCR-Document-Search-App
```

## 3.Install Dependencies:

```
pip install -r requirements.txt
```
## 4.Run the Application:

```
streamlit run app.py
```
## 5.Access the Application:
```
Open your web browser and go to http://localhost:8501.
```

##Features 

##Image Upload: Users can upload images in JPG, JPEG, or PNG format.
Text Extraction: The application uses EasyOCR to extract text from the uploaded image.
Keyword Search: Users can enter keywords to search within the extracted text, with matching sections highlighted.

## Features


- **Image Upload**: Users can upload images in JPG, JPEG, or PNG format.
- **Text Extraction**: The application uses EasyOCR to extract text from the uploaded image.
- **Keyword Search**: Users can enter keywords to search within the extracted text, with matching sections highlighted.
## Deployment
The application can be deployed on platforms such as Streamlit Sharing or Hugging Face Spaces. Follow their instructions to make your application accessible via a public URL.
## Live URL

https://huggingface.co/spaces/Shabdobhedi/Ocr-Using-Easy-Ocr
## Conclusion
This project demonstrates how OCR technology can be integrated into a web application, providing an efficient tool for extracting and searching text from images.
## Demo

https://drive.google.com/file/d/12W-EzBGLtuOGTG8PtQd8GACj7dNW6xJG/view?usp=sharing

