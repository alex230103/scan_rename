import pytesseract
from pyzbar.pyzbar import decode
import os
import shutil
from pdf2image import convert_from_path
from ocr import get_img

config = r'--oem 3 --psm 6'


def move_ttn(file_name, name):
    shutil.move("pdf/" + file_name, "ttn/" + name + ".pdf")


def get_name_from_qr_code(images, file_name):

    data = decode(images[0])
    if data:
        name = data[0].data.decode('utf-8')
        print(name + " успешно распознан. ")
        move_ttn(file_name, name)
        return True
    else:
        return False


def get_file():
    files_path = os.listdir('pdf/')

    for file_name in files_path:

        images = convert_from_path("pdf/" + file_name, 300)
        ttn_qr = get_name_from_qr_code(images, file_name)

        if not ttn_qr:
            images[0].save("img.jpg")
            img = get_img("img.jpg")

            text = pytesseract.image_to_string(image=img, config=config)
            
            number = text.find("390-")
            if number > -1:
                name = str(text[number: number+10]).replace('\n', '')
                print(name + " успешно распознан. ")
                move_ttn(file_name, name)
            else:
                print(str(file_name) + " не распознан.")
                shutil.move("pdf/" + file_name, "bad/" + file_name)


if __name__ == "__main__":
    get_file()
