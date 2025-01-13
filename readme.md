# TKinter Rounded Button

This is a Python script that creates a button with rounded corners using the Tkinter library. The button has a custom background color and text color.

## Usage

To use the `RoundedButton`, you need to have the `RoundedButton` class defined in a separate file (e.g., `RoundedButton.py`). 

### Example

Here is a simple example of how to create a rounded button in your Tkinter application:
```python
import tkinter as tk
from RoundedButton import RoundedButton
```

Create the main window
```python
root = tk.Tk()
root.title("Rounded Button Example")
```
Create a canvas
```python
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()
```
Create a rounded button
```python
rounded_button = RoundedButton(canvas, "Click Me", 50, 50, 200, 50, 20, command=lambda: print("Button clicked"))
```
Start the Tkinter event loop
```python
root.mainloop()
```