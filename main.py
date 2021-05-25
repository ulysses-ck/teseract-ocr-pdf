import os
import fitz
import pytesseract
import cv2
import io
from PIL import Image, ImageFile
from colorama import Fore, init
import platform

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Global var
strPDF, textScanned,  textScanned, inputTeEx, dirName = "","","","", ["images", "output_txt"]

# Get input from User
def gInUs():
    # Global var
    global strPDF
    global inputTeEx

    if(platform.system() == "Windows"):
        print(Fore.YELLOW + "[.] Insert path to your tesseract.exe" + Fore.RESET)
        inputTeEx = input()

    # Print input
    print(Fore.GREEN + "[!] Insert path to PDF file:" + Fore.RESET)
    inputUser = input()
    # -------------

    # Print an alert if input is not valid, if not, call to fun reDoc
    if(inputUser == "" or len(inputUser.split("\\"))  == 1):
        print(Fore.RED + "[X] Please put a valid PATH to a file" + Fore.RESET)
    else:
        extIm(inputUser)
    # -------------


# Extracting images
def extIm(fileStr):
    global dirName

    # open the file
    pdf_file = fitz.open(fileStr)

    # Create output folder if don't exists
    for i in dirName:
        try:
            os.makedirs(i)
            print(Fore.GREEN + "[!] Directory " , i ,  " Created"+ Fore.RESET)
        except FileExistsError:
            print(Fore.RED + "[X] Directory " , i ,  " already exists" + Fore.RESET)

    # List images if exists and print each one. if not extract all images uWu
    content = os.listdir("images")
    if(len(content) >= 1):
        # Print every img in content
        for i in content:
            print(Fore.YELLOW + f"This is an image: {i}" + Fore.RESET)
    else:
        # Iterate over PDF pages
        for page_index in range(len(pdf_file)):

            # get the page itself
            page = pdf_file[page_index]
            image_list = page.getImageList()

            # printing number of images found in this page
            if image_list:
                print(Fore.GREEN + f"[+] Found a total of {len(image_list)} images in page {page_index}" + Fore.RESET)
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
    # Global var
    global textScanned
    global dirName
    global inputTeEx


    pytesseract.pytesseract.tesseract_cmd = f"{inputTeEx}"


    # List the images
    content = os.listdir('images')

    for i in range(len(content)):
        # Reading each image in images
        image = cv2.imread(f'images/{content[i]}')

        # Scan text from image
        print(Fore.YELLOW + f"[.] Scan text from {content[i]}" + Fore.RESET)
        text = pytesseract.image_to_string(image,lang='spa')

        # Concate text scanned in a string
        textScanned += text

        # print
        print(Fore.GREEN + "[!] Finished scan text" + Fore.RESET)


        # Showing img input
        cv2.imshow('Image',image)
        # 0.5 milisecond
        cv2.waitKey(1000)

    # Create and write file txtResult.txt
    print(Fore.CYAN + "[.] Writing txtResult.txt" + Fore.RESET)
    fileTxt = open(f"{dirName[1]}/txtResult.txt", "w")
    fileTxt.write(textScanned)
    print(Fore.GREEN + "[!] File Writted" + Fore.RESET)
# Call to fun main
gInUs()