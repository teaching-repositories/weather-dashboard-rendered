import tkinter as tk
from tkinter import ttk
from create_dashboard import create_dashboard

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")

# Create the dashboard
create_dashboard(root)

# Start the Tkinter event loop
root.mainloop()
