# Analysing Super Store Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Reading Data
data = pd.read_csv('..\\data\\Sample_Superstore.csv', encoding='ISO-8859-1')

# Data Columns
columns = data.columns

# Filling The Missing Values
# for c in data.columns:
#     if data[c].dtype != 'object':
#         data[c].fillna(data[c].mean(), inplace=True)
#     else:
#         data[c].fillna('', inplace=True)
data.fillna({c: data[c].mean() if data[c].dtype != 'object' else '' for c in data.columns}, inplace=True)

# Dropping Duplicated Data
data.drop_duplicates(inplace=True)

# Formating Dates
data['Ship Date'] = pd.to_datetime(data['Ship Date'], format='%m/%d/%Y')
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%m/%d/%Y')


# Downcasting All Strings To Lowercase
for c in data.select_dtypes(include='object').columns:
    data[c]=data[c].apply(lambda x:x.strip().lower())


data.isnull().sum()


# Statistical Description
print(data.describe())
print(data.describe(include='object'))


for c in data.select_dtypes(include='object').columns:
    print(data[c].value_counts())


# Average Of Profits For  Each Category Kind
data.groupby('Category')['Profit'].mean()


# Profit Margin = Profit/Sales
data['Profit Margin'] = data['Profit'] / data['Sales']


# Now i'm gonna go for Query's questions plot

# -------------------------------------------------

# What are the total sales and profits? Which has grown the most? 
obj = ['Sales','Profit']
x_pos = np.arange(len(obj))
y_pos = data[obj].sum()
plt.bar(x_pos,y_pos,color = ['red','green'])
plt.title('Total Sales & Profit')
plt.yticks(y_pos)
plt.xticks(x_pos,obj)
plt.ylabel('Values')
plt.savefig('..\\Plots\\Total_Sales_&_Profit.jpg')


# Have sales trends been growing?
df = data.groupby('Order Date')['Sales'].sum()
y = df.values
x = df.index
plt.figure(figsize=(500,200))
plt.plot(x,y,marker='o', linestyle='-')
plt.title('Trends')
plt.xlabel('Date')
plt.ylabel('Sales')
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
plt.savefig('..\\Plots\\Trends.jpg')


# What product category has the most sales/profits?
df2 = data.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
x_label = df2['Category'].values
x_pos2 = np.arange(len(x_label))
y2 = df2['Sales'].values
y3 = df2['Profit'].values
bar_width = 0.34
plt.figure(figsize=(10,6))
plt.bar(x_pos2 - bar_width/2 ,y2,bar_width,color = 'r' ,label = 'Sales')
plt.bar(x_pos2 + bar_width/2 ,y3,bar_width,color = 'g' ,label = 'Profit')
plt.xticks(x_pos2,x_label)
plt.legend()
plt.ylabel('Amount')
plt.title('Profit & Sales')
plt.savefig('..\\Plots\\Profit_Sales.jpg')


# Which state has the most profit?
df3 = data.groupby('State')['Profit'].sum()
y_pos = np.arange(len(df3.index))
x_pos = df3.values
y_label = df3.index

plt.figure(figsize=(15,15))
plt.barh(y_pos,x_pos, color = 'g')
plt.yticks(y_pos,y_label)
plt.ylabel('State')
plt.xlabel('Profit')
plt.title("State's Profit")
plt.savefig("..\\Plots\\State's Profit.jpg")


# Do we have high-sales, low-profit products?
# sns.scatterplot(data=data,x='Sales',y='Profit Margin',color= '#25C5DB') <--- for showing another way to drawing
sns.regplot(data=data,x='Sales',y='Profit Margin',line_kws={'color' : '#D82222','linewidth': 1},scatter_kws={'color' : '#25C5DB','s' : 5})
plt.title('Sales With Low Profits')
plt.savefig('..\\Plots\\Sales_Low_Profit.jpg')


# Shipping Delays by Category
data['Delay'] = (data['Ship Date']-data['Order Date']).dt.total_seconds()/(24*60*60) # this '.dt.total_seconds/24*60*60' part is to get the number of delay column(e.g. 3 days 22:00:30.551626591) /60 is for minute then /60 is for hours then /24 for days
df4 = data.groupby('Category')['Delay'].mean()
y_pos = np.arange(len(df4.index))
y_label = df4.index
x_pos = df4.values
bar_width= 0.5

plt.figure(figsize=(12,6))
plt.barh(y_pos,x_pos,bar_width,color = '#F3EE12')
plt.yticks(y_pos,y_label)
plt.ylabel('Category')
plt.xlabel('Delay')
plt.title('Delay By Category')
plt.savefig("..\\Plots\\Delay_By_Category.jpg")