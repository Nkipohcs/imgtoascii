import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

def image_to_ascii(image, new_width):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    width, height = image.size
    aspect_ratio = height / width
    new_height = aspect_ratio * new_width * 0.55
    resized_image = image.resize((new_width, int(new_height)))
    grayscale_image = resized_image.convert("L")
    pixels = grayscale_image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i+new_width] + "\n"
    return ascii_img


def update_ascii_art(*args):
    if current_image:
        width = ascii_width_slider.get()
        ascii_art.set(image_to_ascii(current_image, width))

def open_image(file_path=None):
    global current_image
    if file_path is None: 
        file_path = filedialog.askopenfilename()
    if file_path:
        current_image = Image.open(file_path)
        update_ascii_art()

def drop(event):
    file_path = event.data
    if file_path:
        open_image(file_path)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(ascii_art.get())

app = TkinterDnD.Tk()
app.title("Convertisseur d'image en ASCII")

button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, fill=tk.X)

ascii_art = tk.StringVar()

open_button = tk.Button(button_frame, text="Importer une image", command=lambda: open_image(None))
open_button.pack(side=tk.LEFT, padx=5, pady=5)

copy_button = tk.Button(button_frame, text="Copier dans le presse-papier", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5, pady=5)

ascii_width_slider = tk.Scale(button_frame, from_=30, to_=200, orient=tk.HORIZONTAL, label="Largeur ASCII")
ascii_width_slider.set(100)  # Valeur par défaut
ascii_width_slider.pack(side=tk.LEFT, padx=5, pady=5)
ascii_width_slider.bind("<ButtonRelease-1>", lambda event: update_ascii_art())

status_label = tk.Label(button_frame, text="", fg="red")
status_label.pack(side=tk.LEFT, padx=5, pady=5)

ascii_text = tk.Label(app, textvariable=ascii_art, font=("Courier", 8), justify=tk.LEFT)
ascii_text.pack(expand=True)

app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', drop)

app.mainloop()
