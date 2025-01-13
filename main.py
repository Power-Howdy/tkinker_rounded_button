import tkinter as tk
from RoundedButton import RoundedButton

# Create the main window
root = tk.Tk()
root.title("Rounded Button Example")

# Create a canvas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Create a rounded button
rounded_button = RoundedButton(canvas, "Click Me", 50, 50, 200, 50, 20, command=lambda: print("Button clicked"))  # Instantiate RoundedButton


# Start the Tkinter event loop
root.mainloop()