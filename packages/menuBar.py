try: from Tkinter import *
except ImportError: from tkinter import *

class menuBar:
	def __init__(self, master):
		super(menuBar, self).__init__()
		self.master = master

	def showMenu():
		print("showMenu")