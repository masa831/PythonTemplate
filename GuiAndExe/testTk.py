#-*- coding:utf-8 -*-
import sys
import tkinter as tk
from tkinter import ttk

# Tkinter App Template

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.create_widgets()
        self.set_windows_details()


    # Create Widgets function
    def create_widgets(self):
        #Label
        self.label_init = ttk.Label(self)
        self.label_init.configure(text='[Description] xxxx ')
        self.label_init.pack()

        #Button
        self.button_hello = ttk.Button(self)
        self.button_hello.configure(text="Hello World")
        self.button_hello.configure(command = self.say_Hello) #do not forget to add self!
        self.button_hello.pack()

        #Label
        self.label_hello = ttk.Label(self)
        self.label_hello.configure(text='A Label')
        self.label_hello.pack()

        #Entry
        self.name = tk.StringVar()
        self.entry_name = ttk.Entry(self)
        self.entry_name.configure(textvariable = self.name)
        self.entry_name.pack()

        #Label2
        self.label_name=ttk.Label(self)
        self.label_name.configure(text = 'Please input something in Entry')
        self.label_name.pack()

        # exitBotton
        self.button_quit = ttk.Button(self)
        self.button_quit.configure(text="Quit")
        self.button_quit.configure(command =lambda: self.quit()) #do not forget to add self!
        self.button_quit.bind('<Return>', lambda event: self.quit())
        self.button_quit.pack()

    def set_windows_details(self):
        self.master.update_idletasks()
        self.master.title("App Template [Tkinter]")
        self.master.resizable(False,False) # Windows Resize

        # sw, sh = self.master.winfo_screenmmwidth(), self.master.winfo_screenmmheight()
        # fw, fh = self.master.winfo_width(), self.master.winfo_height()
        # self.master.geometry(f'{fw}x{fh}+{sw//2-fw//2}+{sh//2-fh//2}')
        # self.master.deiconify()
        self.master.geometry("300x300")

    # Event Callback Function
    def say_Hello(self):
        print("Hello, World")  # on python console
        self.label_hello.configure(text="I Have benn Clicked!")
        print(self.name.get())
        self.label_name.configure(text=self.name.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
