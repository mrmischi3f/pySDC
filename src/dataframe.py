import pandas as pd

class sdcDataFrame():
    def __init__(self, filepath=None):
        self.df = pd.DataFrame()
        if filepath is not None:
            self.df = pd.read_csv(filepath)