from tkinter import *
from tkinter import ttk

def raiseFrame(frame):
	frame.tkraise()

if __name__ == '__main__':
	root = Tk()
	f1 = Frame(root)
	f2 = Frame(root)
	f1.grid(column = 0, row = 0)
	f2.grid(column = 0, row = 0)

	Label(f1, text = 'FRAME 1').pack()
	Button(f1, text = 'Ir a frame 2', command = lambda: raiseFrame(f2)).pack()
	Label(f2, text = 'FRAME 2').pack()
	Button(f2, text = 'Ir a frame 1', command = lambda: raiseFrame(f1)).pack()

	raiseFrame(f1)
	root.mainloop()