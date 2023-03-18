from tkinter import *
from tkinter import ttk
from initial_frame import initialFrame
from import_frame import importFrame

class Root(Tk):
	def __init__(self):
		super().__init__()
		self.title("Virgen del Valle")
		self.resizable(width = False, height = False)
		self.getScreenSize()
		self.geometry("{}x{}".format(
			self.width,
			self.height
			)
		)
		self.configureGeometry()
		self.frames = {}
		self.setFrames()

	def configureGeometry(self):
		self.configureColumns()
		self.configureRows()

	def configureColumns(self):
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 1)

	def configureRows(self):
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		self.rowconfigure(3, weight = 1)
		self.rowconfigure(4, weight = 1)
		self.rowconfigure(5, weight = 1)
		self.rowconfigure(6, weight = 1)
		self.rowconfigure(7, weight = 1)

	def getScreenSize(self):
		self.width = self.winfo_screenwidth()
		self.height = self.winfo_screenheight()

	def setFrames(self):
		self.frames["InitialFrame"] = initialFrame(
			controller = self
		)
		self.frames["ImportFrame"] = importFrame(
			controller = self
		)
		
		self.frames["InitialFrame"].grid(
			column = 0, 
			row = 0, 
			columnspan = 2,
			rowspan = 6)
		self.frames["ImportFrame"].grid(
			column = 0, 
			row = 0,
			columnspan = 2,
			rowspan = 6)

		self.raiseFrame("InitialFrame")

	def setStyles(self):
		self.configure('TButton', background = 'green')

	def raiseFrame(self, frameName):
		frame = self.frames[frameName]
		frame.tkraise()

if __name__ == '__main__':
	root = Root()
	root.mainloop()