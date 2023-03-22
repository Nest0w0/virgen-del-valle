import tkinter as tk
import os
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
from app_frame import AppFrame

class importFrame(AppFrame):

	def __init__(self, controller):
		super().__init__(
			controller
		)
		self.buildButtons(self.controller)
		#self.buildTable()
		self.buildLabel()

	def buildLabel(self):
		labelImportar = ttk.Label(
			self,
			text = 'Importar'
		)
		labelImportar.grid(column = 2, row = 0)

	def buildTable(self, dataFrame):
		table = ttk.Treeview(self, show = 'headings')
		table['columns'] = tuple(['id']) + tuple(dataFrame.columns.values)

		table.column('id', width = 0, stretch = False)
		table.heading('id', text = '', anchor = 'center')		
		for column in dataFrame.columns.values:
			table.heading('{}'.format(column), text = column, anchor = 'center')

		for i in range(len(dataFrame)):
			table.insert(
				parent = '',
				index = 'end',
				text = '',
				values = tuple([i]) + tuple(dataFrame.iloc[i].values)
			)		
		table.grid(column = 0, row = 1, columnspan = 3, rowspan = 6)

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
				filetypes = [('Archivos de Excel', '*.xlsx'),
							('Archivos de Excel', '*.xls')]
			)

		excel = pd.ExcelFile(self.imported_excel.name)
		tabla = pd.read_excel(excel, 0)
		self.buildTable(tabla)