from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os

def raiseFrame(frame):
	frame.tkraise()

if __name__ == '__main__':
	root = Tk()
	root.geometry("300x300")
	root.title("Prueba")
	root.resizable(False,False)

	curdir = os.getcwd()
	tempdir = filedialog.askdirectory(
		parent = root,
		initialdir = curdir,
		title = 'Seleccione'
	)

	if len(tempdir) > 0:
		print("Eligió {}".format(tempdir))
	root.mainloop()