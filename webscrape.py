import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
    
targetclass = 'text'
rs= requests.Session()
class_set = set()
class_list=[]

def showclasslist():
    class_set = set()
    if urlinput.get()!= '':
        targeturl = urlinput.get()
    response= rs.get(targeturl)
    if response.ok:
        print('Success') 
        #print(response.text)
        soup = BeautifulSoup(response.content, 'html.parser')

        tags = {tag.name for tag in soup.find_all()}   
        for tag in tags:  
            for i in soup.find_all( tag ):  
                if i.has_attr( "class" ): 
                    if len( i['class'] ) != 0: 
                        class_set.add(" ".join( i['class'])) 
        class_list = list(class_set)
        classcombo['values'] = class_list

def searchbyclass():
    targeturl = urlinput.get()
    response= rs.get(targeturl)
    soup = BeautifulSoup(response.content, 'html.parser')
    targetclass = classcombo.get()
    s = soup.find('div', class_= targetclass)
    if s!= None:
        lines = s.find_all('p')
        output_text.set(lines)

def classrefresh(event):
    classcombo['values'] = class_list

window = tk.Tk()
window.title('Web Scraper')
window.geometry('800x700')

urlinput_frame = ttk.Frame(window)
urlinput = tk.StringVar(value= 'https://www.geeksforgeeks.org/python-programming-language/')
urlinput_entry=ttk.Entry(urlinput_frame, textvariable= urlinput, width=80)
urlinput_entry.pack(side='left', padx= 5)
urlbutton =ttk.Button(urlinput_frame, text = 'Confirm', command= showclasslist)
urlbutton.pack(side='left', padx= 5)
urlinput_frame.pack(pady=10)

classinput_frame =ttk.Frame(window)
classstr= tk.StringVar(value='')
classcombo=ttk.Combobox(classinput_frame, textvariable=classstr)
classcombo.bind('<FocusIn>', lambda event:classrefresh(event))
classcombo.pack(side='left', padx= 5)
classbutton = ttk.Button(classinput_frame, text = 'Confirm', command= searchbyclass)
classbutton.pack(side='left', padx= 5)
classinput_frame.pack(pady=10)

output_frame=ttk.Frame(master= window, border= '2', borderwidth='5')
output_text=tk.StringVar(value='')
output_label =ttk.Label(master=output_frame, textvariable= output_text, wraplength= 650)
output_label.pack(padx=10, pady=5)
output_frame.pack(padx=10, pady=5)

window.mainloop()
#showclasslist()
#searchbyclass()