import tkinter as tk
from tkinter import ttk

def convertmile():
    temp = mile_float.get()*1.61
    km_float.set(temp) 

def convertkm():
    temp = km_float.get()/1.61
    mile_float.set(temp) 

window =tk.Tk()
window.title('Converter')
window.geometry('600x300')

s=ttk.Style()
s.configure('my.TButton', font=('Calibri', 16))

title_label =ttk.Label(master= window, text= 'Distance converter', font='Calibri 20 bold')
title_label.pack(pady= 10)

input_frame1= ttk.Frame(master=window)
input_frame2= ttk.Frame(master=window)
mile_float =tk.DoubleVar()
km_float =tk.DoubleVar()

mile_frame =ttk.Entry(master=input_frame1, textvariable = mile_float,  font='Calibri 16', width=15)
mile_label =ttk.Label(master= input_frame1, text = 'Mile(s)',  font='Calibri 16')
milebutt =ttk.Button(master= input_frame1, text= 'Convert Mile', command= convertmile, style= 'my.TButton')

mile_frame.pack(side='left', padx= 1)
mile_label.pack(side='left', padx= 1)
milebutt.pack(side='left', padx= 1)

kmbutt =ttk.Button(master= input_frame2, text= 'Convert Km', command= convertkm, style= 'my.TButton')
km_frame =ttk.Entry(master=input_frame2, textvariable = km_float,  font='Calibri 16', width=15)
km_label =ttk.Label(master= input_frame2, text = 'Km',   font='Calibri 16')

km_frame.pack(side='left', padx= 1)
km_label.pack(side='left', padx= 1)
kmbutt.pack(side='left', padx= 1)

input_frame1.pack(pady= 5)
input_frame2.pack(pady= 5)

window.mainloop()
