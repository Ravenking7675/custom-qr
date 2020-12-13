from cairosvg import svg2png
from PIL import Image  


def topng(svg_data):

    svg2png(bytestring=svg_data, write_to='output.png', scale=4.0)
    
    
    #newsize = (300, 300) 
#im1 = im1.resize(newsize) 
#Shows the image in image viewer  
#im1.show()  

def insert_logo(logo_size=50):
    qr = Image.open('output.png')
    logo = Image.open('new_output.png')
    
    width, height = qr.size
    
    final_img = Image.new('RGBA', (width,height), (0, 0, 0, 0))
    
    
    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))
    
    
    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # put the logo in the qr code

    final_img.paste(qr, ((final_img.width - qr.width) // 2, (final_img.height - qr.height) // 2))
    final_img.paste(logo, ((final_img.width - logo.width) // 2, (final_img.height - logo.height) // 2), mask=logo)


    #qr.paste(logo, (xmin, ymin, xmax, ymax))

    final_img.show()
    
def make_qr_transparent():
    img = Image.open('output.png')
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (0, 0, 0, 255):
                pixdata[x, y] = (0, 0, 0, 0)

    img.save("output_transparent.png", "PNG")
    
def add_gradient():
    
    qr = Image.open('output_transparent.png')
    bg = Image.open('bg.png')
    
    width, height = qr.size
    final_img = Image.new('RGBA', (width,height), (0, 0, 0, 0))
    
    final_img.paste(bg, ((final_img.width - bg.width) // 2, (final_img.height - bg.height) // 2))
    final_img.paste(qr, ((final_img.width - qr.width) // 2, (final_img.height - qr.height) // 2), mask=qr)


    #qr.paste(logo, (xmin, ymin, xmax, ymax))

    final_img.show()
    final_img.save('gradient_back.png')
    
    
    
    
    
    
    
    
    
    
    
    
