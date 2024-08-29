from PIL import Image
import datetime

# URL == string
def generate_qrcode(url):
    # QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # adding URL to object
    qr.add_data(url)
    qr.make(fit=True)

    #image path
    time_obj = str(datetime.datetime.now())
    stringged_url = str(url)
    image_folder = "qr-code-pngs/"
    #image_name = stringged_url + time_obj to long names but sometimes works
    image_path = image_folder + time_obj + ".png"

    # create image for code
    img = qr.make_image(fill='black', back_color='white')
    img.save(image_path)

    return(image_path)

def generate_pdf(file):
    """
    image = Image.open(file)
    pdf_path = file.replace('.png', '.pdf')
    image.save(pdf_path, 'PDF', resolution=100.0)
    return('pdf_path.png')
    """

    # Open 
    img = Image.open(file)

    # Convert
    img = img.convert("RGB")

    # Save 
    img.save("output.pdf")

    return('output.pdf')