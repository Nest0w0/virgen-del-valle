import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
	root = tk.Tk()
	root.title('MALDITA SEA BARRAS DE SCROLL')
	#root.grid_columnconfigure(0, weight = 1)
	#root.grid_rowconfigure(0, weight = 1)

	text = tk.Text(root, height = 10)
	text.pack(side = 'left', fill = 'y')

	scroll = ttk.Scrollbar(root, orient = 'vertical', command = text.yview)
	scroll.pack(side = 'right', fill = 'y')

	text['yscrollcommand'] = scroll.set

	for i in range(1,50):
		position = '{}'.format(i)
		text.insert(position, 'Line {}'.format(i))

	root.mainloop()