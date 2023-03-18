import tkinter as tk
from tkinter import ttk

class importFrame(tk.Frame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.controller = controller
		self.options = {'padx': 0, 'pady': 0}
		self.grid(sticky = 'nsew')
		self.configureGeometry()
		self.buildButtons(self.controller)


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
		volver = ttk.Button(
			self,
			text = 'Volver',
			command = lambda: controller.raiseFrame('InitialFrame')
		)
		volver.grid(column = 0, row = 0, pady = 5)

		labelImportar = ttk.Label(
			self,
			text = 'Importar'
		)
		labelImportar.grid(column = 0, row = 6)

		var = 0
		importarDiferencia = ttk.Radiobutton(
			self,
			text = 'Diferencia',
			variable = var,
			value = 1
			)
		importarDiferencia.grid(column = 1, row = 6)
		
		importarDestructiva = ttk.Radiobutton(
			self,
			text = 'Completa',
			variable = var,
			value = 2
			)
		importarDestructiva.grid(column = 2, row = 6)
