import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
%matplotlib inline
# Import the trees from sklearn
from sklearn import tree
# Helper function to split our data
from sklearn.model_selection import train_test_split
# Helper fuctions to evaluate our model.
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, roc_auc_score
# Helper function for hyper-parameter turning.

# Import our Decision Tree
from sklearn.tree import DecisionTreeClassifier
# Import our Random Forest
from sklearn.ensemble import RandomForestClassifier
# Library for visualizing our tree
# If you get an error, run 'pip install graphviz' in your terminal
import graphviz
import pickle

df = pd.read_csv('https://raw.githubusercontent.com/miaonanlin/CTP_DataScience_GroupProject/main/phishing_website_dataset.csv')
select_features = ['SSLfinal_State','URL_of_Anchor', 'web_traffic',  'having_Sub_Domain','Links_in_tags']

X = df[select_features]

y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

model = RandomForestClassifier()

model.fit(X_train, y_train)


#pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb') )

pickle.dump(model, open('models/text-classifier.pkl', 'wb') )
