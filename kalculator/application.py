import tkinter as tk
from tkinter import ttk
from . import view as v
from tkinter import messagebox

class app(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title('Kalculator')
		self.resizable(False, False)
		self.attributes('-alpha', 0.9)

		self.callbacks = {
							'quad_equation':self.quadratic_eqn,
							'exit':self.Exit,

		}

		menu = v.Menu(self, self.callbacks)
		self.config(menu=menu)

		self.calc = v.calculator(self)
		self.calc.grid()

	def quadratic_eqn(self):
		self.calc.quad_equation_data('a')

	def Exit(self):
		title = 'Exit Kalculator'
		message = 'Closing ... '
		detail = 'Are you sure you want to exit the app?'
		close_option = messagebox.askyesno(title=title, message=message, detail=detail)
		if not close_option:
			return
		else:
			self.quit()
			self.destroy()
			exit()


