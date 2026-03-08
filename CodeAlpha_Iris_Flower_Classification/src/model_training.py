from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def train_models(X_train, y_train):

    models = {}

    lr = LogisticRegression(max_iter=200)
    lr.fit(X_train, y_train)
    models["Logistic Regression"] = lr

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    models["Decision Tree"] = dt

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    models["Random Forest"] = rf

    return models