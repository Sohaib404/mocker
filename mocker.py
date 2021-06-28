"""
mocker.py: A small application that reads a string you give it and mocks you for it.

Author: Sohaib Khadri

"""

from tkinter import *
from tkinter import colorchooser, messagebox, ttk
from ttkthemes import themed_tk as tk
import os

'''
# GUI system
root = tk.ThemedTk()
root.get_themes()
root.set_theme("equilux")
root.title("Mocker")
root.iconbitmap('images/icon.ico')
root.resizable(False, False)
root.configure(bg='grey20')

notebook_style = ttk.Style()
notebook_style.configure('Custom.TNotebook.Tab', padding=[46, 0])

notebook = ttk.Notebook(root, style='Custom.TNotebook')
notebook.grid(row=1, column=0, padx=15, pady=15)

menu_tab = LabelFrame(notebook, padx=10, pady=5, bg='grey20')
settings_tab = LabelFrame(notebook, padx=10, pady=5, bg='grey20')
#menu_tab.pack()
#settings_tab.pack()

preset_frame = LabelFrame(menu_tab, text=" Presets ", font=('Malgun Gothic', 15), fg='White', padx=5, pady=5,
                          bg='grey20')
preset_frame.grid(row=1, column=0, sticky=W+E, padx=5, pady=2)
'''

if __name__ == '__main__':
    # GUI loop
    #root.mainloop()

    input_string = input()
    output = ""
    switch = True
    add_qs = True

    if add_qs:
        output += "\""
    for char in input_string:
        #print(ord(char))
        if switch:

            if ord(char) > 64 and ord(char) < 91:
                output += chr(ord(char)+32)
                switch = not switch
            elif ord(char) > 96 and ord(char) < 123:
                output += chr(ord(char)-32)
                switch = not switch
            else:
                output += char

        else:
            output += char
            switch = not switch
        
        
        
        
    if add_qs:
        output += "\""
    
    print("out:" + output)
