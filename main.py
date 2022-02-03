import getpass
import pyperclip
from PIL import ImageGrab
import random, string
import keyboard
import os
import pyimgur
import time
name = getpass.getuser()
spam = '​||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
clientid = 'your id here' # https://apidocs.imgur.com/
clientsecret = 'your secret here' # https://apidocs.imgur.com/
letters = string.ascii_lowercase
images = ImageGrab.grabclipboard()
im = pyimgur.Imgur(clientid)
def delete(filename):
    try:
        os.remove(f"{filename}")
    except: 
        pass
while True:
    try:
        im = pyimgur.Imgur(clientid)
        keyboard.wait("F7")
        filename = ''.join(random.choice(letters) for i in range(25))
        filepath = f'C:\\Users\\{name}\\AppData\\Local\\Temp\\{filename}.png'
        images.save(f'{filepath}','PNG')
        time.sleep(0.22)
        uploadedimage = im.upload_image(filepath, title="bruh.png")
        pyperclip.copy(f'<https://anywebsite.anything/>{spam}{uploadedimage.link}')
        delete(filename)
    except:
        pass

