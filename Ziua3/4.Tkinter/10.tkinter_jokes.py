import tkinter as tk
import requests
import json

LINK = "http://icanhazdadjoke.com"
window = tk.Tk()

WIDTH = 700
HEIGHT = 500

screen_width = window.winfo_screenwidth()
screen_hight = window.winfo_screenheight()
x = screen_width // 2 - WIDTH // 2
y = screen_hight // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")



def fetch_new_joke():
    parameti = {"Accept": "application/json"}
    response = requests.get(LINK, headers = parameti)
    json_response = json.loads(response.text)
    joke = json_response["joke"]
    joke_label.config(text = joke)


joke_label = tk.Label(window, text = "Aici va fi gluma")
joke_label.pack()

fetch_joke_button = tk.Button(window, text = "Incearca o gluma noua", command = fetch_new_joke)
fetch_joke_button.pack()

window.mainloop()