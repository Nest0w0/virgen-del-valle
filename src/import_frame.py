import tkinter as tk
from tkinter import ttk

class importFrame(tk.Frame):

	def __init__(self, parent, controller):
		super().__init__(parent)
		self.controller = controller
		self.options = {'padx': 5, 'pady': 5}
		self.grid()
		self.buildButtons(self.controller)

	def buildButtons(self, controller):
		volver = ttk.Button(
			self,
			text = 'Volver',
			command = lambda: controller.raiseFrame('InitialFrame')
		)
		volver.grid(column = 0, row = 0)
		var = 0
		importarDiferencia = ttk.Radiobutton(
			self,
			text = 'Diferencia',
			variable = var,
			value = 1
			)
		importarDiferencia.grid(column = 0, row = 1)
		
		importarDestructiva = ttk.Radiobutton(
			self,
			text = 'Completa',
			variable = var,
			value = 2
			)
		importarDestructiva.grid(column = 1, row = 1)
