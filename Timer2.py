from tkinter import *
import os
import time

root = Tk()
root.title("Sleep timer")
root.resizable(False, False)
root.geometry('500x300')



def timeroff(event):
    print(event)
    print("Таймер выключен")
    os.system("shutdown -a")


def settimer():
    global en1

    print("Таймер поставлен")
    en1 = int(en1.get()) * 60
    global otchet

    os.system("shutdown -s -t {0}".format(str(en1)))








but = Button(root,text="Стар",font="Tahoma 20",bg="#105206",command=settimer,bd=0.5)
but.place(relx=0.2, rely=0.8, anchor='n', width=90,height=60)

en1 = Entry(root, font="Tahoma 20")
en1.place(relx=0.61, rely=0.05, anchor='n', width=65)
min_1 = Label(root,text="(мин)",font="Tahoma 20",bg="grey22")
min_1.place(relx=0.75, rely=0.047, anchor='n',)

root["bg"] = "gray22"

labelt = Label(text="Впишите время :", font="Tahoma 20",bg="grey22")
labelt.place(relx=0.32, rely=0.047, anchor='n')

button = Button(root, text="Остановить таймер", font="Tahoma 20",bd=0.5, bg="#630707", command=lambda: timeroff(event=1))
button.place(relx=0.6, rely=0.8, anchor='n',height=60)

#otchet = Label(root, text="Ostalos vremeni", font="Tahoma 20")
#otchet.place(relx=0.5, rely=0.5, anchor='n')

root.mainloop()