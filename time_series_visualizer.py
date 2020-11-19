import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import math

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'], infer_datetime_format=True)

# Clean data
df = df[
  (df['value'] > df['value'].quantile(0.025)) &
  (df['value'] < df['value'].quantile(0.975))
]


def draw_line_plot():
  # Draw line plot
  df_line = df.copy()

  fig = plt.figure(figsize=(15, 5))
  plt.plot(df_line.index, df_line['value'], 'r-')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.groupby([df.index.year, df.index.month_name()], sort=False).mean()

  df_bar.index.set_names(["year", "month"], inplace=True)

  df_bar = df_bar.reset_index()

  # plot bar chart
  fig, ax = plt.subplots()
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  years = df_bar['year'].unique()
  # get index of first month in 'month' column
  x_shift = months.index(df_bar.iloc[0]['month'])

  for i, month in enumerate(months):
    rows = df_bar.loc[df_bar['month'] == month]
    x_values = rows.index.values
    x = pd.Series(x_values).apply(lambda v: v + 12 * (len(years) - len(x_values) + math.floor(v / 12))) + x_shift
    y = rows.value.values
    ax.bar(x, y, width=1, label=month, align='edge')
  
  # add 'x_shift' empty bars at the start to meet test requirements
  ax.bar(range(0, x_shift), np.array([0]) * x_shift, width=1, align='edge')

  # Add custom x-axis tick labels, etc.
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  ax.set_xticks(np.arange(6, len(years) * 24, 24))
  ax.set_xticklabels(years)
  ax.legend()

  fig.tight_layout()

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)





  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
