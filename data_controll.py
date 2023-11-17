import pandas as pd

EXCEL_FILE_PATH = 'data\szavak.xlsx'

class Data_controll():
    def __init__(self) -> None:
        self.read()


    def read(self):
        self.df = pd.read_excel(EXCEL_FILE_PATH)


    def write(self):
        self.df.to_excel(EXCEL_FILE_PATH, index=False)


    def modifies(self, key, number, modifies_key, modifies_number):
        # df.loc[df['Név'] == 'Alice', 'Életkor'] = 25
        self.df.loc[self.df[key] == number, modifies_key] = modifies_number