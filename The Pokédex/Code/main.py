import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from audioplayer import AudioPlayer

window = tk.Tk()
window.iconbitmap(r"Assets/PokeballIcon.ico")
window.geometry("600x600")
window.title("The Pokédex Ver. 1.2")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="The Pokédex")
title_label.config(font=("Arial", 32, "bold"))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_size = tk.Label(window)
pokemon_size.config(font=("Arial", 20))
pokemon_size.pack(padx=10, pady=10)

shiny_sprite = "default"


def load_pokemon():
    try:
        pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

        http = urllib3.PoolManager()
        response = http.request("GET", pokemon.sprites.front.get(shiny_sprite))
        image = PIL.Image.open(BytesIO(response.data))

        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=img)
        pokemon_image.image = img

        pokemon_information.config(
            text=f"ID: {pokemon.dex} | Name: {pokemon.name.title()}")

        pokemon_types.config(text="Type: " + " & ".join(
            [t for t in pokemon.types]).title())

        pokemon_size.config(
            text=f"Weight: {round(pokemon.weight / 4.536, 1)} lbs. | Height: {pokemon.height * 10} cm.")

        text_id_name.delete(1.0, tk.END)

        AudioPlayer(
            "Assets/soundeffect1.mp3").play(block=True)
    except:
        pokemon_image.image = None

        pokemon_information.config(
            text=f"Pokémon: \"{text_id_name.get(1.0, 'end-1c')}\" not found.")

        pokemon_types.config(
            text=" ")

        pokemon_size.config(
            text=" ")

        text_id_name.delete(1.0, tk.END)

        AudioPlayer(
            "Assets/soundeffect2.mp3").play(block=True)


label_id_name = tk.Label(
    window, text="Enter the ID or Name of a Pokémon!")
label_id_name.config(font=("Arial", 20, "italic"))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

button_load = tk.Button(
    window, text="Search For Pokémon", command=load_pokemon)
button_load.config(font=("Arial", 20))
button_load.pack(padx=10, pady=10)


def configure_shiny():
    global shiny_sprite

    if shiny_sprite == "shiny":
        button_shiny.config(text="Shiny Sprite OFF")
        shiny_sprite = "default"

    else:
        button_shiny.config(text="Shiny Sprite ON")
        shiny_sprite = "shiny"


button_shiny = tk.Button(
    window, text="Shiny Sprite OFF", command=configure_shiny)
button_shiny.config(font=("Arial", 20))
button_shiny.pack(side="bottom", padx=5, pady=5)

window.mainloop()
