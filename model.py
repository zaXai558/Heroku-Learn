import pandas as pd
data =pd.read_csv('Advertising.csv')
feature_cols = ['TV', 'radio', 'newspaper']
X = data[feature_cols]
X = data[['TV', 'radio', 'newspaper']]
y = data['sales']
from sklearn.linear_model import LinearRegression

# instantiate
linreg = LinearRegression()

# fit the model to the training data (learn the coefficients)
linreg.fit(X, y)

#saving model in disk
import pickle
pickle.dump(linreg, open('model.pkl','wb'))

#loading model
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,2,3]]))

