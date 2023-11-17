# import data_controll
from data_controll import Data_controll
from random import choices

class Data_choise():
    def __init__(self) -> None:
        self.df = Data_controll().df
        
    def random(self, elem=1):
        lista = self.df['Magyar'].tolist()
        sulyok = self.df['Tudásszint'].tolist()
        valasztott_elemek = set()

        # Súlyok normalizálása
        osszeg = sum(sulyok)
        normalizalt_sulyok = [suly / osszeg for suly in sulyok]
        # Inverz súlyok kiszámítása
        inverz_sulyok = [1/suly for suly in normalizalt_sulyok]

        while len(valasztott_elemek) < elem:
            valasztott_elem = choices(lista, weights=sulyok, k=1)[0]
            valasztott_elemek.add(valasztott_elem)

        return list(valasztott_elemek)   


    def random_data(self, elem):
        valasztott_elem = self.random(elem)
        self.adatok = []
        for i in range(elem):
            adat = self.df[self.df['Magyar'] == valasztott_elem[i]][['Angol', 'Kategória', 'Tudásszint']]
            
            adat_list = [valasztott_elem[i], adat['Angol'].values[0], adat['Kategória'].values[0], adat['Tudásszint'].values[0]]
            self.adatok.append(adat_list)
        return self.adatok



if __name__ == "__main__":
    adatok = Data_choise()
    valasztott = adatok.random_data(2)
    print("Inverz súlyozott véletlenszerűen kiválasztott elem:", valasztott)
        
