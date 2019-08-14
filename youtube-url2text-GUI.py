#!/usr/local/bin/python3

from tkinter import filedialog
from tkinter import *
from external_solution_timedtext import get_timedtext

def save_file():
    youtube_url = entry.get()
    # do some error checking if it is correct youtube url
    timed_text = get_timedtext(youtube_url)

    fout =  filedialog.asksaveasfile(mode='w', defaultextension=".txt")

    fout.write(timed_text)

    print(fout)






root = Tk()

button = Button(root, text='summit and save as' , command=save_file)
button.pack(side= RIGHT)
entry = Entry(root, bd =5)
entry.pack(side = LEFT)

root.mainloop()
