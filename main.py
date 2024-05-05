import tkinter
from tkinter import *
from tkinter import filedialog
import os

def main():
    filename = filedialog.askdirectory()
    print(filename)
    path = str(filename)
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)
    for i in range(len(dir_list)):
        new_name = dir_list[i].replace('[SPOTIFY-DOWNLOADER.COM] ','')
        print(dir_list[i])
        os.chdir(fr"{path}")
        os.system(f'rename "{dir_list[i]}" "{new_name}"')
        print(f'rename "{dir_list[i]}" "{new_name}"')
        print(f"renamed to {new_name}")


root = Tk()
folder_path = StringVar()
lbl = Label(text="Tool for deleting prefix on \nhttps://spotify-downloader.com/")
lbl.place(relx=0.5,rely=0.5,anchor=tkinter.S)
button2 = Button(text="Browse", command=main)
button2.place(relx=0.5,rely=0.5,anchor=tkinter.N)



root.mainloop()

