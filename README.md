#  OCR Image Processing Pipeline

##  Project Overview

This project implements a complete Optical Character Recognition (OCR) pipeline using Python, combining advanced image preprocessing techniques with the Tesseract OCR engine to improve text extraction accuracy from images.

The system processes a folder of images, applies multiple preprocessing strategies, performs OCR, and exports structured results into a CSV file.

This project demonstrates practical skills in Computer Vision, Image Processing, Text Extraction, OCR Optimization, and Post-processing techniques.

---

##  Technical Architecture

The OCR system follows a structured three-stage pipeline:

### 1️⃣ Image Preprocessing

To improve OCR accuracy, several preprocessing operations are applied:

- Grayscale conversion  
- Contrast enhancement  
- Image resizing (resolution scaling)  
- Binary thresholding  
- Noise reduction  

Libraries used:
- OpenCV  
- Pillow (PIL)  

---

### 2️⃣ OCR Engine

Text extraction is performed using:

- Tesseract OCR Engine  
- pytesseract (Python wrapper)

Configuration parameters:
- OCR Engine Mode (--oem 3)  
- Page Segmentation Mode (--psm 6)  
- Multi-language support (fra + eng)  

---

##  Technologies & Tools Used

- Python – Core programming language  
- OpenCV – Image preprocessing  
- Pillow (PIL) – Image manipulation  
- Tesseract OCR – Text recognition engine  
- pytesseract – Python interface for Tesseract  
- CSV module – Structured result export  
- Git – Version control  
- GitHub – Project hosting  

---

##  Project Structure

OCRProject/
│
├── image/ et 1/          # Input images  
├── main.py              # Main OCR pipeline  
├── ocr_results.csv      # Output results  
└── README.md            # Project documentation  

---

##  Installation & Usage

1️⃣ Clone the repository

git clone https://github.com/takwa309/OCRProject.git  
cd OCRProject  

2️⃣  Install Tesseract OCR

Download and install Tesseract:  
https://github.com/tesseract-ocr/tesseract  

Update the Tesseract path inside the script if needed:

pytesseract.pytesseract.tesseract_cmd = r"YOUR_PATH_TO_TESSERACT"

3️⃣ Run the project

python main.py  

The extracted text will be saved in:

ocr_results.csv  

---

## Technical Resources

OCR & Tesseract:
- https://pypi.org/project/pytesseract/  
- https://github.com/tesseract-ocr/tesseract  
- https://realpython.com/python-tesseract-ocr/  

Image Preprocessing:
- https://docs.opencv.org/  
- https://pyimagesearch.com/category/ocr/  
- https://pyimagesearch.com/2021/08/16/image-thresholding-with-opencv/  

Improving OCR Accuracy:
- https://pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/  
- https://towardsdatascience.com/improving-ocr-accuracy-with-opencv-and-python  

Advanced OCR Alternatives:
- https://github.com/JaidedAI/EasyOCR  
- https://github.com/PaddlePaddle/PaddleOCR  

---

##  Future Improvements

- Automatic deskew (rotation correction)  
- Text detection using EAST or CRAFT  
- Integration with deep learning OCR models  
- Web interface (Flask or FastAPI)  
- Evaluation metrics implementation (CER / WER)  


