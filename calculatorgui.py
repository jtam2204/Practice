import tkinter  as tk
from tkinter import ttk

inputarr=[]

def addnumber(num):
    inputarr.append(num)
    tempstr=''.join(inputarr)
    inputstr.set(tempstr)

def delnumber():
    inputarr.pop()
    tempstr=''.join(inputarr)
    inputstr.set(tempstr)

def clearnumber():
    inputarr.clear()
    tempstr=''.join(inputarr)
    inputstr.set(tempstr)

def calculation():
    startptr=0
    numarr=[]
    oprarr=[]
    for i in range(len(inputarr)):
        if inputarr[i] not in ['+', '-', '*', '/']:
            if i==len(inputarr)-1:
                temp=''.join(inputarr[startptr:i+1])
                numarr.append(temp)     
        else:
            temp=''.join(inputarr[startptr:i])
            numarr.append(temp)
            oprarr.append(inputarr[i])
            startptr=i+1
    if len(numarr)<=len(oprarr):
        answerstr.set('Error')
        return 0
    else:
        answerstr.set('')
        # calculation
        i=0
        while i< len(oprarr):
            while oprarr[i] not in ['+', '-'] and len(oprarr) >0:
                if oprarr[i] == '*':
                    numarr[i] =str(float(numarr[i])*float(numarr[i+1]))
                else:
                    numarr[i] =str(float(numarr[i])/float(numarr[i+1]))
                del numarr[i+1]
                del oprarr[i]
                if len(oprarr) <=i:
                    break
            i+=1
            #print(','.join(numarr))
            #print(','.join(oprarr))
        #print('+ and - phase')
        i=1
        while i < len(numarr):
            if oprarr[i-1] == '+':
                numarr[0]= str(float(numarr[i-1])+ float(numarr[i]))
            else:
                numarr[0]= str(float(numarr[i-1])- float(numarr[i]))
            del numarr[i]
            del oprarr[i-1]
            #print(','.join(numarr))
            #print(','.join(oprarr))
        if len(numarr) ==1:
            inputstr.set(str(numarr[0]))     

root = tk.Tk()
root.title('Calculator')
root.geometry('500x400')

s=ttk.Style()
s.configure('number.TButton', width=3, height=3, font =('Calibri', 20))

input_frame=ttk.Frame(root)

inputstr=tk.StringVar(value='0')
input_entry = ttk.Entry(input_frame, justify= 'center', textvariable= inputstr, width=16, font=('Calibri', 20))
input_entry.pack(pady=10)

row1=ttk.Frame(input_frame)
button1=ttk.Button(row1, text='1', style= 'number.TButton', command= lambda: addnumber('1'))
button2=ttk.Button(row1, text='2', style= 'number.TButton', command= lambda: addnumber('2'))
button3=ttk.Button(row1, text='3', style= 'number.TButton', command= lambda: addnumber('3'))
buttonplus=ttk.Button(row1, text='+', style= 'number.TButton', command= lambda: addnumber('+'))
button1.pack(side= 'left', padx=2)
button2.pack(side= 'left', padx=2)
button3.pack(side= 'left', padx=2)
buttonplus.pack(side= 'left', padx=2)
row1.pack(pady=2)

row2=ttk.Frame(input_frame)
button4=ttk.Button(row2, text='4', style= 'number.TButton', command= lambda: addnumber('4'))
button5=ttk.Button(row2, text='5', style= 'number.TButton', command= lambda: addnumber('5'))
button6=ttk.Button(row2, text='6', style= 'number.TButton', command= lambda: addnumber('6'))
buttonminus=ttk.Button(row2, text='-', style= 'number.TButton', command= lambda: addnumber('-'))
button4.pack(side= 'left', padx=2)
button5.pack(side= 'left', padx=2)
button6.pack(side= 'left', padx=2)
buttonminus.pack(side= 'left', padx=2)
row2.pack(pady=2)

row3=ttk.Frame(input_frame)
button7=ttk.Button(row3, text='7', style= 'number.TButton', command= lambda: addnumber('7'))
button8=ttk.Button(row3, text='8', style= 'number.TButton', command= lambda: addnumber('8'))
button9=ttk.Button(row3, text='9', style= 'number.TButton', command= lambda: addnumber('9'))
buttontimes=ttk.Button(row3, text='*', style= 'number.TButton', command= lambda: addnumber('*'))
button7.pack(side= 'left', padx=2)
button8.pack(side= 'left', padx=2)
button9.pack(side= 'left', padx=2)
buttontimes.pack(side= 'left', padx=2)
row3.pack(pady=2)

row4 =ttk.Frame(input_frame)
clearbutt=ttk.Button(row4, text= 'C', style= 'number.TButton', command= clearnumber)
button0=ttk.Button(row4	, text= '0', style= 'number.TButton', command= lambda: addnumber('0'))
delbutt=ttk.Button(row4 , text= 'DEL', style= 'number.TButton', command= delnumber)
buttondivide=ttk.Button(row4, text='/', style= 'number.TButton', command= lambda: addnumber('/'))
clearbutt.pack(side= 'left', padx=2)
button0.pack(side= 'left', padx=2)
delbutt.pack(side= 'left', padx=2)
buttondivide.pack(side= 'left', padx=2)
row4.pack(pady=2)

row5= ttk.Frame(input_frame)
buttonequal = ttk.Button(row5, text= '=', style='number.TButton', width= 11, command= calculation)
buttondot=ttk.Button(row5, text='.', style= 'number.TButton', command= lambda: addnumber('.'))
buttonequal.pack(padx=2, side='left')
buttondot.pack(padx=2, side='left')
row5.pack(pady=2)

answerstr=tk.StringVar()
answer_label = ttk.Label(input_frame, textvariable= answerstr, font=('', 20))
answer_label.pack(pady=2)

input_frame.pack(padx=5, side='left')

def paint(event, colours, sizes = 4):
    x,y=event.x, event.y
    x1, y1, x2, y2 = ( event.x - 2 ),( event.y - 2 ), ( event.x + 2 ),( event.y + 2 ) 
    draftppr.create_oval(x1, y1, x2, y2, fill=colours, outline= colours)
    #draftppr.create_oval(x2, y1, x1, y2, fill=colours, width=sizes)
    #draftppr.create_oval(x2, y, x1, y, fill=colours, width=sizes)
    #draftppr.create_oval(x, y1, x, y2, fill=colours, width=sizes)

draft_frame =ttk.Frame(root)
draft_label =ttk.Label(draft_frame, text='Left click to draw, right click to erase\nDouble right click to clear canvas')
draftppr =tk.Canvas(draft_frame, bg='white', width= 250, height=380, bd=1)
draftppr.bind('<B1-Motion>', lambda event: paint(event, 'black'))
draftppr.bind('<B3-Motion>', lambda event: paint(event, 'white', 5))
draftppr.bind('<Double-Button-3>', lambda event: draftppr.delete('all'))
draft_label.pack()
draftppr.pack()
draft_frame.pack(side= 'right')

root.mainloop()