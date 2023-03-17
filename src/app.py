from tkinter import *
from tkinter import ttk
from initial_frame import initialFrame
from import_frame import importFrame

class Root(Tk):
	def __init__(self):
		super().__init__()
		self.title('Virgen del Valle')
		self.resizable(width = False, height = False)
		self.container = Frame(self)
		self.container.grid(column = 0, row = 0)

		self.frames = {}
	
		self.frames["InitialFrame"] = initialFrame(parent = self.container, controller = self)
		self.frames["ImportFrame"] = importFrame(parent = self.container, controller = self)
		
		self.frames["InitialFrame"].grid(column = 0, row = 0)
		self.frames["ImportFrame"].grid(column = 0, row = 0)

		self.raiseFrame("InitialFrame")
		
	def setStyles(self):
		self.configure('TButton', background = 'green')

	def raiseFrame(self, frameName):
		frame = self.frames[frameName]
		frame.tkraise()

if __name__ == '__main__':
	root = Root()
	root.mainloop()