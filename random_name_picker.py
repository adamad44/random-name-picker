import random
import tkinter
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('random name picker')
root.geometry('650x700')
root.minsize(650,700)
root.maxsize(700,750)
root.config(bg='#212121')

def generate():

    content = entry_box.get("1.0","end")
    nearly_final_content = (content.split('\n'))
    del nearly_final_content[-1]
    global random_number
    random_number = random.choice(nearly_final_content)
    global a
    a = False
    if random_number == '' or ' ':
        a = True









def main():
    try:
        number_widget.config(font='Helvetica 16')
        generate()
        if a == True:
            generate()
        length = len(entry_box.get('1.0','end'))
        if length <20:
            number_widget.config(font='Helvetica 40')
        elif length <30:
            number_widget.config(font='Helvetica 30')
        elif length <20:
            number_widget.config(font='Helvetica 20')
        number_widget.config(text=(str(random_number)))
        number_widget.pack_forget()
        root.update()
        number_widget.pack(fill=tk.BOTH, expand=True)
        root.update()
        delete_button.pack()
        root.update()
        for i in nearly_final_content:

            if i == random_number:
                nearly_final_content.remove(i)
                root.update()
                entry_box.delete('1.0', END)
                entry_box.insert('1.0', content.replace(' ' , '\n'))
    except:
        pass



title = Label(root, text='Random name picker', font='Helvetica 30 bold', pady=20,bg='#212121', fg='white')
title.pack()


button = Button(root, text='choose', command=main, pady=20, padx=20, bg = '#5910ad',activebackground='#6313bf',activeforeground='white',borderwidth=0,
                font='Helvetica 15 bold',fg='white')



number_widget = Label(root, font ='verdena 20', text='' ,bg='#212121',fg='white')
entry_box = Text(root,width=40,height=17, bg='#292929',fg='white', font='Helvetica 16')

entry_box.pack()
button.pack()







root.mainloop()
