import pandas as pd

class sdcDataFrame():
    def __init__(self, filepath=None):
        self.df = pd.DataFrame()
        if filepath is not None:
            self.df = pd.read_csv(filepath)

    def head(self, n=5):
        return self.df.head(n=5)
    
    def getColumnNames(self):
        columns = self.df.columns
        types = self.df.dtypes
        dataset = [[columns[i], types[i]] for i in range(len(columns))]
        return pd.DataFrame(dataset, columns=["ColumnName", "DataType"]).reset_index(drop=True)

    def addNoise(self, columName, type="additive"):
        if not (pd.is_numeric_dtype(self.df[columName])):
            raise Exception("You can only apply noise on numeric columns")
        
        if type == "additive":
            self._additiveNoise()
        elif type == "correlated":
            self._correlativeNoise()
        else:
            raise Exception("Unsupported type of noise")

    def _additiveNoise(self):
        #TODO implement additive noise
        pass

    def _correlativeNoise(self):
        #TODO implement correlative noise
        pass