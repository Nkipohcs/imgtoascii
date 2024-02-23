import tkinter as tk
from tkinter import filedialog, ttk, PhotoImage
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import signal

def image_to_ascii(image, new_width):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
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

def close_app():
    app.destroy()

def convert_text_to_ascii(text):
    ascii_art_dict = {
        'A': ["  ___  ", " / _ \ ", "/ /_\ \\", "|  _  |", "| | | |", "\\_| |_/", "       "],
        'B': ["______ ", "| ___ \\", "| |_/ /", "| ___ \\", "| |_/ /", "\\____/ ", "       "],
        'C': [" _____ ", "/  __ \\", "| /  \\/", "| |    ", "| \\__/\\", " \\____/", "       "],
        'D': ["______ ", "|  _  \\", "| | | |", "| | | |", "| |/ / ", "|___/  ", "       "],
        'E': [" _____ ", "|  ___|", "| |__  ", "|  __| ", "| |___ ", "\\____/ ", "       "],
        'F': ["______ ", "|  ___|", "| |_   ", "|  _|  ", "| |    ", "\\_|    ", "       "],
        'G': [" _____ ", "|  __ \\", "| |  \\/", "| | __ ", "| |_\\ \\", " \\____/", "       "],
        'H': [" _   _ ", "| | | |", "| |_| |", "|  _  |", "| | | |", "\\_| |_/", "       "],
        'I': [" _____ ", "|_   _|", "  | |  ", "  | |  ", " _| |_ ", " \\___/ ", "       "],
        'J': ["   ___ ", "  |_  |", "    | |", "    | |", "/\\__/ /", "\\____/ ", "       "],
        'K': [" _   __", "| | / /", "| |/ / ", "|    \\ ", "| |\\  \\", "\\_| \\_/", "       "],
        'L': [" _     ", "| |    ", "| |    ", "| |    ", "| |____", "\\_____/","       "],
        'M': ["___  ___", "|  \\/  |", "| .  . |", "| |\\/| |", "| |  | |", "\\_|  |_/", "       "],
        'N': [" _   _ ", "| \\ | |", "|  \\| |", "| . ` |", "| |\\  |", "\\_| \\_/", "       "],
        'O': [" _____ ", "|  _  |", "| | | |", "| | | |", "\\ \\_/ /", " \\___/ ", "       "],
        'P': ["______ ", "| ___ \\", "| |_/ /", "|  __/ ", "| |    ", "\\_|    ", "       "],
        'Q': [" _____ ", "|  _  |", "| | | |", "| | | |", "\\ \\/' /", " \\_/\\_\\", "       "],
        'R': ["______ ", "| ___ \\", "| |_/ /", "|    / ", "| |\\ \\ ", "\\_| \\_|", "       "],
        'S': [" _____ ", "/  ___|", "\\ `--. ", " `--. \\", "/\\__/ /", "\\____/ ", "       "],
        'T': [" _____ ", "|_   _|", "  | |  ", "  | |  ", "  | |  ", "  \\_/  ", "       "],
        'U': [" _   _ ", "| | | |", "| | | |", "| | | |", "| |_| |", " \\___/ ", "       "],
        'V': ["__     __", "\\ \\   / /", " \\ \\ / / ", "  \\   /  ", "   \\ /   ", "    V    ", "         "],
        'W': [" _    _ ", "| |  | |", "| |  | |", "| |/\\| |", "\\  /\\  /", " \\/  \\/ ", "       "],
        'X': ["__   __", "\\ \\ / /", " \\ V / ", " /   \\ ", "/ /^\\ \\", "\\/   \\/", "       "],
        'Y': ["__   __", "\\ \\ / /", " \\ V / ", "  \\ /  ", "  | |  ", "  \\_/  ", "       "],
        'Z': ["______", "|___ /", "   / /", "  / / ", " / /  ", "/____|", "      "],
        '0': ["  ___  ", " / _ \\ ", "| | | |", "| | | |", "| |_| |", " \\___/ ", "       "],
        '1': [" __ ", "/_ |", " | |", " | |", " | |", " |_|", "    "],
        '2': [" _____  ", "/___  \\ ", "   /  / ", "  /  /_ ", " /_____|", "        ", "        "],
        '3': [" _____ ", "|___ / ", "  |_ \\ ", " ___) |", "|____/ ", "       ", "       "],
        '4': [" _  _   ", "| || |  ", "| || |_ ", "|__   _|", "   |_|  ", "        ", "       "],
        '5': [" ____  ", "| ___| ", "|___ \\ ", " ___) |", "|____/ ", "       ", "       "],
        '6': ["  __   ", " / /_  ", "| '_ \\ ", "| (_) |", " \\___/ ", "      ", "     "],
        '7': [" ______ ", "|____  |", "    / / ", "   / /  ", "  /_/   ", "       ", "      "],
        '8': ["  ___  ", " ( _ ) ", " / _ \\ ", "| (_) |", " \\___/ ", "      ", "     "],
        '9': ["  ___  ", " / _ \\ ", "| (_) |", " \\__, |", "   /_/ ", "      ", "     "],
        '?': [" _____", "|  __ \\ ", "| |  \\/", "| | __ ", "| |_\\ \\", " \\____/", "       "],
        '!': [" _ ", "| |", "| |", "|_|", "(_)", "   ", "   "],    
        '+': ["       ", "   _   ", " _| |_ ", "|_   _|", "  |_|  ", "       ", "       "],
        '@': ["  ____  ", " / __ \\ ", "| |  | |", "| |  | |", "| |__| |", " \\____/ ", "        "],
        '#': ["   _  _   ", " _| || |_ ", "|_  __  _|", " _| || |_ ", "|_  __  _|", "  |_||_|  ", "          "],
        '$': ["  _  ", " | | ", "/ __)", "\\__ \\", "(   /", " |_| ", "     "],
        '%': [" _   __", "(_) / /", "   / / ", "  / /  ", "/_/   ", "      ", "      "],
        '^': [" /\\ ", "|/\\|", "    ", "    ", "    ", "    ", "    "],
        '&': ["  ___  ", " ( _ ) ", " / _ \\/\\", "| (_>  <", " \\___/\\/", "        ", "        "],
        '*': ["    _    ", " /\\| |/\\ ", " \\ ` ' / ", "|_     _|", " / , . \\ ", " \\/|_|\\/ ", "         "],
        '(': ["  __", " / /", "| | ", "| | ", "| | ", " \\_\\", "    "],
        ')': ["__  ", "\\ \\ ", " | |", " | |", " | |", "/_/ ", "    "],
        '-': ["       ", "       ", " _____ ", "|_____|", "       ", "       ", "       "],
        '_': ["       ", "       ", "       ", "       ", "       ", " _____ ", "|_____|"],
        '=': ["       ", " _____ ", "|_____|", "|_____|", "       ", "       ", "       "],
        '[': [" ___ ", "|  _|", "| |  ", "| |  ", "| |  ", "| |_ ", " \\__|"],
        ']': [" ___ ", "|_  |", "  | |", "  | |", "  | |", " _| |", "|___|"],
        '{': ["  __", " / /", "| | ", "< < ", "| | ", " \\_\\", "    "],
        '}': ["__  ", "\\ \\ ", " | |", " > >", " | |", "/_/ ", "    "],
        '|': [" _ ", "| |", "| |", "| |", "| |", "| |", "|_|"],
        ';': [" _ ", "(_)", " _ ", "| |", "| |", "| |", "|_|"],
        ' ': [
        "         ",  # 9 espaces
        "         ",  # 9 espaces
        "         ",  # 9 espaces
        "         ",  # 9 espaces
        "         ",  # 9 espaces
        "         ",  # 9 espaces
        "         ",  # 9 espaces
    ],
    }
    
    ascii_art_lines = [""] * 7  # Chaque lettre est représentée sur 7 lignes
    for char in text.upper():  # Convertit le texte en majuscules
        if char in ascii_art_dict:
            for i, line in enumerate(ascii_art_dict[char]):
                ascii_art_lines[i] += line + " "  # Ajoute 1 espaces entre les lettres
    return "\n".join(ascii_art_lines)

