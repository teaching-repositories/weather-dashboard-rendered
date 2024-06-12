import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualise_data import create_forecast_card, plot_scatter, plot_min_max
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from utils import determine_weather


def update_weather(city_var, plot_frame):
    """
    Fetch and update the weather data for the selected city, then update the plots in the dashboard.

    Args:
        city_var (tk.StringVar): A Tkinter StringVar containing the selected city name.
        plot_frame (ttk.Frame): A Tkinter frame where the plots will be displayed.
    """
    city = city_var.get()
    api_key = 'd0de46031ad7410d0c72c6063690e1d0'  # Replace with your OpenWeatherMap API key
    current_data, forecast_data = fetch_weather_data(api_key, city)
    current_df, hourly_df, daily_df = process_weather_data(current_data, forecast_data)
    daily_df['Weather'] = daily_df.apply(determine_weather, axis=1, args=(25, 15, 80))

    for widget in plot_frame.winfo_children():
        widget.destroy()

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    fig.tight_layout(pad=5.0)

    # Generate plots
    create_forecast_card(axs[0], daily_df.iloc[0]['Date'], daily_df.iloc[0]['Max Temperature (C)'], daily_df.iloc[0]['Min Temperature (C)'], daily_df.iloc[0]['Weather'])
    plot_scatter(hourly_df, 'Temperature (C)', 'Wind Speed (m/s)', axs[1], title="Wind Speed vs Temperature")
    plot_min_max(daily_df, 'Date', 'Min Temperature (C)', 'Max Temperature (C)', axs[2], title="Daily Min/Max Temperature")

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def create_dashboard(root):
    """
    Create the weather dashboard GUI.

    Args:
        root (tk.Tk): The root Tkinter window.
    """
    # Create a frame for the controls
    control_frame = ttk.Frame(root, padding="10")
    control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # Create a frame for the plots
    plot_frame = ttk.Frame(root, padding="10")
    plot_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Dropdown for city selection
    city_var = tk.StringVar(value='Sydney')
    city_dropdown = ttk.Combobox(control_frame, textvariable=city_var, values=['Sydney', 'New York', 'London', 'Beijing'])
    city_dropdown.grid(row=0, column=0, padx=5, pady=5)

    # Button to fetch and update weather data
    update_button = ttk.Button(control_frame, text="Update Weather", command=lambda: update_weather(city_var, plot_frame))
    update_button.grid(row=0, column=1, padx=5, pady=5)

    # Configure row and column weights
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    plot_frame.grid_rowconfigure(0, weight=1)
    plot_frame.grid_columnconfigure(0, weight=1)

    # Initialize the weather data
    update_weather(city_var, plot_frame)
