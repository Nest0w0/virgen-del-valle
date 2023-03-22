import tkinter as tk
from tkinter import ttk

class Table(tk.Canvas):

	def __init__(self, controller):
		super().__init__(
			controller
		)

		self.horizontal_scroll = tk.Scrollbar(
			self,
			orient = 'horizontal',
			command = self.xview
		)
		self.horizontal_scroll.pack(side = 'bottom', fill = 'x')
		#self.horizontal_scroll.config(command = self.xview)
		
		self.vertical_scroll = tk.Scrollbar(
			self,
			orient = 'vertical',
			command = self.yview
		)
		self.vertical_scroll.pack(side = 'right', fill = 'y')
		#self.vertical_scroll.config(command = self.yview)
		
		#self.config(
		#	xscrollcommand = self.horizontal_scroll.set,
		#	yscrollcommand = self.vertical_scroll.set)
		
		self['yscrollcommand'] = self.vertical_scroll.set
		self['xscrollcommand'] = self.horizontal_scroll.set
		self.grid(column = 0, row = 1, columnspan = 3, rowspan = 6)


	def buildTable(self, dataFrame):
		table = ttk.Treeview(
			self,
			show = 'headings'
		)
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
		table.pack()