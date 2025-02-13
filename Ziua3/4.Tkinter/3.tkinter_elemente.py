import tkinter as tk

window = tk.Tk()

WIDTH = 700
HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_hight = window.winfo_screenheight()
x = screen_width // 2 - WIDTH // 2
y = screen_hight // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

label1 = tk.Label(window, text = "Label-ul meu.... din fereastra mea")
label1.pack()

label2 = tk.Label(window, text = "Un alt label al mey.... din fereastra mea")
label2.pack()

label_list = []

for i in range(100):
    new_label = tk.Label(window, text = f"Label-ul {i}.... din fereastra mea")
    new_label.pack()
    label_list.append(new_label)


scroll_bar = tk.Scrollbar(window)
scroll_bar.pack(side="right")



window.mainloop()

