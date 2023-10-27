# **tesseract ocr pdf**
It´s a script extract PDF´s images and use **tesseract OCR** for scan it

## Pre-installation dependencies
Before you can run it, you need to install Python 3.8, onwards, and tesseract OCR
### Python 3
You can download for your OS from their [Oficial Download Page](https://www.python.org/downloads/)

### tesseract

#### Windows
For Windows, you can download the binary installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).

## Install dependencies

```
$ pip install pillow
$ pip install pytesseract
$ pip install opencv-python
$ pip install PyMuPDF
```

## Usage

When finish the installation, you can run the script
```
$ cd tesseract-ocr-pdf
$ python main.py
```

### Windows
You need to provide the path to your tesseract.exe. For example:
```
> [!] Insert path to your tesseract.exe
> C:\Users\User\tesseract\tesseract.exe
```
Then, the path to your PDF´file
```
> [!] Insert path to your tesseract.exe
> C:\Users\User\Documents\file.pdf
```
And then, the script starts to extract images, scan and create the file with the text output
