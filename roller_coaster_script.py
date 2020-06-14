import pandas as pd
import matplotlib.pyplot as plt

# load rankings data:
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# function to plot rankings over time for 1 roller coaster:
def plot_ranking(coaster_name, park_name, ranking_df):
  locating_ranking = ranking_df[(ranking_df['Name'] == coaster_name) & (ranking_df['Park'] == park_name)]
  x = locating_ranking['Year of Rank']
  y = locating_ranking['Rank']

  ax = plt.subplot()
  plt.plot(x, y, marker='o')
  ax.set_yticks(locating_ranking['Rank'].values)
  ax.set_xticks(locating_ranking['Year of Rank'].values)
  ax.invert_yaxis()

  plt.title('{} Rankings'.format(coaster_name))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  return plt.show()

plot_ranking('Boulder Dash', 'Lake Compounce', wood_df)

plt.clf()

# function to plot rankings over time for 2 roller coasters:
def check_two_ranking(name1, name2, park_name1, park_name2, ranking_df):
  locating_ranking1 = ranking_df[(ranking_df['Name'] == name1) & (ranking_df['Park'] == park_name1)]
  locating_ranking2 = ranking_df[(ranking_df['Name'] == name2) & (ranking_df['Park'] == park_name2)]
  x1 = locating_ranking1['Year of Rank']
  x2 = locating_ranking2['Year of Rank']
  y1 = locating_ranking1['Rank']
  y2 = locating_ranking2['Rank']
  
  ax = plt.subplot()
  plt.plot(x1, y1, marker='o', label=name1)
  plt.plot(x2, y2, marker='*', label=name2)
  ax.invert_yaxis()

  ax.set_yticks(pd.concat([y1, y2]).drop_duplicates().values)
  ax.set_yticklabels(pd.concat([y1, y2]).drop_duplicates().values)
  plt.title('{} VS. {} Rankings'.format(name1, name2)) 
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend()
  return plt.show()

check_two_ranking('Phoenix', 'Boulder Dash', 'Knoebels Amusement Resort', 'Lake Compounce', wood_df)

plt.clf()

# function to plot top n rankings over time:
def top_n_ranking(n, ranking_df):
  top_n_rankings = ranking_df[ranking_df['Rank'] <= n]
  for coaster in set(top_n_rankings['Name']):
    coaster_ranking = top_n_rankings[top_n_rankings['Name'] == coaster]
    x = coaster_ranking['Year of Rank']
    y = coaster_ranking['Rank']
    
    ax = plt.subplot()
    plt.plot(x, y, marker='o', label=coaster)
    
    ax.invert_yaxis()
    ax.set_yticks(range(1, n+1))
    plt.legend()
    plt.title('Top ' + str(n) + ' Coasters')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
  return plt.show()

top_n_ranking(4, wood_df)

plt.clf()

# load roller coaster data:
roller_coasters = pd.read_csv('roller_coasters.csv')
#print(roller_coasters.head())


# function to plot histogram of column values:
def value_hist(numeric_column, coaster_df):
  if numeric_column == 'height':
    heights = coaster_df[coaster_df['height'] <= 140]
    value = heights[numeric_column].dropna()
  else:
    value = coaster_df[numeric_column].dropna()
  
  plt.hist(value, bins=20)
  plt.xlabel(numeric_column.title())
  plt.ylabel('Count')
  plt.title(numeric_column.title() + ' Histogram')
  return plt.show()

value_hist('length', roller_coasters)

plt.clf()

# function to plot inversions by coaster at a park:
def plot_inversions(coaster_df, park_name):
  park_coasters = coaster_df[coaster_df['park'].str.contains(park_name, case=False)].sort_values(by='num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  num_inversions = park_coasters['num_inversions']

  ax = plt.subplot()
  plt.bar(range(len(num_inversions)), num_inversions)
  plt.axis(xmin=1, xmax=(max(range(len(num_inversions)))+1))
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation=90)

  plt.title('Number of Inversions per Coaster at {} Park'.format(park_name.title()))
  plt.xlabel('Roller Coaster')
  plt.ylabel('Number of Inversions')
  return plt.show()

plot_inversions(roller_coasters, 'amusement')

plt.clf()
    
# function to plot pie chart of operating status:
def operating_status(coaster_df):
  status_operating = coaster_df[coaster_df['status'] == 'status.operating']
  status_closed = coaster_df[coaster_df['status'] == 'status.closed.definitely']
  operating_num = [len(status_operating), len(status_closed)]

  ax = plt.subplot()
  plt.pie(operating_num, labels=['Operating', 'Closed'] , autopct='%0.1f%%' )
  ax.axis('equal')
  plt.title('Comparing Operating Status')
  plt.legend()
  return plt.show()

operating_status(roller_coasters)

plt.clf()
  
# function to create scatter plot of any two numeric columns:
def scatter_plot(coaster_df, column_name1, column_name2):
  if column_name1 != 'height' and column_name2 != 'height':
    x = coaster_df[column_name1]
    y = coaster_df[column_name2]
  else:
    coaster_df = coaster_df[coaster_df['height'] < 140]
    x = coaster_df[column_name1]
    y = coaster_df[column_name2]   

  plt.scatter(x, y)
  plt.title('Scatter Plot of {} VS. {}'.format(column_name1.title(), column_name2.title()))
  plt.xlabel(column_name1.title())
  plt.ylabel(column_name2.title())
  return plt.show()

scatter_plot(roller_coasters, 'speed', 'height')

plt.clf()
