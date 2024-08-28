import pdf2image
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

def generate_pdf(url):
    # Load 
    with open('example.pdf', 'rb') as file:
        pages = pdf2image.convert_from_bytes(file.read())

    # Save 
    for page in pages:
        img = Image.frombytes('RGB', page.size, page.tobytes())
        img.save(f'output_{i}.png')
        i += 1
