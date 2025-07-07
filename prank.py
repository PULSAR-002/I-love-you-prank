import pyautogui as pg
import time as t
import tkinter as tk

def on_yes():
    root.destroy()

def on_no():
    root.destroy()
    main()

def main():
    global root
    root = tk.Tk()
    root.title("<3")
    root.geometry("300x300")


    l1=tk.Label(root,text="Do you love me?").pack()
    root.protocol('WM_DELETE_WINDOW',on_no)
    btn1 = tk.Button(root, text="yes", command=on_yes).pack()
    btn2 = tk.Button(root, text="NO", command=on_no).pack()




    root.mainloop()


main()