import pandas as pd

def load_data(path):

    df = pd.read_csv(path)

    X = df.drop("species", axis=1)
    y = df["species"]

    return X, y