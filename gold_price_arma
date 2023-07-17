# In this program we will be estimating the gold prices and forecast future values using Auto Regression and Moving Average(ARMA) model
import pandas as pd
import seaborn as sns
from statsmodels.tsa.ar_model import AutoReg
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = pd.read_csv('gold_price_data.csv',parse_dates=[0])
df=data.copy()
print(data.head())

# Plotting gold prices
df.index = df['Date']
df['Value'].plot()

# Getting the trend of the gold rates
sns.regplot(x=data.index.values,y=data['Value'])
data =pd.read_csv('gold_price_data.csv',parse_dates=[0])
data
data['lag1'] = data['Value'].shift(1)
data['resid'] = data['Value']-data['lag1']

# buidling ARMA model
train, test = data[1:df.shape[0] - 15], data[data.shape[0] - 15:]
xTrain, yTrain = train['lag1'], train['Value']
xTest, yTest = test['lag1'], test['Value']
trainData, testData = data.resid[1:df.shape[0]-15], data.resid[data.shape[0]-15:]

model = AutoReg(trainData,lags=5)
modelFit = model.fit()

# forecasting residual values
predResidue = modelFit.predict(start=len(trainData), end=len(trainData) + len(testData))

# adding the residuals to the forecast we have already made
predictions = data.lag1[data.shape[0]-15:] + predResidue

size = data.shape[0]
value = data['Value'].iloc[-1]
pred = list(modelFit.forecast(15))
pred = [value+i for i in pred]
print(pred)
