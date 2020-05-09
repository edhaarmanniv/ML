import pandas as pd
from sklearn.linear_model import SGDRegressor
from joblib import dump
from preprocess import prep_data

df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

clf = LassoCV(n_alphas=10, max_iter=10000, normalize=True)
clf.fit(X, y)

dump(lr, "Lasso_CV.joblib")