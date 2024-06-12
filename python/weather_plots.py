import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def plot_current_weather_table(current_data, ax):
    """
    Plot the current weather table.

    Parameters:
    current_data (DataFrame): The current weather data.
    ax (Axes): The matplotlib axes on which to plot.
    """
    ax.axis('off')
    ax.table(cellText=current_data.values, colLabels=current_data.columns, cellLoc='center', loc='center')
    ax.set_title('Current Weather Data')


def plot_weather_pie_chart(hourly_data, ax):
    """
    Plot a pie chart showing the proportion of different weather descriptions.

    Parameters:
    hourly_data (DataFrame): The hourly weather data.
    ax (Axes): The matplotlib axes on which to plot.
    """
    weather_counts = hourly_data['Weather'].value_counts()
    ax.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    ax.set_title('Proportion of Weather Descriptions')


def plot_trend(data, time_column, value_column, ax, title="Trend"):
    """
    Plot the trend of a specific value over time.

    Parameters:
    data (DataFrame): The data containing the time and value columns.
    time_column (str): The name of the time column.
    value_column (str): The name of the value column.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    """
    ax.plot(data[time_column], data[value_column], marker='o', linestyle='-', linewidth=1, color='tab:blue', label=value_column)
    z = np.polyfit(data.index, data[value_column], 1)
    p = np.poly1d(z)
    ax.plot(data[time_column], p(data.index), "r--", label='Trendline', linewidth=2)
    ax.set_xlabel(time_column)
    ax.set_ylabel(value_column)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)


def plot_scatter(data, x_column, y_column, ax, title="Scatter Plot"):
    """
    Plot a scatter plot of two variables.

    Parameters:
    data (DataFrame): The data containing the x and y columns.
    x_column (str): The name of the x column.
    y_column (str): The name of the y column.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    """
    ax.scatter(data[x_column], data[y_column], color='blue', alpha=0.6, edgecolors='w', linewidth=0.5, label='Data Points')
    z = np.polyfit(data[x_column], data[y_column], 1)
    p = np.poly1d(z)
    ax.plot(data[x_column], p(data[x_column]), "r--", label='Best Fit Line', linewidth=2)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)


def plot_min_max(data, date_column, min_column, max_column, ax, title="Min/Max Plot"):
    """
    Plot the minimum and maximum values over time.

    Parameters:
    data (DataFrame): The data containing the date, min, and max columns.
    date_column (str): The name of the date column.
    min_column (str): The name of the minimum value column.
    max_column (str): The name of the maximum value column.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    """
    ax.bar(data[date_column], data[min_column], width=0.4, label=f'Min {min_column}', color='tab:blue', align='center')
    ax.bar(data[date_column] + pd.Timedelta(days=0.4), data[max_column], width=0.4, label=f'Max {max_column}', color='tab:red', align='center')
    z_min = np.polyfit(data.index, data[min_column], 1)
    p_min = np.poly1d(z_min)
    z_max = np.polyfit(data.index, data[max_column], 1)
    p_max = np.poly1d(z_max)
    ax.plot(data[date_column], p_min(data.index), "b--", label=f'Min {min_column} Trendline')
    ax.plot(data[date_column] + pd.Timedelta(days=0.4), p_max(data.index), "r--", label=f'Max {max_column} Trendline')
    ax.set_xlabel(date_column)
    ax.set_ylabel('Value')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)


def plot_histogram(data, column, ax, title="Histogram", xlabel=None, ylabel="Frequency", bins=20, color='tab:blue'):
    """
    Plot a histogram of a specific column.

    Parameters:
    data (DataFrame): The data containing the column to plot.
    column (str): The name of the column to plot.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    bins (int): The number of bins in the histogram.
    color (str): The color of the histogram bars.
    """
    ax.hist(data[column], bins=bins, color=color, alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else column)
    ax.set_ylabel(ylabel)
    ax.grid(True)


def plot_box_plot(data, column, ax, title="Box Plot"):
    """
    Plot a box plot of a specific column.

    Parameters:
    data (DataFrame): The data containing the column to plot.
    column (str): The name of the column to plot.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    """
    ax.boxplot(data[column])
    ax.set_title(title)
    ax.set_ylabel(column)
    ax.grid(True)


def plot_box_plots(data, columns, ax, title="Box Plot"):
    """
    Plot multiple box plots for specified columns.

    Parameters:
    data (DataFrame): The data containing the columns to plot.
    columns (list of str): The names of the columns to plot.
    ax (Axes): The matplotlib axes on which to plot.
    title (str): The title of the plot.
    """
    ax.boxplot([data[column] for column in columns], labels=columns)
    ax.set_title(title)
    ax.grid(True)


def plot_correlation_heatmap(data, columns, ax):
    """
    Plot a correlation heatmap for specified columns.

    Parameters:
    data (DataFrame): The data containing the columns to plot.
    columns (list of str): The names of the columns to include in the correlation heatmap.
    ax (Axes): The matplotlib axes on which to plot.
    """
    correlation_matrix = data[columns].corr()
    cax = ax.matshow(correlation_matrix, cmap='coolwarm')
    fig.colorbar(cax)
    ticks = list(range(len(columns)))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(columns)
    ax.set_yticklabels(columns)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="left", rotation_mode="anchor")
    for i in range(len(columns)):
        for j in range(len(columns)):
            ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', ha='center', va='center', color='white')
    ax.set_title('Correlation Matrix Heatmap')


def create_forecast_card(ax, date, high_temp, low_temp, weather):
    """
    Create a forecast card displaying weather information.

    Parameters:
    ax (Axes): The matplotlib axes on which to plot.
    date (datetime): The date of the forecast.
    high_temp (float): The high temperature for the day.
    low_temp (float): The low temperature for the day.
    weather (str): The weather condition (e.g., 'Sunny', 'Rainy', 'Partly Cloudy').
    """
    # Background color based on weather
    if weather == 'Sunny':
        bg_color = 'gold'
    elif weather == 'Partly Cloudy':
        bg_color = 'lightgrey'
    elif weather == 'Rainy':
        bg_color = 'lightblue'
    else:
        bg_color = 'white'

    # Create a rectangle patch for the background color
    rect = patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color=bg_color, zorder=0)
    ax.add_patch(rect)

    ax.axis('off')  # Hide axes

    # Display date
    ax.text(0.5, 0.8, date.strftime('%Y-%m-%d'), fontsize=12, ha='center', va='center')
    # Display high temperature
    ax.text(0.5, 0.6, f'High: {high_temp}°C', fontsize=10, ha='center', va='center', color='red')
    # Display low temperature
    ax.text(0.5, 0.4, f'Low: {low_temp}°C', fontsize=10, ha='center', va='center', color='blue')
    # Display weather condition
    ax.text(0.5, 0.2, weather, fontsize=10, ha='center', va='center')
