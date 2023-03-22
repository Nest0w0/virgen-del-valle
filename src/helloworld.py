from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import pandas as pd
import numpy as np


def buildTable(root, dataFrame):
	table = ttk.Treeview(root)
	table['columns'] = tuple(dataFrame.columns.values)

	for i in dataFrame.columns.values:
		table.heading('{}'.format(i), text = i, anchor = 'center')

	for i in range(len(dataFrame)):
		table.insert(
			parent = '',
			index = 'end',
			text = '',
			values = tuple(dataFrame.iloc[i].values)
		)
	
	table.pack()
	#table.grid(column = 0, row = 1, columnspan = 2, rowspan = 5)


if __name__ == '__main__':
	root = Tk()
	excel = pd.ExcelFile('/home/noxtol/Desktop/sample.xlsx')

	prueba = pd.read_excel(excel, 0)
	buildTable(root, prueba)
	root.mainloop()