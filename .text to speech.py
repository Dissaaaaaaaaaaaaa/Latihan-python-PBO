import tkinter as tk
from tkinter import Label, Entry, Button, filedialog
from gtts import gTTS
import os
import pygame

def convert_to_speech():
    text = entry_text.get()
    language = 'id'  # You can change the language code as needed

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Delete old audio files
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

        # Save the audio file
        tts.save("output.mp3")

        # Play the saved audio file
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

    except Exception as e:
        print(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Get the window size
window_width = 300
window_height = 150

# Calculate the center position of the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create widgets
label_instruction = Label(root, text="Enter text to convert:")
entry_text = Entry(root, width=50)
button_convert = Button(root, text="Convert to Speech", command=convert_to_speech)

# Place widgets on the window
label_instruction.pack(pady=10)
entry_text.pack(pady=10)
button_convert.pack(pady=10)

# Start the GUI event loop
root.mainloop()