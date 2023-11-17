from data_choise import Data_choise
import random

class Main_prog():
    def __init__(self) -> None:
        pass


    def random_proba(self):
        probak = [self.hungarian_to_english_one_word, self.english_to_hungarian_one_word]
        self.valasztott_proba = random.sample(probak, 1)
        self.valasztott_proba[0]()


    def hungarian_to_english_one_word(self):
        feladat = Data_choise().random_data(1)
        magyar_szo = feladat[0][0]
        angol_szo = feladat[0][1]
        print(1)
        return magyar_szo, angol_szo

    def english_to_hungarian_one_word(self):
        feladat = Data_choise().random_data(1)
        magyar_szo = feladat[0][0]
        angol_szo = feladat[0][1]
        print(2)
        return magyar_szo, angol_szo

    def four_word(self):
        feladat = Data_choise().random_data(4)
        magyar_szo = feladat[0][0]
        angol_szo = feladat[0][1]
        return magyar_szo, angol_szo

    def tizproba(self):
        for i in range(10):
            self.random_proba()




if __name__ == "__main__":
    adatok = Main_prog()
    e = adatok.tizproba()
    # print(e[1])