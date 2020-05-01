class Konto:
    def __init__(self, stan_konta=0):
        self.stan_konta = stan_konta
        self.operacje = []

    def __wplata__(self, kwota):
        self.stan_konta += kwota
        self.operacje.append(kwota)
        return self.stan_konta

    def __wyplata__(self, kwota):
        if self.stan_konta - kwota > 0:
            self.stan_konta -= kwota
            self.operacje.append(-kwota)
            return self.stan_konta
        else:
            print('Nie można wykonać operacji. Stan konta wynosi: ' \
                  'PLN {}'.format(self.stan_konta))

    def __przelew_wew__(self, nr_konta, kwota):
        if self.__check_number__(nr_konta):
            self.__wyplata__(kwota)

    def __przelew_zew__(self, nr_konta, odbiorca, kwota):
        self.odbiorca = odbiorca
        if self.__check_number__(nr_konta):
            self.__wyplata__(kwota)

    def __check_number__(self, nr_konta):
        ok = False
        try:
            ok = int(nr_konta)
        except ValueError:
            print('Nieprawidłowy numer konta')
        return ok


class Odbiorca:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres


konto1 = Konto()
print(str(konto1.stan_konta))
konto1.__wplata__(10)
print(str(konto1.stan_konta))
konto1.__wyplata__(11)
konto1.__wplata__(109)
print(str(konto1.stan_konta))
konto1.__wyplata__(11)
print(str(konto1.stan_konta))
konto1.__przelew_wew__("numer konta", 12)
konto1.__przelew_wew__(123, 12)
print(str(konto1.stan_konta))
konto1.__przelew_zew__(234,("Spoldzielnia mieszkaniowa","Wańkowicza 17, Olsztyn"),78)
print(str(konto1.stan_konta))