def generate_ascii_art(event=None):
    input_text = text_entry.get()
    selected_style = style_var.get()
    ascii_art_result = convert_text_to_ascii(input_text)
    ascii_art.set(ascii_art_result)




for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP, signal.SIGQUIT):
    signal.signal(sig, lambda signum, frame: close_app())

app = TkinterDnD.Tk()
app.title("Convertisseur d'image en ASCII")
icon = PhotoImage(file='img/logo.png')
app.iconphoto(True, icon)
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

text_entry_frame = tk.Frame(app)
text_entry_frame.pack(side=tk.TOP, fill=tk.X)

text_entry_label = tk.Label(text_entry_frame, text="Entrez votre texte :")
text_entry_label.pack(side=tk.LEFT, padx=5, pady=5)

text_entry = tk.Entry(text_entry_frame)
text_entry.pack(side=tk.LEFT, padx=5, pady=5)
text_entry.bind("<Return>", generate_ascii_art)

styles = ["Style 1", "Style 2", "Style 3", "...", "Style 50"]
style_var = tk.StringVar(value=styles[0])
style_menu = ttk.Combobox(text_entry_frame, textvariable=style_var, values=styles)
style_menu.pack(side=tk.LEFT, padx=5, pady=5)

generate_button = tk.Button(text_entry_frame, text="Générer", command=generate_ascii_art)
generate_button.pack(side=tk.LEFT, padx=5, pady=5)

app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', drop)
app.mainloop()

