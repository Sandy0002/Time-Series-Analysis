# In this program we will estimate the electricity requirements
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data = pd.read_csv('energy_req.csv',parse_dates=[0])
print(data.head())

data = data[['Date','AllIndia']]
print(data.info())

data.rename(columns={'AllIndia':'required'},inplace=True)
data['Date'] = pd.to_datetime(data['Date'],format=('%Y-%d-%M'))

# Assuming the humidity data is stored in the 'humidity' column
humidity_data = data['required']
print(data.head())

# There is a growing trend
df = data.copy()
df.index = data['Date']

df['required'].plot()

yearlyConsumption = data.resample('A',on='Date').mean()
monthlyConsumption = data.resample('M',on='Date').mean()

# Plotting yearly consumptions of electricity
yearlyConsumption.plot()

# Lets see if there is any seasonality
year1 = data[data['Date'].dt.year==2015]
year2 = data[data['Date'].dt.year==2016]
print(year1)

year1.plot()
year2.plot()

# There are trend and seasonality
plot_acf(data['required'])

plot_pacf(data['required'])
plt.show()

# Train test split
size = len(data)
trainSize  = int(size*0.8)
testSize = size-trainSize
trainData,testData = data[:trainSize],data[trainSize:]

# We will perform dickey fuller test to whether to include d or not
result = adfuller(data['required'])
test_statistic = result[0]
p_value = result[1]
d = 1 if p_value<0.005 else 0

# SARIMA creation as there is seasonality 
model = ARIMA(trainData['required'],order=(1,1,0),seasonal_order=(1,0,1,12))
model = model.fit()

# Getting model summary
print(model.summary())

pred = model.predict(start=trainSize,end=trainSize+testSize-1)
print(r2_score(testData['required'],pred))

# Model predictions for the next 15 days
pred = model.predict(start=size,end=size+15)
print(pred)
