#Author: @Terminalcreeds
#modified: 8/24/2021
#Added the ability to block Fiddler and other sniffing tool 

#++++++ Imported Modules+++++++
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
from PIL import ImageTk,Image
import time


#++++++ Imported Modules+++++++




class Window(Tk):
	def __init__(self):
		super(Window, self).__init__()
		self.title("Check FMI")
		self.minsize(500,500)
		self.wm_iconbitmap('76414826.ico')
		self.resizable(0,0)
		self.link()
		self.update()
		self.previous()
		self.Frontend()
		

	def Frontend(self):
		


		
		image = Image.open('images/images.png')
		image = image.resize((500, 500), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		label = tk.Label(self, image=photo)
		label.image = photo
		label.pack(expand=True)

		

		self.label=Label(self, text="Terminal", fg="red", font=("Times New Roman", 30, "bold"))
		self.label.place(x=120,y=50)
		

		self.label2=Label(self, text="Creeds", fg="black", font=("Times New Roman", 30, "bold"))
		self.label2.place(x=285,y=50)
		


		self.label3=Label(self, text="Enter IMEI/SN", fg="black", font=("Times New Roman", 20, "bold"))
		self.label3.place(x=180,y=200)
		

		self.entry= Entry(self, width=23, font=("helvatica", 15, "bold"))
		self.entry.place(x=145,y=250)
		self.entry.focus()

		self.btn = ttk.Button(self, width=42,text="Check Info", command=self.backend)
		self.btn.place(x=145,y=300)

		self.btn2 = ttk.Button(self, width=42,text="Open Menu Help", command=self.OpenMenu)
		self.btn2.place(x=145,y=400)
		

	def update(self):
		try:
			url = requests.get("https://terminalcreeds.com/version.txt")
			version="1.6 beta2"
			if url.text <=  version:
				pass
			elif url.text >= version :
				messagebox.showinfo("update", "Software Update!")
				webbrowser.open("https://www.mediafire.com/file/djldmuuvg9eb1g9/Terminalcreeds_Fmi_Check.zip/file?fbclid=IwAR3cw96Ksl_JX7x89ajXlWHQEDIsuLyw-8uLXUjPb2mVSFA1hHXfuEyiEhs")
				exit()
		except Exception as e:
			messagebox.showerror("error", "Ooops you are not connected to the internet")
			exit()
	def backend(self):
		try:
			self.secure()
	
			response = requests.get('https://api.com/fmi_checker.php?imei='+self.entry.get())#insert your API for checkng imei Info
			
			soup = BeautifulSoup(response.text, 'html.parser')
			messagebox.showinfo("Response", soup.find_all('pre')[0].get_text(' '))
		except Exception as e:
		
			messagebox.showerror("Server Error", "No internet connection")



	def link(self):
		webbrowser.open("https://t.me/savatorr")
	def secure(self):
		i = subprocess.check_output('tasklist', shell=True)
		#print(s)
		for e in range(1000):

			if b'Fiddler Everywhere.exe, wireshark.exe,Fiddler.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit fiddler")
				exit()
				time.sleep(1)

			elif b'Fiddler.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit fiddler telerik")
				exit()
				time.sleep(1)

			elif b'Wireshark.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit wireshark")
				
				exit()



	def previous(self):
		#this will block any sniffing tool from getting your API
		i = subprocess.check_output('tasklist', shell=True)
		#print(s)
		for e in range(1000):

			if b'Fiddler Everywhere.exe, wireshark.exe,Fiddler.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit fiddler")
				exit()
				time.sleep(1)

			elif b'Fiddler.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit fiddler telerik")
				exit()
				time.sleep(1)

			elif b'Wireshark.exe' in i:
				messagebox.showinfo("Error", "Don't be a smart ass exit wireshark")
				
				exit()

		
		













if __name__ == '__main__':
	win = Window()
	win.mainloop()
