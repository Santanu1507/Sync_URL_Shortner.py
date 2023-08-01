import tkinter as tk
from tkinter import ttk
import requests
import pyperclip

# Function to shorten a given URL using the TinyURL API
def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        if response.ok:
            return response.text
        else:
            print("Error:", response.status_code, response.text)
            return None
    except requests.RequestException as e:
        print("Error:", e)
        return None

# Function to handle the "Shorten URL" button click event
def shorten_button_click():
    long_url = url_entry.get()
    if long_url:
        shortened_url = shorten_url(long_url)
        if shortened_url:
            # If the URL is successfully shortened, update the result labels and enable the copy button
            result_label.config(text="Shortened URL :")
            result_display.config(text=shortened_url)
            copy_button.config(state=tk.NORMAL)
        else:
            # If there's an error while shortening the URL, display an error message and disable the copy button
            result_label.config(text="Error: Unable to shorten URL.")
            result_display.config(text="")
            copy_button.config(state=tk.DISABLED)
    else:
        # If no URL is entered, display an error message and disable the copy button
        result_label.config(text="Error: Please enter a valid URL.")
        result_display.config(text="")
        copy_button.config(state=tk.DISABLED)

# Function to copy the shortened URL to the clipboard
def copy_shortened_url():
    shortened_url = result_display.cget("text")
    if shortened_url:
        pyperclip.copy(shortened_url)

# Create the main Tkinter window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("480x250")

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")

# Create and configure the ttk style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground="black", background="white", font=("Helvetica", 12))
style.configure("TButton", foreground="black", background="yellow", font=("Helvetica", 12))

# Create and pack widgets for the application

# URL entry
url_label = ttk.Label(root, text="Enter URL to shorten :")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# "Shorten URL" button
shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_button_click)
shorten_button.pack(pady=10)

# Result labels for displaying the shortened URL or error message
result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

result_display = ttk.Label(root, text="", wraplength=350)
result_display.pack(pady=10)

# Copy button with Unicode icon for copying the shortened URL
copy_icon_unicode = "\u2398"
copy_button = ttk.Button(root, text=copy_icon_unicode, command=copy_shortened_url, state=tk.DISABLED)
copy_button.pack(pady=5)

# Start the Tkinter main event loop
root.mainloop()
