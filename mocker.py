"""
mocker.py: A small application that reads a string you give it and mocks you for it.

Author: Sohaib Khadri

"""

from tkinter import *
from tkinter import colorchooser, messagebox, ttk, END
from ttkthemes import themed_tk as tk
import os


# GUI system
root = tk.ThemedTk()
root.get_themes()
root.set_theme("equilux")
root.title("Mocker")
root.iconbitmap('icon.ico')
root.configure(bg='grey20')
root.resizable(False, False)

input_frame = LabelFrame(root,text=" Input ", font=('Malgun Gothic', 15), fg='White', padx=10, pady=10, bg='grey25', borderwidth = 0,highlightthickness=0)
input_frame.pack()
middle_frame = LabelFrame(root, padx=10, pady=0, bg='grey20', borderwidth = 0,highlightthickness=0)
middle_frame.pack()
output_frame = LabelFrame(root,text=" Output ", font=('Malgun Gothic', 15), fg='White', padx=10, pady=10, bg='grey25', borderwidth = 0,highlightthickness=0)
output_frame.pack()

add_qs = IntVar()

input_field = Text(input_frame, height=10, width=40)
input_field.pack()

add_qs_button = Checkbutton(middle_frame, text = "Add Quotations", variable = add_qs, bg='grey20', fg = 'white', highlightcolor = 'grey20', selectcolor="black")
add_qs_button.pack()

output_field = Text(output_frame, height=10, width=40)
#output_field.config(state=DISABLED)
output_field.pack()

def mock():
    input_string = input_field.get("1.0",END).rstrip()
    
    output = ""
    switch = True

    #print(add_qs.get())

    if add_qs.get():
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

    if add_qs.get():
        output += "\""

    print("out:" + output)
    output_field.delete('1.0', END)
    output_field.insert(END, output)
    

mock_button = Button(middle_frame, text = "Mock!", command=mock, bg='grey20', fg = 'white')
mock_button.pack()

copy_button = Button(middle_frame, text = "Copy to Clipboard", command = lambda: root.clipboard_append(output_field.get("1.0",END).rstrip()), bg='grey20', fg = 'white')
copy_button.pack()






if __name__ == '__main__':
    # GUI loop
    
    root.mainloop()

    
    
