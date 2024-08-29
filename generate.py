from fpdf import FPDF
import os

def pngtopdf(file):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(file, x=10, y=10, w=190, h=277)
    pdf.output("pdf-with-image.pdf")
    return()
