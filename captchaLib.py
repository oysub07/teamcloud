from captcha.image import ImageCaptcha
import string
import random
from tkinter import *


def print_random():
    _LENGTH_ = 6
    string_pool = string.ascii_uppercase + string.digits

    result = ""
    for i in range(_LENGTH_):
        result += random.choice(string_pool)
    global tmp_str
    tmp_str = result
    print(tmp_str)
    return result


def refresh():
    image = ImageCaptcha(width=160, height=90)
    txt_captcha = print_random()
    image.generate(txt_captcha)
    image.write(txt_captcha, 'captcha_result.png')
    photo = PhotoImage(file='captcha_result.png')
    return txt_captcha, photo
