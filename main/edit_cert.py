#!/usr/bin/python
import os as os
from PIL import Image
from pdf2image import convert_from_path
import sys
import time

# Constants
flag_path = "../lib/flag/flag.jpg"
file_not_found = "PDF File not found"
poppler = r"..\lib\poppler\bin"
bg_colour = (232,236,239)
cert_img = 'image_output.jpeg'
success_messages = ["Certificate File Located Successfully.", "Image Extracted from Certificate Successfully.", "Certificate Edited Successfully"]
error_messages = ["Certificate Path not Provided \nUsage: python edit_cert.py <path_to_cert>"]

def startEditCert():
    if os.path.exists(original_cert_path):
        print(success_messages[0])
        time.sleep(0.2)
        
        # Convert PDF to Image so that we can edit
        try:
            img_cert = convert_from_path(original_cert_path, poppler_path = poppler)  
            img_cert[0].save(cert_img, 'JPEG')
            print(success_messages[1])
            time.sleep(0.2)
        except IndexError as e:
            print("ERROR: " + str(e))

        # Load Flag Image
        img_flag = Image.open(flag_path)

        # Certificate image
        certificate = Image.open(cert_img)

        for i in range(0, 950):
            for j in range(1616, 1950):
                if i not in range(837, 886) or j not in range(1606, 1656):
                    certificate.putpixel((i,j), bg_colour)

        #insert flag
        certificate.paste(img_flag, (180, 1616))
        
        #save result as pdf
        certificate.save('certificate_with_flag.pdf', 'PDF', resolution=100.0)
        print(success_messages[2])
        os.remove(cert_img)

    else:
        print(file_not_found)
        
# Read file path and check if exists
try:
    original_cert_path = sys.argv[1]
    startEditCert()
except IndexError as e:
    print(error_messages[0])