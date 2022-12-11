from serial import Serial
from tkinter import ttk
from tkinter import *

arduino = Serial(port='COM10', baudrate=115200 )
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

while True:
  data = arduino.readline()
  ttk.Label(frm, text=str(data)).grid(column=0, row=0)
  root.update()

  