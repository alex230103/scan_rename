from PIL import Image
from pyzbar.pyzbar import decode
import os
import shutil

img_dir = 'img/'
good_dir = 'good/'
bad_dir = 'bad/'



def list_dir ():
    files_path = os.listdir(img_dir)

    for file_name in files_path:
        img= Image.open(img_dir + file_name)
        data = decode(img)

        if data:
            name = data[0].data.decode('utf-8').replace("mx1_", "")

            print(name + " успешно распознан. ")
            shutil.move(img_dir + file_name, good_dir + name + ".jpg")
            print("Success")
        else:
            print ("Error read img")
            shutil.move(img_dir + file_name, bad_dir + file_name + ".jpg")

    
if __name__ == "__main__":
    list_dir()
