from glob import glob
from tkinter import *
import tkinter.messagebox as msgbox
import random
import string
from captcha.image import ImageCaptcha
import sys

root = Tk()

title = Label(root, text = "CLOUD 회원가입", font = ("맑은 고딕", '25','bold'))
root.geometry("540x360+200+100") #윈도우/창이 나타나는 위치를 지정
title.pack()

mainFrame = Frame(root)
mainFrame.pack()

sexframe = Frame(mainFrame)
sexframe.pack()
labelsex = Label(sexframe, text = "성별", width = 16, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelsex.grid(row = 1, column=0)

sex = IntVar()
male = Radiobutton(sexframe, text = "남성", anchor = "e", variable = sex, value = 1)
female = Radiobutton(sexframe, text = "여성", anchor = "e", variable = sex, value = 2)
male.grid(row=1, column=1)
female.grid(row=1, column=2)

nameframe = Frame(mainFrame)
nameframe.pack()
labelname = Label(nameframe, text = "이름", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelname.grid(row = 1, column=0)
name = Entry(nameframe)
name.grid(row = 1, column = 1)

emailframe = Frame(mainFrame)
emailframe.pack()
labelemail = Label(emailframe, text = "e-mail", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelemail.grid(row = 1, column=0)
email = Entry(emailframe)
email.grid(row = 1, column = 1)
email_str = email.get()

#이메일 형식 판독 함수
def is_email_valid(email_str):
    #이메일 형식이 알맞지 않은 경우
    if email_str.rfind("@") == -1 or email_str.rfind(".") == -1:
        return FALSE
    #이메일 형식이 알맞은 경우
    else:
       return TRUE
            

pwframe = Frame(mainFrame)
pwframe.pack()
labelpw = Label(pwframe, text = "password", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelpw.grid(row = 1, column=0)
pw = Entry(pwframe, show = '*')
pw.grid(row = 1, column = 1)

def print_random():
    _LENGTH_=6
    string_pool = string.ascii_uppercase + string.digits

    result = ""
    for i in range(_LENGTH_):
        result += random.choice(string_pool)
    global tmp_str
    tmp_str = result
    print(tmp_str)
    return result


#보안문자
randomframe = Frame(mainFrame)

#새로고침
def refresh_btncmd():
    global randomframe
    randomframe.pack()

    image = ImageCaptcha(width=160, height=90)
    txt_captcha = print_random()
    image.generate(txt_captcha)
    image.write(txt_captcha, 'captcha_result.png')
    photo = PhotoImage(file='captcha_result.png')

    labelrandom = Label(randomframe, image=photo)
    labelrandom.grid(row = 1, column=0)
    global rand
    rand = Entry(randomframe, width = 15, font = 8)
    rand.place(x = 40, y = 20)
    rand.grid(row = 2)
refresh_btncmd()

ref_btn = Button(randomframe, text = "새로고침", anchor = "e", command = refresh_btncmd)
ref_btn.grid(row = 1, column = 1)


#등록 버튼 기능
def signin_btncmd():
    #입력되지 않은 정보가 있는 경우
    if name.get() == "" or email.get() == "" or pw.get() == "" or (sex.get() != 1 and sex.get() != 2) :
        print(name.get())
        print(email.get())
        print(pw.get())
        print(sex.get())
        msgbox.showwarning("오류", "입력되지 않은 정보가 있습니다. 다시 확인하세요.")
    
    else:
        #이메일 형식이 알맞지 않은 경우
        if is_email_valid(email.get()) == FALSE:
            msgbox.showwarning("오류", "이메일 형식이 알맞지 않습니다. 형식을 다시 확인하세요.")
        #이메일 형식이 알맞은 경우
        else:
            if tmp_str == rand.get().upper() : 
                msgbox.showinfo("완료", "회원가입이 완료되었습니다")
                root.destroy() #창 닫기
                
            #보안문자가 일치하지 않는 경우
            else:
                msgbox.showwarning("오류", "보안문자가 일치하지 않습니다. 다시 입력하세요.")
            

#등록 버튼
signin_btn = Button(root, text = "등록", anchor = CENTER, command=signin_btncmd, width = 10, height = 2)
signin_btn.pack()



root.mainloop()
