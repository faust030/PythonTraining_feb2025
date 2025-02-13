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

increment = 0

def printeaza_in_consola():
    global increment
    increment += 1
    print(f"Butonul a fost apasat de {increment} ori")

button = tk.Button(window, text="Apasa-ma!", command = printeaza_in_consola)
button.pack()

window.mainloop()

