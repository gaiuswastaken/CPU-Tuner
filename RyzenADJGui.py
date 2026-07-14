import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("CPU Tuner")
window.geometry("960x480")

# Title
title_label = ttk.Label(master=window, text="CPU Parameters", font = "sans-serif 75")
title_label.pack()

# Main Loop
window.mainloop()