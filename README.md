**README.md**

# Quote Generator

This is a simple Python application that generates random quotes from the Quotable API.

**Dependencies:**
* `requests`
* `tkinter`
* `ttkbootstrap`

**Usage:**
1. Install the required dependencies:
```bash
pip install requests ttkbootstrap
```

2. Run the application:
```bash
python quote_generator.py
```

**Features:**
* Retrieves random quotes from the Quotable API.
* Displays the quote and author in a tkinter window.
* Provides a "Get Quote" button to refresh the quote.

**Code Breakdown:**

1. Import the necessary libraries: `requests`, `tkinter`, and `ttkbootstrap`.

2. Define the URL of the Quotable API endpoint: `URL = "https://api.quotable.io/random"`.

3. Define a function `fetch_quote()` that makes a GET request to the Quotable API, parses the JSON response, and returns a tuple containing the quote and author.

4. Define a function `update_quote()` that calls the `fetch_quote()` function to retrieve a new quote and author, and updates the `quote_label` and `author_label` with the new information.

5. Create a tkinter main window using the `ttk.Window()` constructor and set its title, geometry, and theme.

6. Create a tkinter frame using the `ttk.Frame()` constructor and pack it into the main window.

7. Create a tkinter label using the `ttk.Label()` constructor to display the quote and pack it into the frame.

8. Create another tkinter label using the `ttk.Label()` constructor to display the author and pack it into the frame.

9. Create a tkinter button using the `ttk.Button()` constructor, set its text to "Get Quote", and bind its `command` event to the `update_quote()` function. Pack the button into the frame.

10. Start the tkinter main loop using the `root.mainloop()` method.