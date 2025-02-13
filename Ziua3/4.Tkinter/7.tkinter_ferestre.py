import tkinter as tk

window = tk.Tk()

WIDTH = 700
HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_hight = window.winfo_screenheight()
x = screen_width // 2 - WIDTH // 2
y = screen_hight // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

counter = 0

def aduna_valoare(x):
    global counter
    counter += x
    print(f"Counter-ul este la {counter}")
    counter_label.config(text = f"      {counter}       ")

label = tk.Label(window, text = "Mariti sau micsorati valoarea")
label.pack()

frame = tk.Frame(window)  
frame.pack()  

minus_button = tk.Button(frame, text = "    -   ", command = lambda x = -1: aduna_valoare(x))
minus_button.grid(row=0, column=0)

plus_button = tk.Button(frame, text = "     +     ", command = lambda x = +1: aduna_valoare(x))
plus_button.grid(row=0, column=2)

counter_label = tk.Label(frame, text=f"     {counter}    ")
counter_label.grid(row=0, column=1)



window.mainloop()