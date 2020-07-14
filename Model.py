from sklearn.datasets import load_boston
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.metrics import r2_score,mean_squared_error

import warnings; warnings.simplefilter('ignore')

from sklearn.model_selection import train_test_split

data = load_boston()

X = pd.DataFrame(data.data,columns=data.feature_names)
y = pd.DataFrame(data.target,columns=['price'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(max_depth=10, random_state=0)

model.fit(X_train, y_train)


filename = 'finalized_model.sav'

pickle.dump(model, open(filename, 'wb'))


y_pred = model.predict(X_test)

y_pred = pd.DataFrame(y_pred,columns=y_test.columns)


#print(r2_score(y_test,y_pred))
#print(mean_squared_error(y_test,y_pred))

