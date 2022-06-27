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

    sozluk = {
        25 : [147, 200], 41 : [271, 200], 62 : [397, 200], 11 : [83, 280], 33 : [209, 280], 52 : [335, 280],
        77 : [459, 280], 82 : [521, 280], 8 : [21, 355], 28 : [147, 355], 47 : [272, 355], 67 : [398, 355],
        89 : [521, 355], 1 : [17, 527], 20 : [143, 527], 40 : [269, 527], 64 : [395, 527], 71 : [460, 527],
        10 : [79, 605], 30 : [206, 605], 56 : [332, 605], 79 : [458, 605], 88 : [521, 605], 2 : [521, 605],
        23 : [142, 680], 46 : [268, 680], 68 : [395, 680], 87 : [520, 680], 4 : [20, 200]
    }


    for i in sozluk:
        if cikan_sayi == i:
            puldeneme = Label(window, image=pul, bg='white')
            puldeneme.place(x=int(sozluk[i][0]), y=int(sozluk[i][1]))


Button(window, text="Sayi Cek!", font=('Times 15 bold'), command=clicked_button).place(x=240, y=90)


window.mainloop()
