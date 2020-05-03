class Bohater:
    def __init__(self, imie, zywotnosc, sila_zrecznosc, pkty_taktyki):
        self.imie = imie
        self.zywotnosc = zywotnosc
        self.sila_zrecznosc = sila_zrecznosc
        self.pkty_taktyki = pkty_taktyki

    def __zmien_zywotnosc__(self, nowa_zywotnosc):
        if nowa_zywotnosc > 100 or nowa_zywotnosc < 0:
            print('Podano niewłaściwą wartość')
        else:
            self.zywotnosc = nowa_zywotnosc
        return self.zywotnosc

    def __moc_ataku__(self):
        moc = self.sila_zrecznosc * self.pkty_taktyki * self.zywotnosc
        return moc


class Wojownik(Bohater):
    def __zmien_zywotnosc__(self, nowa_zywotnosc):
        Bohater.__zmien_zywotnosc__(self, nowa_zywotnosc)
        self.__szal__(self.zywotnosc)

    def __szal__(self, zywotnosc):
        if zywotnosc < 20:
            self.zywotnosc = 150
        return self.zywotnosc


class Lucznik(Bohater):
    pass


wojownik = Wojownik("Seger", 100, 9, 5)
lucznik = Lucznik("Kurt", 100, 8, 8)

print(wojownik.pkty_taktyki, wojownik.sila_zrecznosc, wojownik.zywotnosc, wojownik.imie)
print(lucznik.pkty_taktyki, lucznik.sila_zrecznosc, lucznik.zywotnosc, lucznik.imie)
print(wojownik.__moc_ataku__())
print(lucznik.__moc_ataku__())
wojownik.__zmien_zywotnosc__(19)
print(wojownik.zywotnosc)

# Result:
#
# 5 9 100 Seger
# 8 8 100 Kurt
# 4500
# 6400
# 150
#
# Process finished with exit code 0
