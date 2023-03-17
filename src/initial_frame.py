import tkinter as tk
from tkinter import ttk

class initialFrame(ttk.Frame):

	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.options = {'padx': 5, 'pady': 5}
		self.grid()
		self.buildButtons(self.controller)

	def show(self):
		self.lift()

	def buildButtons(self, controller):
		botonImportar = ttk.Button(
			self,
			text = 'Importar',
			command = lambda: controller.raiseFrame('ImportFrame')
		)
		botonImportar.grid(column = 0, row = 0, padx = 10, pady = 10)

		botonListar = ttk.Button(
			self,
			text = 'Listar'
		)
		botonListar.grid(column = 1, row = 0, padx = 10, pady = 10)

		botonExportar = ttk.Button(
			self,
			text = 'Exportar'
		)
		botonExportar.grid(column = 10, row = 0, padx = 10, pady = 10)
