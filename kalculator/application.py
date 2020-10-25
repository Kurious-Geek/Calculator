import tkinter as tk
from tkinter import ttk
from . import view as v

class app(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title('Kalculator')
		self.resizable(False, False)

		self.callbacks = {}

		calc = v.calculator(self)
		calc.grid()


