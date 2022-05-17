from tkinter import *
import tkinter.messagebox as msgbox
import random
import string

root = Tk()
root.title("CLOUD") #창 이름
root.geometry("540x360+200+100") #윈도우/창이 나타나는 위치를 지정

title = Label(root, text = "CLOUD 회원가입", font = ("맑은 고딕", '25','bold'))
#title.grid(row = 1, column = 1)
title.pack()

mainFrame = Frame(root)
mainFrame.pack()

#이름
nameframe = Frame(mainFrame)
nameframe.pack()
labelname = Label(nameframe, text = "이름", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelname.grid(row = 1, column=0)
name = Entry(nameframe)
name.grid(row = 1, column = 1)

#성별
sexframe = Frame(mainFrame)
sexframe.pack()
labelsex = Label(sexframe, text = "성별", width = 16, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelsex.grid(row = 1, column=0)

sex = IntVar()
male = Radiobutton(sexframe, text = "남성", anchor = "e", variable = sex, value = 1) #남성은 1
female = Radiobutton(sexframe, text = "여성", anchor = "e", variable = sex, value = 2) #여성은 2
#male.pack()
#female.pack()
male.grid(row=1, column=1)
female.grid(row=1, column=2)

#lb = Label(sexframe,text = "성별은 : None", fg = "red")


#이메일
emailframe = Frame(mainFrame)
emailframe.pack()
labelemail = Label(emailframe, text = "e-mail", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelemail.grid(row = 1, column=0)
email = Entry(emailframe)
email.grid(row = 1, column = 1)

#패스워드
pwframe = Frame(mainFrame)
pwframe.pack()
labelpw = Label(pwframe, text = "password", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelpw.grid(row = 1, column=0)
pw = Entry(pwframe, show = '*')
pw.grid(row = 1, column = 1)

root.mainloop()