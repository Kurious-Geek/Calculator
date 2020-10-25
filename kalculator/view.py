import tkinter as tk
from tkinter import ttk

class calculator(tk.Frame):
 	def __init__(self, parent, *args, **kwargs):
 		super().__init__(parent, *args, **kwargs)
 		#self.callbacks = callbacks

 		self.button = {}
 		self.old = ''
 		self.expression = tk.StringVar()

 		display_bg = '#181818'
 		font = ('Times', 12)
 		num_button_bg = '#686868'
 		num_button_fg = 'white'
 		function_bg = '#585858'

 		self.config(bg=display_bg)		

 		display_frame = tk.Frame(self, bg=display_bg)
 		display_frame.grid(row=0, columnspan=4, sticky=tk.E)

 		self.display = ttk.Label(display_frame, font=('Droid', 25), textvariable=self.expression, justify='right', cursor='ibeam', wraplength='360', background=display_bg, foreground='white')
 		self.display.grid(row=0, sticky=tk.E, pady=20, padx=5)

 		self.button_frame = tk.Frame(self, bg=num_button_bg)
 		self.button_frame.grid(row=1)
 		
 		self.button['open_bracket'] = tk.Button(self.button_frame, text='(', font=font, padx=38.5, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp('('))
 		self.button['close_bracket'] = tk.Button(self.button_frame, text=')', font=font, padx=38.5, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp(')'))
 		self.button_cancel_everything = tk.Button(self.button_frame, text='CE', font=font, padx=31, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=self.clear_all)
 		self.back_button = tk.Button(self.button_frame, text=u'\u232b', font=font, padx=27, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=self.backspace)

 		self.button['seven'] = tk.Button(self.button_frame, text='7', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(7))
 		self.button['eight'] = tk.Button(self.button_frame, text='8', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(8))
 		self.button['nine'] = tk.Button(self.button_frame, text='9', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(9))
 		self.button['divide'] = tk.Button(self.button_frame, text=u'\u00F7', font=font, padx=33, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp("\u00F7"))

 		self.button['four'] = tk.Button(self.button_frame, text='4', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(4))
 		self.button['five'] = tk.Button(self.button_frame, text='5', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(5))
 		self.button['six'] = tk.Button(self.button_frame, text='6', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(6))
 		self.button['multiply'] = tk.Button(self.button_frame, text=u'\u00D7', font=font, padx=33, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp('\u00D7'))

 		self.button['one'] = tk.Button(self.button_frame, text='1', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(1))
 		self.button['two'] = tk.Button(self.button_frame, text='2', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(2))
 		self.button['three'] = tk.Button(self.button_frame, text='3', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(3))
 		self.button['substract'] = tk.Button(self.button_frame, text='-', font=font, padx=34, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp('-'))

 		self.button['period'] = tk.Button(self.button_frame, text='.', font=font, padx=39, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp('.'))
 		self.button['zero'] = tk.Button(self.button_frame, text='0', font=font, padx=37, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=lambda:self.integer_inp(0))
 		self.equal_button = tk.Button(self.button_frame, text='=', font=font, padx=36, pady=20, relief=tk.FLAT, background=num_button_bg, foreground=num_button_fg, command=self.equal)
 		self.button['add'] = tk.Button(self.button_frame, text='+', font=font, padx=33, pady=20, relief=tk.FLAT, background=function_bg, foreground=num_button_fg, command=lambda:self.integer_inp('+'))
 
 		self.button['open_bracket'].grid(row=1, column=1)
 		self.button['close_bracket'].grid(row=1, column=2)
 		self.button_cancel_everything.grid(row=1, column=0)
 		self.back_button.grid(row=1, column=3)

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

 		self.clear_all()
 
 	def clear_all(self):
 		self.old = ''
 		self.expression.set('')

 	def backspace(self):
 		expression = self.expression.get()
 		integer = list(expression)
 		try:
 			del integer[-1]
 		except IndexError:
 			return
 		else:
	 		new_integer = ''.join(integer)
	 		self.expression.set(new_integer)
	 		self.old = new_integer
 		
 	def integer_inp(self, number):

 		if self.old == '':
 			self.expression.set(number)
 			self.old = number
 		else:
 			self.new = str(self.old) + str(number)
 			self.expression.set(self.new)
 			self.old = self.new

 		

 	def equal(self):
 		cmd = self.expression.get().strip()
 		
 		if '\u00F7' or '\u00D7' in cmd:
 			cmd = cmd.replace("\u00F7", "/")
 			cmd = cmd.replace("\u00D7", "*")

 		else:
 			cmd = cmd

 		try:
 			output = str(eval(cmd))
 		except Exception as e:
 			output = 'Syntax Error'

 		self.expression.set(output)
 		self.old = output


 		
