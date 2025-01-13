import tkinter as tk

class RoundedButton:
    def __init__(self, canvas, text, x, y, width, height, radius, bg_color='green', fg_color='yellow', font=('Arial', 12), command=None, hover_color = 'lightgreen', hover_text_color = 'black', click_color = 'darkgreen', click_text_color = 'white'):
        self.canvas = canvas
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font = font
        self.command = command
        self.hover_color = hover_color
        self.hover_text_color = hover_text_color
        self.click_color = click_color
        self.click_text_color = click_text_color
        
        self.create_button()

    def create_button(self):
        # Draw the button shapes without borders
        self.left_circle = self.canvas.create_oval(
            self.x - self.radius, self.y,
            self.x + self.radius, self.y + self.height,
            fill=self.bg_color, outline=""
        )
        self.right_circle = self.canvas.create_oval(
            self.x + self.width - self.radius, self.y,
            self.x + self.width + self.radius, self.y + self.height,
            fill=self.bg_color, outline=""
        )
        self.rectangle = self.canvas.create_rectangle(
            self.x, self.y,
            self.x + self.width, self.y + self.height,
            fill=self.bg_color, outline=""
        )

        # Create the button with activebackground set
        self.button = tk.Button(
            self.canvas, text=self.text,
            bg=self.bg_color, fg=self.fg_color,
            font=self.font, borderwidth=0,
            command=self.command,
            activebackground=self.click_color,  # Set active background color
            cursor="hand2"  # Change cursor to pointer
        )
        self.button.place(x=self.x, y=self.y, width=self.width, height=self.height + 2)

        # Bind hover and click events
        self.button.bind("<Enter>", self.on_hover)
        self.button.bind("<Leave>", self.on_leave)
        self.button.bind("<ButtonPress>", self.on_click)

    def on_hover(self, event):
        self.change_color(self.hover_color)
        self.button.config(fg=self.hover_text_color)

    def on_leave(self, event):
        self.change_color(self.bg_color)
        self.button.config(fg=self.fg_color)

    def on_click(self, event):
        self.change_color(self.click_color)
        self.button.config(fg=self.click_text_color)

    def change_color(self, color):
        self.button.config(bg=color)
        self.canvas.itemconfig(self.left_circle, fill=color)
        self.canvas.itemconfig(self.right_circle, fill=color)
        self.canvas.itemconfig(self.rectangle, fill=color)