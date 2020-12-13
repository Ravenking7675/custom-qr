''' Styles available -->
    arrow, circle, classic, default, heavyround, lightround, sieve

    Eye Shapes available -->
    circle, cushion, default, diamond, dots, heavyround, leaf, left_eye, right_eye, shield, sieve, star
'''

import qrlib
from pngconverter import topng
from PIL import Image
from pngconverter import insert_logo
from pngconverter import make_qr_transparent, add_gradient

print("\n---------------------------\nLet's create a custom QR Code for you\n---------------------------\n")
text = input("Enter text for the custom QR Code : ")

print("\n---------------------------\nChoose a style for the QR Code from the options below \n---------------------------\n")
qr_style = input("arrow, circle, classic, default, heavyround, lightround, sieve : ") 

print("\n---------------------------\nChoose a style for the INNER EYE from the options below \n---------------------------\n")

inner_eye_qr = input("circle, cushion, default, diamond, dots, heavyround, leaf, left_eye, right_eye, shield, sieve, star : ")

print("\n---------------------------\nChoose a style for the OUTER EYE from the options below \n---------------------------\n")

outer_eye_qr = input("circle, cushion, default, diamond, dots, heavyround, leaf, left_eye, right_eye, shield, sieve, star : ")


qr_one = qrlib.generate_qr_file(text, qr_format='SVG', style=qr_style, inner_eye_style=inner_eye_qr,
                 outer_eye_style=outer_eye_qr)


topng(qr_one.getvalue())
image = Image.open('output.png')
image.show()

print("\n--------------------\nLook we added logo for you!\n--------------------\n")

insert_logo(100)

print("\n--------------------\nAnd now with a gradient!\n--------------------\n")

make_qr_transparent()
add_gradient()
