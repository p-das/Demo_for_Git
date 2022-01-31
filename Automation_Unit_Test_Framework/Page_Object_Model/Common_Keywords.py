import pandas as pd
from  Object_Repository import utilities_imdb

class CmnKeywords():

    def read_data(self,sheet_name):
        df1 = pd.read_excel(utilities_imdb.input_filepath, sheet_name)
        data = df1.values.tolist()
        input_data = data[0]
        return input_data