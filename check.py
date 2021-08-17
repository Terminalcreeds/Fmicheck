#author: @savatorr
#just play with it and send me for a review
import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import webbrowser
import os
import sys
import subprocess
from cryptography.fernet import Fernet




class Window(Tk):
	def __init__(self):
		super(Window, self).__init__()
		self.title("Check FMI")
		self.minsize(500,500)
		self.wm_iconbitmap('76414826.ico')
		self.resizable(0,0)
		self.link()
		self.Frontend()
		self.previous()

	def Frontend(self):

		label=Label(self, text="Terminal", fg="red", font=("Times New Roman", 30, "bold"))
		label.place(x=100, y=10)

		label2=Label(self, text="Creeds", fg="black", font=("Times New Roman", 30, "bold"))
		label2.place(x=265, y=10)

		self.entry= Entry(self, width=23, font=("helvatica", 15, "bold"))
		self.entry.place(x=130, y=200)

		btn = ttk.Button(self, width=42,text="Check Info", command=self.backend)
		btn.place(x=128, y=250)


	def backend(self):
		self.response = requests.get('http://api.com/check.php?imei='+self.entry.get())
		soup = BeautifulSoup(response.text, 'html.parser')
		messagebox.showinfo("Response", soup.find_all('pre')[0].get_text(' '))



	def link(self):
		webbrowser.open("https://t.me/savatorr")
















if __name__ == '__main__':
	win = Window()
	win.mainloop()
