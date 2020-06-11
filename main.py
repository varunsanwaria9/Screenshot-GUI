import tkinter
import pyautogui as pg
from random import randint
import time

root = tkinter.Tk()

def sshots():
    name = randint(1,1000)
    ss = pg.screenshot()
    ss.save(f"Screenshots\\{name}.png")
    
def fu():
    root.geometry("200x30")
    root.title("Screenshot")
    capt = tkinter.Button(root,text="CAPTURE",command=sshots)
    capt.pack()
    root.mainloop()

fu()