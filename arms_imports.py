# In this program we will estimate the arms imports that India would do in coming years
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

data =pd.read_csv('arms_imports.csv',parse_dates=[0])
print(data.head())

data.rename(columns={'Country/Region/Group':'Year'},inplace=True)

# Since we want only INdia so we create other dataset
data=data[['Year','India']]

# Converting year to datetime
data =  data[data['Year']!='Total']
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
print(data['Year'])

# Plotting the imports
data['India'].plot()

# Creating another dataframe having index as datetime
df = data.copy()
df.index = df['Year']
result  = seasonal_decompose(df['India'],model='additive')
result.plot()

result  = seasonal_decompose(df['India'],model='multiplicative')
result.plot()

# Clearly we can see there is no seasonality only trend is there

# Getting auto correlation
plot_acf(data['India'])

plot_pacf(data['India'])
plt.show()

# We will perform dickey fuller test to whether to get d value
result = adfuller(data['India'])
test_statistic = result[0]
p_value = result[1]
d = 1 if p_value<0.005 else 0

# Building ARIMA model
size = len(data)
trainSize = int(size*0.7)
testSize = size-trainSize
trainData = data[:trainSize]
testData = data[trainSize:]
model = ARIMA(data['India'],order=(1,0,17))
model = model.fit()

# Getting model summary
print(model.summary())

# Model predictions
pred = model.predict(start=trainSize,end=trainSize+testSize-1)
# Predictions for the next 15 days
print(model.predict(start=size,end=size+15))
