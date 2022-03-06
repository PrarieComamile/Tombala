import random
import tkinter
from tkinter import *

window = Tk()

window.title("Tombala")
window.geometry("600x800")


pul = tkinter.PhotoImage(file="pul.png")
kart1_img = tkinter.PhotoImage(file="kart1.png")
kart2_img = tkinter.PhotoImage(file="kart2.png")

labelkart2 = Label(window, image=kart2_img)
labelkart2.place(x=2, y=500)

labelkart1 = Label(window, image=kart1_img)
labelkart1.place(x=2, y=180)

oyuncu1_yazi = Label(window, text="1.Oyuncu", font="Times 19 bold")
oyuncu1_yazi.place(x=10, y=150)

oyuncu2_yazi = Label(window, text="2.Oyuncu", font="Times 19 bold")
oyuncu2_yazi.place(x=10, y=470)

img = tkinter.PhotoImage(file="torba.png")
label = Label(window, image=img)
label.place(x=260, y=20)

def clicked_button():
    cikan_sayi = random.randint(1, 90)

    yazi = Label(text=cikan_sayi, fg="Black", bg="#8D7A29", font='16')
    yazi.place(x=283, y=50)

    if str(cikan_sayi) == '4':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=20, y=200)

    if str(cikan_sayi) == '25':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=147, y=200)

    if str(cikan_sayi) == '41':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=271, y=200)

    if str(cikan_sayi) == '62':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=397, y=200)

    if str(cikan_sayi) == '11':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=83, y=280)

    if str(cikan_sayi) == '33':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=209, y=280)

    if str(cikan_sayi) == '52':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=335, y=280)

    if str(cikan_sayi) == '77':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=459, y=280)

    if str(cikan_sayi) == '82':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=521, y=280)

    if str(cikan_sayi) == '8':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=21, y=355)

    if str(cikan_sayi) == '28':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=147, y=355)

    if str(cikan_sayi) == '47':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=272, y=355)

    if str(cikan_sayi) == '67':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=398, y=355)

    if str(cikan_sayi) == '89':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=521, y=355)

    if str(cikan_sayi) == '1':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=17, y=527)

    if str(cikan_sayi) == '20':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=143, y=527)

    if str(cikan_sayi) == '40':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=269, y=527)

    if str(cikan_sayi) == '64':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=395, y=527)

    if str(cikan_sayi) == '71':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=460, y=527)

    if str(cikan_sayi) == '10':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=79, y=605)

    if str(cikan_sayi) == '30':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=206, y=605)

    if str(cikan_sayi) == '56':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=332, y=605)

    if str(cikan_sayi) == '79':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=458, y=605)

    if str(cikan_sayi) == '88':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=521, y=605)

    if str(cikan_sayi) == '2':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=16, y=680)

    if str(cikan_sayi) == '23':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=142, y=680)

    if str(cikan_sayi) == '46':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=268, y=680)

    if str(cikan_sayi) == '68':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=395, y=680)

    if str(cikan_sayi) == '87':
        puldeneme = Label(window, image=pul, bg='white')
        puldeneme.place(x=520, y=680)


Button(window, text="Sayi Cek!", font=('Times 15 bold'), command=clicked_button).place(x=240, y=90)


window.mainloop()

#tombala kagıdını resim olarak koyup cikan sayıları konum ile yerlestir
