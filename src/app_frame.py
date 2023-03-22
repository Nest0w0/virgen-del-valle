import tkinter as tk
from tkinter import ttk


class AppFrame(tk.Frame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.controller = controller
		self.options = {'padx': 0, 'pady': 0}
		self.grid(sticky = 'nsew')
		self.configureGeometry()
		self['bg'] = '#81c1b0'
		
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