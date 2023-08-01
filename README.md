# URL Shortener Application

This is a simple URL Shortener application built using Python and Tkinter. The application utilizes the TinyURL API to generate shortened URLs for long URLs provided by the user.

## Features

- Generate a shortened URL for a long URL using the TinyURL API.
- Display the shortened URL to the user.
- Copy the shortened URL to the clipboard for easy sharing.

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- ttk library (part of the tkinter package)
- requests library (for making HTTP requests to the TinyURL API)
- pyperclip library (for copying the shortened URL to the clipboard)

## Usage

1. Run the `url_shortener.py` file to start the application.
2. Enter the long URL in the provided input field.
3. Click the "Shorten URL" button to generate a shortened URL using the TinyURL API.
4. The shortened URL will be displayed below the input field.
5. Click the copy icon button next to the shortened URL to copy it to the clipboard for sharing.

## How It Works

The application uses the Tkinter library to create a graphical interface with input fields, buttons, and labels. The `shorten_url()` function sends a request to the TinyURL API with the long URL provided by the user to get the shortened URL.

When the "Shorten URL" button is clicked, the application calls the `shorten_button_click()` function. This function retrieves the long URL from the input field, calls the `shorten_url()` function to get the shortened URL, and updates the result labels accordingly.

The `copy_shortened_url()` function is triggered when the user clicks the copy icon button. This function retrieves the shortened URL from the result label and copies it to the clipboard using the `pyperclip` library.

## Future Improvements

- Implement error handling for invalid URLs or failed API requests.
- Add support for more URL shortening services.
- Improve the user interface with more styling options and feedback messages.
