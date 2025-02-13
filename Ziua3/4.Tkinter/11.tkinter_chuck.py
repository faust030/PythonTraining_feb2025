import tkinter as tk
import requests
import json

LINK = "https://api.chucknorris.io/jokes/search"
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

    search_term = input_field.get()

    response = requests.get(LINK, headers = parameti, params={"query" : search_term})
    json_response = json.loads(response.text)
    print(json_response)
    result = json_response["result"]
    if result:
        joke = result[0]["value"]
        joke_label.config(text = joke)
    else:
        joke_label.config(text = "Nu este nicio gluma")



input_field = tk.Entry(window)
input_field.pack()


joke_label = tk.Label(window, text = "Aici va fi gluma")
joke_label.pack()

fetch_joke_button = tk.Button(window, text = "Incearca o gluma noua", command = fetch_new_joke)
fetch_joke_button.pack()

window.mainloop()