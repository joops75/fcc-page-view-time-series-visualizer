import matplotlib.pyplot as plt
import pandas as pd
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
  
  # create new df with complete year and month ranges
  years = df_bar.index.get_level_values('year').unique()
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  new_df_years = []
  new_df_months = []
  new_df_values = []
  for year in range(years[0], years[-1] + 1):
    for month in months:
      new_df_years.append(year)
      new_df_months.append(month)
      try:
        new_df_values.append(df_bar.loc[(year, month), 'value'])
      except:
        new_df_values.append(0)
        
  df_bar = pd.DataFrame({ 'year': new_df_years, 'month': new_df_months, 'value': new_df_values})
  
  # plot bar chart
  fig, ax = plt.subplots()

  for i, month in enumerate(months):
    rows = df_bar.loc[df_bar['month'] == month]
    x_values = rows.index.values
    x = pd.Series(x_values).apply(lambda v: v + 12 * math.floor(v / 12))
    y = rows.value.values
    ax.bar(x, y, width=1, label=month, align='edge')

  # Add custom x-axis tick labels, etc.
  years = df_bar['year'].unique()
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  ax.set_xticks(range(6, len(years) * 24, 24))
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
