import random
from tkinter import *
from tkinter import messagebox

database = {"email": "password"}

root = Tk()  # main 설정
root.title("sign in to team10")  # 위에 뜨는 거
root.geometry("400x400+100+100")  # 넓이 설정
root.resizable(False, False)  # 크기 조정 가능한지 x축, y축

MAX_LENGTH = 6

title = Label(root, text="Sign In", font='Helvetica 15 bold')
# root는 위치 할 곳, text는 표시할 문자,font는 설정
title.pack(pady='10')
# pack은 가운데에 위치 시키는 거고, pady는 padding y축 (y축으로 위아래 10씩!)

mainFrame = Frame(root)
# Frame은 contents가 들어갈 곳! root에 위치시켜도 되는데
mainFrame.pack()

# email을 저장할 frame(emailFrame)을 main frame에 위치 시킴
emailFrame = Frame(mainFrame)


count=0
def countUP():
    global count
    count +=1
    label.config(text=str(count))

label = Label(root, text="0")
label.pack()

button = Button(root, overrelief="solid", width=15, command=countUP
                , repeatdelay=1000, repeatinterval=100, text="test")

button.flash()
button.pack()


