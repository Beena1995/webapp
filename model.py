## importing libraries
from pyforest import *
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
from sklearn.datasets import load_iris
import joblib

## loading the dataset into a pandas dataframe
data = load_iris()
# data.feature_names
df = pd.DataFrame(data.data)

df.columns = data.feature_names
df["target"] = data.target

X = df.drop("target", axis=1)
y = df.target

## splitting the dataset into train and test

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

## loading SVC model by creating an object of the class

model = SVC()
## training the model
model.fit(X_train,y_train)

## making predictions
y_pred = model.predict(X_test)

## pickling the model
joblib.dump(model, "model.pkl")
c = [2,3,3,4]
from_jb = joblib.load(open("model.pkl", 'rb'))
from_jb.predict([c])