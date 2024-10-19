import tkinter  as tk
from tkinter import ttk

phonebook = [
    {"name": "Alice Johnson", "phone": "555-1234", "email": "alice.johnson@example.com"},
    {"name": "Bob Smith", "phone": "555-5678", "email": "bob.smith@example.com"},
    {"name": "Charlie Brown", "phone": "555-9101", "email": "charlie.brown@example.com"},
    {"name": "Diana Prince", "phone": "555-1122", "email": "diana.prince@example.com"},
    {"name": "Edward Norton", "phone": "555-3344", "email": "edward.norton@example.com"},
    {"name": "Fiona Gallagher", "phone": "555-5566", "email": "fiona.gallagher@example.com"},
    {"name": "George Harrison", "phone": "555-7788", "email": "george.harrison@example.com"},
    {"name": "Hannah White", "phone": "555-9900", "email": "hannah.white@example.com"},
    {"name": "Ian Curtis", "phone": "555-2233", "email": "ian.curtis@example.com"},
    {"name": "Julia Roberts", "phone": "555-4455", "email": "julia.roberts@example.com"}
]


root=tk.Tk()
root.geometry('600x450')
root.title('Address book')

s=ttk.Style()
s.configure('TButton', font=('', 12))

startpage= tk.Frame(root)
startlabel=ttk.Label(startpage, text='Address Book')
startlabel.pack(pady= 5)

table1= ttk.Treeview(startpage, columns=('name', 'phone', 'email'), show='headings', height= 10)
table1.heading('name', text= 'Name')
table1.column('name', minwidth=0, width= 130, stretch= False)
table1.heading('phone', text= 'Phone number')
table1.column('phone', minwidth=0, width= 120, stretch= False)
table1.heading('email', text= 'Email address')
table1.column('email', minwidth=0, width= 200, stretch= False)
table1.pack(fill='both', expand= True, padx= 10)

input_frame= ttk.Frame(startpage)

name_str=tk.StringVar()
row1=ttk.Frame(input_frame)
name_label=ttk.Label(row1, text='Name:  ', font=('',12))
name_entry=ttk.Entry(row1, textvariable= name_str, font=('',12), width= 30)
name_label.pack(padx=2, side='left')
name_entry.pack(padx=2, side='left')
row1.pack(pady=5)

phone_str=tk.StringVar()
row2=ttk.Frame(input_frame)
phone_label=ttk.Label(row2, text='Phone: ', font=('',12))
phone_entry=ttk.Entry(row2, textvariable= phone_str, font=('',12), width= 30)
phone_label.pack(padx=2, side='left')
phone_entry.pack(padx=2, side='left')
row2.pack(pady=5)

email_str=tk.StringVar()
row3=ttk.Frame(input_frame)
email_label=ttk.Label(row3, text='Email:  ', font=('',12))
email_entry=ttk.Entry(row3, textvariable= email_str, font=('',12), width= 30)
email_label.pack(padx=2, side='left')
email_entry.pack(padx=2, side='left')
row3.pack(pady=5)

def item_insert():
    if name_str.get()!='':
        data =(name_str.get(), phone_str.get(), email_str.get())
        table1.insert(parent='', index=tk.END, values= data)
        name_str.set('')
        phone_str.set('')
        email_str.set('')

def item_edit():
    if name_str.get()!='':
        data =(name_str.get(), phone_str.get(), email_str.get())
        table1.item(table1.selection(), values= data)
        name_str.set('')
        phone_str.set('')
        email_str.set('')

def item_clear():
    name_str.set('')
    phone_str.set('')
    email_str.set('')

row4 = ttk.Frame(input_frame)
input_button=ttk.Button(row4, text='Insert', style= 'TButton',  command= item_insert)
input_button.pack(padx=5, side= 'left')
edit_button=ttk.Button(row4, text='Edit', style= 'TButton',  command= item_edit)
edit_button.pack(padx=5, side= 'left')
clear_button=ttk.Button(row4, text='Clear', style= 'TButton',  command= item_clear)
clear_button.pack(padx=5, side= 'left')
row4.pack(pady=5)

input_frame.pack(pady=5)

startpage.pack()

#insertion

for i in range(len(phonebook)):
    data=(phonebook[i]['name'], phonebook[i]['phone'], phonebook[i]['email'])
    table1.insert(parent='', index=tk.END, values= data)

def item_select(_):
    for i in table1.selection():
        print(table1.item(i)['values'])

def item_delete(_):
    for i in table1.selection():
        table1.delete(i)

def item_foredit(_):
    name_str.set(table1.item(table1.selection())['values'][0])
    phone_str.set(table1.item(table1.selection())['values'][1])
    email_str.set(table1.item(table1.selection())['values'][2])

table1.bind('<<TreeviewSelect>>', item_select)
table1.bind('<Delete>', item_delete)
table1.bind('<Double-Button-1>', item_foredit)

root.mainloop()