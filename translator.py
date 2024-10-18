import translators as ts
from langdetect import detect
import tkinter as tk
from tkinter import ttk

langcodelist=('af','am','ar','az','eu','be','bn','bs','bg','ca','ceb','zh-TW','hr','cs','da','nl','en','eo','et','tl','fi','fr','de','el','gu','ht','iw','hi','hu','id','ga','it','ja','ko','lv','lt','mg','ms','mt','mn','no','fa','pl','pt','pa','ro','ru','sm','sr','sk','sl','es','sw','sv','ta','te','th','tr','uk','ur','vi','cy')
langlist=('afrikaans','amharic','arabic','azerbaijani','basque','belarusian','bengali','bosnian','bulgarian','catalan','cebuano','chinese','croatian','czech','danish','dutch','english','esperanto','estonian','filipino','finnish','french','german','greek','gujarati','haitiancreole','hebrew','hindi','hungarian','indonesian','irish','italian','japanese','korean','latvian','lithuanian','malagasy','malay','maltese','mongolian','norwegian','persian/farsi','polish','portuguese','punjabi','romanian','russian','samoan','serbian','slovak','slovenian','spanish','swahili','swedish','tamil','telugu','thai','turkish','ukrainian','urdu','vietnamese','welsh')

def translate_func():
    q_text=text_box.get("1.0",'end-1c')
    originlang= detect(q_text)
    output_text.set('Detected Language: '+ originlang)
    if originlang == 'zh-tw' :
        originlang = 'zh-TW'
    print(langcombo.get())
    tempid=langlist.index(langcombo.get())
    tolang= langcodelist[tempid]
    print(tolang)
    output_text.set(ts.translate_text(q_text,translator='google', from_language= originlang, to_language= tolang))

def copy_func():
    window.clipboard_clear()
    window.clipboard_append(output_text.get())

window =tk.Tk()
window.title('Translator')
window.geometry('800x700')

s= ttk.Style()
s.configure('TButton', font=('', 12))

title_label= ttk.Label(master= window, text='Translator to Chinese', font='Calibri 24')
title_label.pack(pady=10)

input_frame=ttk.Frame(master=window)
text_box=tk.Text(master=input_frame, width= 90, height=15)
button_frame =ttk.Frame(master= input_frame)
langstr =tk.StringVar(value=langlist[11])
langcombo=ttk.Combobox(button_frame, font= ('',12), textvariable=langstr, values=langlist)
langcombo.bind('<<ComboboxSelected>>', lambda event: output_text.set(f'Translate to {langstr.get()}'))
button=ttk.Button(master=button_frame, text='Translate', command= translate_func, style= 'TButton')
clipbutt =ttk.Button(master=button_frame, text= 'Copy translated text', command= copy_func, style= 'TButton')
text_box.pack(padx=10, pady=5)
langcombo.pack(padx=10, pady=5, side='left')
button.pack(padx=10, pady=5, side='left')
clipbutt.pack(padx=10, pady=5, side='left')
button_frame.pack(padx=10, pady=5)
input_frame.pack(padx=10, pady=5)

output_frame=ttk.Frame(master= window, border= '2', borderwidth='5')
output_text=tk.StringVar(value='Translated text will be shown here.')
output_label =ttk.Label(master=output_frame, textvariable= output_text)
output_label.pack(padx=10, pady=5)
output_frame.pack(padx=10, pady=5)

#q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
#q_text = '吉吉，一隻雞，雞是刺雞。 飢餓的刺雞，吉吉和吉吉雞肉'
#q_html = '''<!DOCTYPE html><html><head><title>《季姬击鸡记》</title></head><body><p>还有另一篇文章《施氏食狮史》。</p></body></html>'''

### usage
#_ = ts.preaccelerate_and_speedtest()  # Optional. Caching sessions in advance, which can help improve access speed.

#print(ts.translators_pool)
#print(ts.translate_text(q_text,translator='google', from_language= originlang, to_language= tolang))
#endingconfirm = input("Press enter to end")
#print(ts.translate_html(q_html, translator='alibaba'))

### parameters
#help(ts.translate_text)
window.mainloop()