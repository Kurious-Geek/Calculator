import tkinter as tk
from tkinter import ttk

class calculator(tk.Frame):
 	def __init__(self, parent, *args, **kwargs):
 		super().__init__(parent, *args, **kwargs)
 		#self.callbacks = callbacks

 		self.button = {}

 		self.display = tk.Text(self, font=('Droid', 20), width=24, height=2)
 		self.display.grid(row=0, columnspan=4)

 		self.button['percent'] = tk.Button(self, text='%', padx=38, pady=20, command=lambda: self.arithmetic('%'))
 		self.button['open_bracket'] = tk.Button(self, text='(', padx=41, pady=20, command=lambda:self.arithmetic('('))
 		self.button['close_bracket'] = tk.Button(self, text=')', padx=40, pady=20, command=lambda:self.arithmetic(')'))
 		self.clear_button = tk.Button(self, text=u'\u232b', padx=31, pady=20, command=self.clear)

 		self.button['seven'] = tk.Button(self, text='7', padx=40, pady=20, command=lambda:self.arithmetic(7))
 		self.button['eight'] = tk.Button(self, text='8', padx=40, pady=20, command=lambda:self.arithmetic(8))
 		self.button['nine'] = tk.Button(self, text='9', padx=40, pady=20, command=lambda:self.arithmetic(9))
 		self.button['divide'] = tk.Button(self, text=u'\u00F7', padx=34, pady=20, command=lambda:self.arithmetic('/'))

 		self.button['four'] = tk.Button(self, text='4', padx=40, pady=20, command=lambda:self.arithmetic(4))
 		self.button['five'] = tk.Button(self, text='5', padx=40, pady=20, command=lambda:self.arithmetic(5))
 		self.button['six'] = tk.Button(self, text='6', padx=40, pady=20, command=lambda:self.arithmetic(6))
 		self.button['multiply'] = tk.Button(self, text='X', padx=35, pady=20, command=lambda:self.arithmetic('*'))

 		self.button['one'] = tk.Button(self, text='1', padx=40, pady=20, command=lambda:self.arithmetic(1))
 		self.button['two'] = tk.Button(self, text='2', padx=40, pady=20, command=lambda:self.arithmetic(2))
 		self.button['three'] = tk.Button(self, text='3', padx=40, pady=20, command=lambda:self.arithmetic(3))
 		self.button['substract'] = tk.Button(self, text='-', padx=36, pady=20, command=lambda:self.arithmetic('-'))

 		self.button['period'] = tk.Button(self, text='.', padx=41, pady=20, command=lambda:self.arithmetic('.'))
 		self.button['zero'] = tk.Button(self, text='0', padx=40, pady=20, command=lambda:self.arithmetic(0))
 		self.equal_button = tk.Button(self, text='=', padx=39, pady=20, command=self.equal)
 		self.button['add'] = tk.Button(self, text='+', padx=34, pady=20, command=lambda:self.arithmetic('+'))
 
 		self.button['percent'].grid(row=1, column=0)
 		self.button['open_bracket'].grid(row=1, column=1)
 		self.button['close_bracket'].grid(row=1, column=2)
 		self.clear_button.grid(row=1, column=3)

 		self.button['seven'].grid(row=2, column=0)
 		self.button['eight'].grid(row=2, column=1)
 		self.button['nine'].grid(row=2, column=2)
 		self.button['divide'].grid(row=2, column=3)

 		self.button['four'].grid(row=3, column=0)
 		self.button['five'].grid(row=3, column=1)
 		self.button['six'].grid(row=3, column=2)
 		self.button['multiply'].grid(row=3, column=3)

 		self.button['one'].grid(row=4, column=0)
 		self.button['two'].grid(row=4, column=1)
 		self.button['three'].grid(row=4, column=2)
 		self.button['substract'].grid(row=4, column=3)

 		self.button['period'].grid(row=5, column=0)
 		self.button['zero'].grid(row=5, column=1)
 		self.equal_button.grid(row=5, column=2)
 		self.button['add'].grid(row=5, column=3)

 		self.clear()

 	def clear(self):
 		self.current = self.display.get(0.0, tk.END)
 		self.display.delete('1.0', 'end')
 		
 		
 	def arithmetic(self, number):
 		
 		self.display.insert(tk.INSERT, number)

 	def equal(self):
 		cmd = self.display.get(1.0, 'end').strip()
 		if cmd:
 			try:
 				output = str(eval(cmd))
 			except Exception as e:
 				output = str(e)

 		#self.display.delete(tk.END, 1.0)
 		self.display.insert(tk.END, '\n' + output)


 		





