import tkinter as tk

window = tk.Tk()

WIDTH = 700
HEIGHT = 500
x = 20
y = 30

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

window.mainloop()

