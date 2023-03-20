import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class importFrame(tk.Frame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.controller = controller
		self.options = {'padx': 0, 'pady': 0}
		self.grid(sticky = 'nsew')
		self.configureGeometry()
		self['bg'] = '#81c1b0'
		self.buildButtons(self.controller)
		self.buildTable()


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

	def buildLabel(self):
		labelImportar = ttk.Label(
			self,
			text = 'Importar'
		)
		labelImportar.grid(column = 0, row = 6)

	def buildTable(self):
		table = ttk.Treeview(self)
		
		table['columns'] = ('Nombre', 'Apellido', 'Cedula', 'Edad')
		
		
		table.column('#0', width = 0)
		table.column('Nombre')
		table.column('Apellido')
		table.column('Cedula')
		table.column('Edad')

		table.heading('Nombre', text = 'Nombre', anchor = 'center')
		table.heading('Apellido', text = 'Apellido', anchor = 'center')
		table.heading('Cedula', text = 'Cedula', anchor = 'center')
		table.heading('Edad', text = 'Edad', anchor = 'center')

		table.insert(
			parent = '',
			index = 'end',
			text = '',
			values = ('Nestor', 'Aguilar', '28316308', '22')
		)
		
		table.grid(column = 0, row = 1, columnspan = 2, rowspan = 5)

	def buildButtons(self, controller):
		volver = ttk.Button(
			self,
			text = 'Volver',
			command = lambda: controller.raiseFrame('InitialFrame')
		)
		volver.grid(column = 0, row = 0, pady = 5)

		var = 0
		importarDiferencia = ttk.Radiobutton(
			self,
			text = 'Diferencia',
			variable = var,
			value = 1
			)
		importarDiferencia.grid(column = 0, row = 6)
		
		importarDestructiva = ttk.Radiobutton(
			self,
			text = 'Completa',
			variable = var,
			value = 2
			)
		importarDestructiva.grid(column = 1, row = 6)

		botonSeleccionar = ttk.Button(
			self,
			text = 'Seleccionar',
			command = lambda: self.getExcelPath()
		)
		botonSeleccionar.grid(column = 2, row = 6)


	def getExcelPath(self):
		self.imported_excel = filedialog.askopenfile(
				parent = self,
				initialdir = os.getcwd(),
				title = 'Seleccione su archivo Excel',
				filetypes = [('Archivos de Excel', '*.xlsx')]
			)

		print(self.imported_excel.name)