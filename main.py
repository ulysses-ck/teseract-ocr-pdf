import os
import fitz
import pytesseract
import cv2
import io
from PIL import Image, ImageFile
from colorama import Fore, init

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Global var
strPDF = ""
textScanned = ""

# Get input from User
def gInUs():

    global strPDF

    # Print input
    print(Fore.GREEN + "[!] Insert path to PDF file:" + Fore.RESET)
    inputUser = input()
    # -------------

    # Print an alert if input is not valid, if not, call to fun reDoc
    if(inputUser == "" or len(inputUser.split("\\"))  == 1):
        print(Fore.RED + "Please put a valid PATH to a file" + Fore.RESET)
    else:
        extIm(inputUser)
    # -------------


# Extracting images
def extIm(fileStr):
    dirName = "images"

    # open the file
    pdf_file = fitz.open(fileStr)

    # Create output folder if don't exists
    try:
        os.makedirs(dirName)
        print(Fore.GREEN + "[!] Directory " , dirName ,  " Created"+ Fore.RESET)
    except FileExistsError:
        print(Fore.RED + "[X] Directory " , dirName ,  " already exists" + Fore.RESET)


    # iterate over PDF pages
    for page_index in range(len(pdf_file)):

        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()

        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print(Fore.RED + "[!] No images found on page", page_index, Fore.RESET)

        for (image_index, img) in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"images/image{page_index+1}_{image_index}.{image_ext}", "wb"))
    reImg()

def reImg():
    global textScanned

    # List the images
    content = os.listdir('images')
    pytesseract.pytesseract.tesseract_cmd = r'R:/Programas\Tesseract\tesseract.exe'

    for i in range(len(content)):

        image = cv2.imread(f'images/{content[i]}')
        text = pytesseract.image_to_string(image,lang='spa')
        textScanned += text
        print('Texto: ',text)


        # cv2.imshow('Image',image)
        # cv2.waitKey(10)
        # cv2.destroyAllWindows()
# Call to fun main
gInUs()