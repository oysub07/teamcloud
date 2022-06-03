import random
from tkinter import *


database = {"email": "password"}

root = Tk()  # main 설정
root.title("log in to team10")  # 위에 뜨는 거
root.geometry("400x400+100+100")  # 넓이 설정
root.resizable(False, False)  # 크기 조정 가능한지 x축, y축

MAX_LENGTH = 6

title = Label(root, text="Log In", font='Helvetica 15 bold')
# root는 위치 할 곳, text는 표시할 문자,font는 설정
title.pack(pady='10')
# pack은 가운데에 위치 시키는 거고, pady는 padding y축 (y축으로 위아래 10씩!)

mainFrame = Frame(root)
# Frame은 contents가 들어갈 곳! root에 위치시켜도 되는데
mainFrame.pack()

# email을 저장할 frame(emailFrame)을 main frame에 위치 시킴
emailFrame = Frame(mainFrame)
emailFrame.pack()
lblEmail = Label(emailFrame, text="email", width='8', anchor="w")  # 넓이 8, anchor='w'해서 왼쪽 정렬
lblEmail.grid(row=1, column=0)  # grid는 격자로 해서 위치 지정!
email = Entry(emailFrame)
email.grid(row=1, column=1)

# password을 저장할 frame(emailFrame)을 main frame에 위치 시킴
passwordFrame = Frame(mainFrame)
passwordFrame.pack()
lblPassword = Label(passwordFrame, text="password", width='8', anchor="w")
lblPassword.grid(row=1, column=0)
password = Entry(passwordFrame)
password.grid(row=1, column=1)

global captchaNumber

captchaFrame = Frame(mainFrame)
captchaFrame.pack(pady=(10, 20))

captcha = Entry(captchaFrame)
captcha.grid(row=2, column=0)


def regen():
    global captchaNumber
    n = str(random.randrange(0, 10 ** MAX_LENGTH))
    captchaNumber = '0' * (MAX_LENGTH - len(n)) + n
    imgCaptcha = Label(captchaFrame, text=captchaNumber, width='8', anchor="w")
    imgCaptcha.grid(row=1, column=0)
    print(captchaNumber)


regen()

regenBtn = Button(captchaFrame, text="regen", width='5', command=regen, repeatdelay=1)
regenBtn.grid(row=1, column=1)

emails = database.keys()
passwords = database.values()
count = 0


def login():
    global count
    k = email.get()
    t = password.get()
    g = captcha.get()

    if (k in emails) and (t in passwords) and (g == captchaNumber):
        new = Tk()
        new.title("successful login")
        new.geometry("400x400+100+100")
        new.resizable(False, False)
        welcome = Label(new, text="Welcome!!", width=20, height=50)
        welcome.pack()
        new.mainloop()
    else:
        count += 1
        notice2.config(text=str(count) + "회 실패하셨습니다")


notice2 = Label(root)

notice2.pack()

loginbuttonFrame = Frame(mainFrame)
loginbuttonFrame.pack(pady=(10, 20))
loginbutton = Button(loginbuttonFrame, overrelief="solid", width=20, command=login, repeatdelay=1000,
                     repeatinterval=100, text="로그인")
loginbutton.grid(row=1, column=1)

root.mainloop()

