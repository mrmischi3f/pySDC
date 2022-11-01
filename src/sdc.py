import dataframe
from src.dataframe import sdcDataFrame

def read_csv(filepath):
    return sdcDataFrame(filepath=filepath)