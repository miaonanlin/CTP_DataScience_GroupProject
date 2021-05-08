import pandas as pd
import numpy as np
# Import the trees from sklearn
from sklearn import tree
# Helper function to split our data
from sklearn.model_selection import train_test_split
# Import our Random Forest
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('https://raw.githubusercontent.com/miaonanlin/CTP_DataScience_GroupProject/main/phishing_website_dataset.csv')
select_features = ['SSLfinal_State','URL_of_Anchor', 'web_traffic',  'having_Sub_Domain','Links_in_tags']

X = df[select_features]

y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

model = RandomForestClassifier()

model.fit(X_train, y_train)


#pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb') )

pickle.dump(model, open('models/classifier.pkl', 'wb') )
