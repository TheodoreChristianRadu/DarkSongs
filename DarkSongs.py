from customtkinter import *
from PIL import Image
import json
import Music
import Input

window = CTk()
window.title("Dark Songs")
window.iconbitmap("Icon.ico")

with open("Configuration.json") as file:
    configuration = json.load(file)
mappings = {tone: StringVar(value=configuration["Mappings"].get(tone, "Nothing")) for tone in Music.tones}
options = {name: StringVar(value=value) for name, value in configuration["Options"].items()}

left = CTkFrame(master=window, fg_color='transparent')
left.pack(side=LEFT, fill=Y, pady=5)

actions = list(Input.actions["Actions"].keys())
for index, (tone, mapping) in enumerate(mappings.items()):
    left.rowconfigure(index, weight=1, minsize=35)
    CTkLabel(master=left, text=tone).grid(row=index, column=0, padx=10)
    CTkOptionMenu(master=left, width=150, values=actions, variable=mapping).grid(row=index, column=1, padx=(0, 5))

right = CTkFrame(master=window, fg_color='transparent')
right.pack(side=RIGHT, fill=Y, pady=5)

for index, (name, variable) in enumerate(options.items()):
    CTkLabel(master=right, text=name).grid(row=index, column=0, padx=5, pady=(0, 5))
    CTkEntry(master=right, textvariable=variable).grid(row=index, column=1, padx=(0, 5), pady=(0, 5))

index += 1
right.rowconfigure(index, weight=1, minsize=70)
detected = CTkLabel(master=right, text="Tone", font=("Constantia", 48))
detected.grid(row=index, columnspan=2, sticky='s', padx=15)
index += 1
right.rowconfigure(index, weight=1, minsize=50)
result = CTkLabel(master=right, text="Action", font=("Constantia", 28))
result.grid(row=index, columnspan=2, sticky='n', padx=10)

index += 1
def process(note, tone):
    if tone in mappings:
        detected.configure(text=tone)
        result.configure(text=mappings[tone].get())
        Input.perform(mappings[tone].get())
def start():
    try:
        duration = float(options["Note Duration"].get())
        fundamental = float(options["Fundamental Frequency"].get())
        volume = float(options["Output Volume"].get())
        Music.Player(process, duration, fundamental, volume)
    except ValueError: pass
CTkButton(master=right, text="Start", command=start).grid(row=index, column=1, sticky='s', padx=(0, 5))
def stop():
    Music.Player.stop()
CTkButton(master=right, text="Stop", command=stop).grid(row=index, column=0, sticky='s', padx=5)

image = CTkImage(Image.open("Image.png"), size=(390, 715))
CTkLabel(master=window, image=image, text="").pack(side=BOTTOM)

window.mainloop()

configuration["Mappings"] = {tone: action.get() for tone, action in mappings.items()}
configuration["Options"] = {name: value.get() for name, value in options.items()}
with open("Configuration.json", "w") as file:
    json.dump(configuration, file, indent=4)
