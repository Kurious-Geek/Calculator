import tkinter as tk
from tkinter import ttk

class calculator(tk.Frame):
 	def __init__(self, parent, callbacks, *args, **kwargs):
 		super().__init__(parent, *args, **kwargs)
 		self.callbacks = callbacks

 		self.button = {}

 		display = tk.Entry(self, width=35)
 		display.grid(row=0, columnspan=4, pady=10, padx=10)

 		self.button['one'] = tk.Button(self, text='1', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['two'] = tk.Button(self, text='2', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['three'] = tk.Button(self, text='3', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['four'] = tk.Button(self, text='4', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['five'] = tk.Button(self, text='5', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['six'] = tk.Button(self, text='6', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['seven'] = tk.Button(self, text='7', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['eight'] = tk.Button(self, text='8', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['nine'] = tk.Button(self, text='9', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['zero'] = tk.Button(self, text='0', padx=40, pady=20, command=self.callbacks['arithmetic'])
 		self.button['divide'] = tk.Button(self, text='/', padx=35, pady=20, command=self.callbacks['arithmetic'])
 		self.button['multiply'] = tk.Button(self, text='X', padx=34, pady=20, command=self.callbacks['arithmetic'])
 		self.button['substract'] = tk.Button(self, text='-', padx=35, pady=20, command=self.callbacks['arithmetic'])
 		self.button['add'] = tk.Button(self, text='+', padx=35, pady=20, command=self.callbacks['arithmetic'])
 		self.button['equal'] = tk.Button(self, text='=', padx=39, pady=20, command=self.callbacks['arithmetic'])
 		self.button['period'] = tk.Button(self, text='.', padx=41, pady=20, command=self.callbacks['arithmetic'])
 		self.button['clear'] = tk.Button(self, text='Clear', padx=25, pady=20, command=self.callbacks['arithmetic'])

 		self.button['one'].grid(row=3, column=0)
 		self.button['two'].grid(row=3, column=1)
 		self.button['three'].grid(row=3, column=2)
 		self.button['multiply'].grid(row=3, column=3)

 		self.button['four'].grid(row=2, column=0)
 		self.button['five'].grid(row=2, column=1)
 		self.button['six'].grid(row=2, column=2)
 		self.button['substract'].grid(row=2, column=3)

 		self.button['seven'].grid(row=1, column=0)
 		self.button['eight'].grid(row=1, column=1)
 		self.button['nine'].grid(row=1, column=2)
 		self.button['clear'].grid(row=1, column=3)

 		self.button['period'].grid(row=4, column=0)
 		self.button['zero'].grid(row=4, column=1)
 		self.button['equal'].grid(row=4, column=2)
 		self.button['divide'].grid(row=4, column=3)
 		self.button['add'].grid(row=5, column=3)

 		




