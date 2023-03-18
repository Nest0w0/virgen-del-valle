from tkinter import *
from tkinter import ttk

def raiseFrame(frame):
	frame.tkraise()

if __name__ == '__main__':
	root = Tk()
	root.geometry("300x300")
	root.title("Prueba")
	root.resizable(False,False)

	#configura las columnas
	root.columnconfigure(0, weight = 1)
	root.columnconfigure(1, weight = 2)

	usernamelabel = ttk.Label(root, text = 'Username:')
	usernamelabel.grid(row = 0, column = 0)
	passwordlabel = ttk.Label(root, text = 'Password:')
	passwordlabel.grid(row = 1, column = 0)


	usernameentry = ttk.Entry(root)
	usernameentry.grid(row = 0, column = 1)
	passwordentry = ttk.Entry(root, show = '*')
	passwordentry.grid(row = 1, column = 1)
	root.mainloop()