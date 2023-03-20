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

	frame = Frame(root)
	frame.pack()

	tabla = ttk.Treeview(frame)