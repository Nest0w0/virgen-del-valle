import tkinter as tk
from tkinter import ttk
from app_frame import AppFrame

class initialFrame(AppFrame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.buildButtons(self.controller)
		#self.buildList()

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
