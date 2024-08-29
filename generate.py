from fpdf import FPDF
import os

def pngtopdf(file):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("docs/fpdf2-logo.png", x=20, y=60)
    pdf.output("pdf-with-image.pdf")
    return()