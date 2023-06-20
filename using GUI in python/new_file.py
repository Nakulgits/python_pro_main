# import tkinter as tk

# class Sidebar(tk.Frame):
#     def __init__(self, master, options):
#         super().__init__(master, bg='#69359c')

#         # Create the line on the left side with a margin of 300 pixels
#         line = tk.Canvas(self, width=5, height=self.winfo_screenheight(), bg='#4b184f', bd=0, highlightthickness=0)
#         line.pack(side=tk.LEFT, fill=tk.Y, padx=300)

#         # Create the area for the options
#         self.options_frame = tk.Frame(self, bg='white', bd=0, highlightthickness=0)
#         self.options_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

#         self.buttons = []
#         for i, option in enumerate(options):
#             btn = tk.Button(
#                 self.options_frame, text=option, width=20, height=2,
#                 bg='#b897c4', activebackground='#4b184f',
#                 relief=tk.FLAT, bd=0, fg='white',
#                 command=lambda i=i: self.select(i)
#             )
#             btn.pack(pady=5, padx=10)
#             self.buttons.append(btn)

#         self.select(0)

#     def select(self, idx):
#         for i, btn in enumerate(self.buttons):
#             if i == idx:
#                 btn.config(bg='#4b184f', activebackground='#4b184f')
#             else:
#                 btn.config(bg='#b897c4', activebackground='#4b184f')


# class Window(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('My Window')
#         self.geometry('800x600')

#         options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
#         sidebar = Sidebar(self, options)
#         sidebar.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

#         # Add widgets to the space between the line and the left side of the window
#         button1 = tk.Button(self, text="Button 1", width=20, height=2, bg='#b897c4', activebackground='#4b184f',
#                             relief=tk.FLAT, bd=0, fg='white')
#         button1.pack(side=tk.LEFT, padx=300, pady=10)

#         button2 = tk.Button(self, text="Button 2", width=20, height=2, bg='#b897c4', activebackground='#4b184f',
#                             relief=tk.FLAT, bd=0, fg='white')
#         button2.pack(side=tk.LEFT, padx=20, pady=10)

#         button3 = tk.Button(self, text="Button 3", width=20, height=2, bg='#b897c4', activebackground='#4b184f',
#                             relief=tk.FLAT, bd=0, fg='white')
#         button3.pack(side=tk.LEFT, padx=20, pady=10)

#         button4 = tk.Button(self, text="Button 4", width=20, height=2, bg='#b897c4', activebackground='#4b184f',
#                             relief=tk.FLAT, bd=0, fg='white')
#         button4.pack(side=tk.LEFT, padx=20, pady=10)

#         self.mainloop()

# if __name__ == '__main__':
#     Window()
# import tkinter as tk

# class Window(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('My Window')
#         self.geometry('800x600')
#         self.resizable(False, False)

#         # Create the line on the left side with a margin of 300 pixels
#         line = tk.Canvas(self, width=5, height=self.winfo_screenheight(), bg='#4b184f', bd=0, highlightthickness=0)
#         line.pack(side=tk.LEFT, fill=tk.Y, padx=300)

#         # Create the area for the purple background
#         bg_frame = tk.Frame(self, bg='#69359c', bd=0, highlightthickness=0)
#         bg_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         # Create the area for the white background on the right side of the line
#         white_frame = tk.Frame(self, bg='white', bd=0, highlightthickness=0)
#         white_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.mainloop()

# if __name__ == '__main__':
#     Window()


import tkinter as tk

root = tk.Tk()
root.title("Window")
root.resizable(False, False)
root.attributes('-toolwindow', True)

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

canvas.create_line(100, 0, 100, 400)
canvas.create_rectangle(0, 0, 300, 400, fill="purple")
canvas.create_rectangle(300, 0, 600, 400, fill="white")

button1 = tk.Button(root, text="Button 1")
button1_window = canvas.create_window(150, 50, window=button1)

button2 = tk.Button(root, text="Button 2")
button2_window = canvas.create_window(150, 150, window=button2)

button3 = tk.Button(root, text="Button 3")
button3_window = canvas.create_window(150, 250, window=button3)

button4 = tk.Button(root, text="Button 4")
button4_window = canvas.create_window(150, 350, window=button4)

root.mainloop()





