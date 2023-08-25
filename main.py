import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #to plot some parameters in seaborn

#Importing the data
df_tick = pd.read_csv("E:/BLT Active Surveillance Results (2013-2019) .csv",index_col=0)

df_tick['Percentage Positive'] = (df_tick['# Positive'] / df_tick['Total BLTs']) * 100 # Make a new column that takes the percentages of the diseased ticks collected
df_tick['Percentage Positive'].fillna(0.0, inplace=True) # Replace all NaN values with 0
df_tick['Percentage Positive'] = df_tick['Percentage Positive'].apply(lambda x: round(x, 1)) # Round values to nearest 10th
df_final = df_tick.drop(['BLT Larvae', 'BLT Adults and Nymphs','Latitude','Longitude'], axis=1) # Drop useless data(cleaning)
BLT_total_sum = df_final['Total BLTs'].sum()
BLT_positive_total_sum = df_final['# Positive'].sum()
top_parks = df_final.sort_values(by='Total BLTs', ascending=False).head(5)

print(df_final.info())
print(df_final.nunique())
print(df_final.head())

x = df_final['Year']
y = df_final['Total BLTs']

plt.figure(figsize=(8, 6))  # Set the figure size
plt.bar(x, y, align='center', alpha=0.7)  # Customize alignment and transparency
plt.title('Total BLT Found')  # Set the title
plt.xlabel('Year')  # Set the X-axis label
plt.ylabel('BLT Found')  # Set the Y-axis label
plt.grid(True)  # Add a grid
plt.show()

slices = [BLT_total_sum, BLT_positive_total_sum]
labels = ['Total ticks', 'Total positive ticks']
colors = ['lightblue', 'lightgreen']
plt.figure(figsize=(8, 8))  #Set the figure size
plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

x = df_final['Year']
y = df_final['Total BLTs']
y2=df_final['# Positive']

plt.figure(figsize=(8, 6))  # Set the figure size
plt.bar(x, y, align='center', alpha=0.7,label='Total BLTs')  # Customize alignment and transparency
plt.bar(x, y2, align='center', alpha=0.7,label='Total Diseased BLTs')  # Customize alignment and transparency
plt.title('Total BLT Found')  # Set the title
plt.xlabel('Year')  # Set the X-axis label
plt.ylabel('BLT Found')  # Set the Y-axis label
plt.grid(True)  # Add a grid
plt.legend()
plt.show()

print(top_parks[['Park Location']]) #print the top 5 worst parks of the data