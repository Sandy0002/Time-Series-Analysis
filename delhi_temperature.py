# In this program we will estimate the temperature of the Delhi
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import MinMaxScaler
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller

data = pd.read_csv('delhi_weather.csv',parse_dates=[0])
print(data.head())
print(data.tail())

# Since only 1 2017 year value is there we remove it
data= data[data['date'].dt.year!=2017]

# checking data information
print(data.info())

# Univariate data analysis
print(data.describe())

# Plotting the relations with the meantemp
sns.pairplot(data,x_vars=['humidity','wind_speed','meanpressure'],y_vars='meantemp')

# pressure is not at all related to temperature so we can remove them
del data['meanpressure']
correlation_matrix = data.corr()
print(correlation_matrix['meantemp'])

df = data.copy()
df.index = df['date']
df['meantemp'].plot()

# There is a seasonality in the data
# plotting the trend
sns.regplot(x=data.index.values, y= data['meantemp'])

# There is a growing trend of mean temperature 
# lets decompose the data
result = seasonal_decompose(df['meantemp'],model='multiplicative')
result.plot()
plt.show()

# resampling data to get the seasonality
quarterlyTemp = data.resample('Q',on='date').mean()
yearlyTemp = data.resample('A',on='date').sum()

yearlyTemp['meantemp'].plot()
# There is a sharp growth in temperature

quarterlyTemp['meantemp'].plot()
# There is seasonlaity in graph
# Scaling data
scaler = MinMaxScaler()
data = data[['meantemp','humidity','wind_speed']]
dataScale = scaler.fit_transform(data)

# Combine the exogenous variables (humidity and wind speed) into a single DataFrame
exog_data = pd.concat([data['humidity'], data['wind_speed']], axis=1)

plot_acf(data['meantemp'])

plot_pacf(data['meantemp'])
plt.show()

# Dickey fuller test
result = adfuller(data['meantemp'])
p_value = result[1]
d = 1 if p_value<0.005 else 0

# Model building
model = SARIMAX(data['meantemp'],exog=exog_data,order=(1,d,1))
model =model.fit()

size = data.shape[0]
trainSize = int(data.shape[0]*0.7)
testSize = size-trainSize
print(trainSize,testSize)

# Predicting for the next 15 days
print(model.forecast(15,exog=exog_data[size-15:]))

#  Generate predictions
predictions = model.predict(start=trainSize, end=trainSize+testSize-1, exog=exog_data[trainSize:])

# Assuming y_test contains the actual temperature values for the test set
y_test = data['meantemp'][trainSize:]

# Predicting for the next 15 days
print(model.forecast(15,exog=exog_data[size-15:]))
