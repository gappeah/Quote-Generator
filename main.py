import requests
import tkinter as ttk
import ttkbootstrap as ttk

URL = "https://api.quotable.io/random"

root = ttk.Window(themename="pulse")
root.title("Quote Generator")
root.geometry("700x250")

frame = ttk.Frame(root)
frame.pack(padx=30, pady=40)

quote_label = ttk.Label(frame, text="Quote", font=("Helvetica", 16))