import tkinter as tk
from tkinter import ttk

class initialFrame(ttk.Frame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.controller = controller
		self.options = {'padx': 0, 'pady': 0}
		self.grid(sticky = 'nsew')
		self.configureGeometry()
		self.buildButtons(self.controller)
		self.buildList()

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

	def buildButtons(self, controller):
		botonImportar = ttk.Button(
			self,
			text = 'Importar',
			command = lambda: controller.raiseFrame('ImportFrame'),
		)
		botonImportar.grid(
			column = 0,
			row = 6,
			padx = 10,
			pady = 10
		)

		botonListar = ttk.Button(
			self,
			text = 'Listar'
		)
		botonListar.grid(column = 1, row = 6, padx = 10, pady = 10)

		botonExportar = ttk.Button(
			self,
			text = 'Exportar'
		)
		botonExportar.grid(column = 2, row = 6, padx = 10, pady = 10)

	def buildList(self):
		list = ttk.Frame(
			self
		)
		list.grid(column = 0, row = 1, columnspan = 3, rowspan = 5)
