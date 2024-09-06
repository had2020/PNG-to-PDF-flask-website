from fpdf import FPDF
import os
from PIL import Image

def convert_to_8bit(file):
    img = Image.open("uploads/IMG_0317_Small.png")
    img = img.convert("RGB")  # Convert to RGB (8-bit per channel)
    img.save("uploads/IMG_0317_Small_8bit.png")
    return("uploads/IMG_0317_Small_8bit.png")

def pngtopdf(file):
    new_file = convert_to_8bit(file)
    pdf = FPDF()
    pdf.add_page()
    pdf.image(new_file, x=10, y=10, w=190, h=277)
    pdf.output("pdf-with-image.pdf")
    os.remove(new_file)
    return()
