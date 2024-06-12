import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def plot_current_weather_table(current_data, ax):
    """
    Plot a table displaying the current weather data.

    Args:
        current_data (pd.DataFrame): DataFrame containing current weather data.
        ax (matplotlib.axes.Axes): Axes object to draw the table on.
    """
    ax.axis('off')
    ax.table(cellText=current_data.values, colLabels=current_data.columns, cellLoc='center', loc='center')
    ax.set_title('Current Weather Data')


def plot_weather_pie_chart(hourly_data, ax):
    """
    Plot a pie chart showing the proportion of different weather descriptions.

    Args:
        hourly_data (pd.DataFrame): DataFrame containing hourly weather data with a 'Weather' column.
        ax (matplotlib.axes.Axes): Axes object to draw the pie chart on.
    """
    weather_counts = hourly_data['Weather'].value_counts()
    ax.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    ax.set_title('Proportion of Weather Descriptions')


def plot_trend(data, time_column, value_column, ax, title="Trend"):
    """
    Plot a trend line of a specified value over time.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        time_column (str): Name of the column containing time data.
        value_column (str): Name of the column containing the values to plot.
        ax (matplotlib.axes.Axes): Axes object to draw the plot on.
        title (str): Title of the plot.
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
    Plot a scatter plot with a best fit line.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        x_column (str): Name of the column for the x-axis values.
        y_column (str): Name of the column for the y-axis values.
        ax (matplotlib.axes.Axes): Axes object to draw the scatter plot on.
        title (str): Title of the plot.
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
    Plot the minimum and maximum values over time with trendlines.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        date_column (str): Name of the column containing date data.
        min_column (str): Name of the column containing minimum values.
        max_column (str): Name of the column containing maximum values.
        ax (matplotlib.axes.Axes): Axes object to draw the plot on.
        title (str): Title of the plot.
    """
    width = 0.3  # Width of the bars
    dates = pd.to_datetime(data[date_column])

    # Plot min values
    ax.bar(dates - pd.Timedelta(days=width/2), data[min_column], width=width, label=f'Min {min_column}', color='tab:blue', align='center')

    # Plot max values
    ax.bar(dates + pd.Timedelta(days=width/2), data[max_column], width=width, label=f'Max {max_column}', color='tab:red', align='center')

    # Calculate trendlines
    z_min = np.polyfit(data.index, data[min_column], 1)
    p_min = np.poly1d(z_min)
    z_max = np.polyfit(data.index, data[max_column], 1)
    p_max = np.poly1d(z_max)

    # Plot trendlines
    ax.plot(dates, p_min(data.index), "b--", label=f'Min {min_column} Trendline')
    ax.plot(dates, p_max(data.index), "r--", label=f'Max {max_column} Trendline')

    # Set labels and title
    ax.set_xlabel(date_column)
    ax.set_ylabel('Value')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)


def plot_histogram(data, column, ax, title="Histogram", xlabel=None, ylabel="Frequency", bins=20, color='tab:blue'):
    """
    Plot a histogram of a specified column.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        column (str): Name of the column to plot.
        ax (matplotlib.axes.Axes): Axes object to draw the histogram on.
        title (str): Title of the plot.
        xlabel (str, optional): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        bins (int, optional): Number of bins in the histogram.
        color (str, optional): Color of the histogram.
    """
    ax.hist(data[column], bins=bins, color=color, alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else column)
    ax.set_ylabel(ylabel)
    ax.grid(True)


def plot_box_plot(data, column, ax, title="Box Plot"):
    """
    Plot a box plot of a specified column.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        column (str): Name of the column to plot.
        ax (matplotlib.axes.Axes): Axes object to draw the box plot on.
        title (str): Title of the plot.
    """
    ax.boxplot(data[column])
    ax.set_title(title)
    ax.set_ylabel(column)
    ax.grid(True)


def plot_box_plots(data, columns, ax, title="Box Plot"):
    """
    Plot box plots for multiple columns.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        columns (list): List of column names to plot.
        ax (matplotlib.axes.Axes): Axes object to draw the box plots on.
        title (str): Title of the plot.
    """
    ax.boxplot([data[column] for column in columns], labels=columns)
    ax.set_title(title)
    ax.grid(True)


def plot_correlation_heatmap(data, columns, ax):
    """
    Plot a correlation heatmap for specified columns.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        columns (list): List of column names to include in the correlation matrix.
        ax (matplotlib.axes.Axes): Axes object to draw the heatmap on.
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
    Create a forecast card with weather information.

    Args:
        ax (matplotlib.axes.Axes): Axes object to draw the forecast card on.
        date (datetime): Date of the forecast.
        high_temp (float): High temperature value.
        low_temp (float): Low temperature value.
        weather (str): Weather condition (e.g., 'Sunny', 'Partly Cloudy', 'Rainy').
    """
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
    ax.text(0.5, 0.6, f'High: {high_temp:.2f}°C', fontsize=10, ha='center', va='center', color='red')

    # Display low temperature
    ax.text(0.5, 0.4, f'Low: {low_temp:.2f}°C', fontsize=10, ha='center', va='center', color='blue')

    # Display weather condition
    ax.text(0.5, 0.2, weather, fontsize=10, ha='center', va='center')
