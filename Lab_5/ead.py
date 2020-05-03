from datetime import datetime


class Konto:
    def __init__(self, wlasciciel, nr_konta, stan_konta=0.0):
        self.stan_konta = stan_konta
        self.wlasciciel = wlasciciel
        self.nr_konta = nr_konta
        self.operacje = []

    def __aktualny_stan_konta__(self):
        print('Aktualny stan konta nr: %d ' % self.nr_konta
              + 'wynosi PLN %.2f' % self.stan_konta)

    def __wplata__(self, kwota):
        try:
            float(kwota)
            if kwota < 0:
                self.__wrong_sum__()
            else:
                self.stan_konta += kwota
                self.operacje.append(kwota)
                return self.stan_konta
        except ValueError:
            self.__wrong_sum__()

    def __wyplata__(self, kwota):
        try:
            float(kwota)
            if kwota < 0:
                self.__wrong_sum__()
            else:
                if self.stan_konta - kwota > 0:
                    self.stan_konta -= kwota
                    self.operacje.append(-kwota)
                    return self.stan_konta
                else:
                    print('Nie można wykonać operacji. Stan konta wynosi: '
                          'PLN %.2f' % self.stan_konta)
        except ValueError:
            self.__wrong_sum__()

    def __time__(self, choice):
        now = datetime.now()
        data = now.date()
        mies = now.date().month
        rok = now.date().year

        if choice == 1:
            return data
        elif choice == 2:
            return mies
        else:
            return rok

    def __przelew_dane__(self, nr_konta, wlasciciel, kwota, cel, in_out):

        def __odbiorca_nadawca__(inout):
            if inout == "in":
                napis = ' nadawcy: '
            else:
                napis = ' odbiorcy: '
            return napis

        print('\nNazwa' + __odbiorca_nadawca__(in_out),
              wlasciciel.nazwa_cz1, wlasciciel.nazwa_cz2)
        print('Adres' + __odbiorca_nadawca__(in_out), str(wlasciciel.adres))
        print('Nr konta' + __odbiorca_nadawca__(in_out) + '' + str(nr_konta))
        print('Tytułem: ' + str(cel))
        print('PLN %.2f' % kwota)
        print('Data wykonania przelewu: {}'.format(self.__time__(1)) + '\n')

    def __przelew_wew__(self, nr_konta, wlasciciel, kwota, cel, in_out):
        if self.__check_number__(nr_konta):
            if in_out == "out":
                if self.__wyplata__(kwota):
                    self.wlasciciel = Wlasciciel(self.wlasciciel.adres,
                                                 self.wlasciciel.nazwa_cz1,
                                                 self.wlasciciel.nazwa_cz2)
                    self.__przelew_dane__(nr_konta, self.wlasciciel, kwota, cel, in_out)
            else:
                if self.__wyplata__(kwota):
                    self.wlasciciel = Wlasciciel(self.wlasciciel.adres,
                                                 self.wlasciciel.nazwa_cz1,
                                                 self.wlasciciel.nazwa_cz2)
                    self.__przelew_dane__(nr_konta, self.wlasciciel, kwota, cel, in_out)

    def __przelew_zew__(self, nr_konta, wlasciciel, kwota, cel, in_out):
        if self.__check_number__(nr_konta):
            if in_out == "out":
                if self.__wyplata__(kwota):
                    self.__przelew_dane__(nr_konta, wlasciciel, kwota, cel, in_out)
            else:
                if self.__wplata__(kwota):
                    self.__przelew_dane__(nr_konta, wlasciciel, kwota, cel, in_out)

    def __check_number__(self, nr_konta):
        if len(str(nr_konta)) != 6:  # w rzeczywistosci !=26:
            self.__wrong_number__()
            return False
        else:
            for i in range(0, len(str(nr_konta))):
                try:
                    int(str(nr_konta)[i])
                except ValueError:
                    self.__wrong_number__()
                    return False
        return True

    def __wrong_number__(self):
        print('Nieprawidłowy numer konta')

    def __wrong_sum__(self):
        print('Nieprawidłowy format kwoty.')

    def __podsumowanie__(self):
        i = len(self.operacje) - 1
        print('\nKonto nr %d: dokonano wpłat i wypłat '
              'opiewających na kwoty:' % self.nr_konta)
        while i >= 0:
            print('PLN %.2f' % self.operacje.pop())
            i -= 1
        self.__aktualny_stan_konta__()


class Wlasciciel:
    def __init__(self, adres, nazwa_cz1, nazwa_cz2=''):
        self.nazwa_cz1 = nazwa_cz1
        self.nazwa_cz2 = nazwa_cz2
        self.adres = adres


class KontoPrywatne(Konto):
    def __przelew_wynagrodzenia__(self, nr_konta, pracodawca, kwota):
        opis = "Wynagrodzenie za miesiąc {} {} roku".format(self.__time__(2), self.__time__(3))
        Konto.__przelew_zew__(self, nr_konta=nr_konta,
                              wlasciciel=pracodawca, kwota=kwota, cel=opis, in_out="in")


class KontoFirmowe(Konto):
    def __przelew_do_ZUS__(self, nr_konta, oddział, rodzaj_skladki, za_kogo, kwota):
        beneficjent = za_kogo.nazwa_cz2 + " " + za_kogo.nazwa_cz1 + "\n" + za_kogo.adres
        opis = "Ubezpieczenie {} za miesiąc {} {} roku.\n" \
               "Beneficjent: {}" \
            .format(rodzaj_skladki, self.__time__(2), self.__time__(3), beneficjent)
        Konto.__przelew_zew__(self, nr_konta=nr_konta,
                              wlasciciel=oddział, kwota=kwota, cel=opis, in_out="out")

    def __przelew_do_US__(self, nr_konta, oddział, rodzaj_podatku, okres, kwota):
        opis = 'Podatek {} za okres {}.'.format(rodzaj_podatku, okres)
        Konto.__przelew_zew__(self, nr_konta=nr_konta,
                              wlasciciel=oddział, kwota=kwota, cel=opis, in_out="out")


konto1 = KontoPrywatne(Wlasciciel("Słomiana 3, 13-432 Garwolin", "Karol", "Rebus"), 223344)
konto1.__przelew_wynagrodzenia__(443322,
                                 Wlasciciel("Chwastowa 12, 13-400 Garwolin",
                                            'Spóldzielnia Pracy "Daremny trud"'),
                                 257.34)
konto2 = KontoFirmowe(Wlasciciel("Chwastowa 12, 13-400 Garwolin",
                                 'Spóldzielnia Pracy "Daremny trud"'),
                      443322, 23987.50)
konto2.__przelew_do_ZUS__(999999,
                          Wlasciciel("Piska 4, 13-401 Garwolin",
                                     'Zakład Ubezpieczeń Społecznych, Oddział w Garwolinie'),
                          "emerytalne",
                          Wlasciciel("Słomiana 3, 13-432 Garwolin", "Karol", "Rebus"), 13.45)

konto2.__przelew_do_US__(333333,
                         Wlasciciel('Koszarowa 2', 'Urząd Skarbowy w Garwolinie'),
                         "obrotowy", "styczeń - maj 2020", 450.20)

konto1.__podsumowanie__()
konto2.__podsumowanie__()

# Result:
#
# Nazwa nadawcy:  Spóldzielnia Pracy "Daremny trud"
# Adres nadawcy:  Chwastowa 12, 13-400 Garwolin
# Nr konta nadawcy: 443322
# Tytułem: Wynagrodzenie za miesiąc 5 2020 roku
# PLN 257.34
# Data wykonania przelewu: 2020-05-03
#
#
# Nazwa odbiorcy:  Zakład Ubezpieczeń Społecznych, Oddział w Garwolinie
# Adres odbiorcy:  Piska 4, 13-401 Garwolin
# Nr konta odbiorcy: 999999
# Tytułem: Ubezpieczenie emerytalne za miesiąc 5 2020 roku.
# Beneficjent: Rebus Karol
# Słomiana 3, 13-432 Garwolin
# PLN 13.45
# Data wykonania przelewu: 2020-05-03
#
#
# Nazwa odbiorcy:  Urząd Skarbowy w Garwolinie
# Adres odbiorcy:  Koszarowa 2
# Nr konta odbiorcy: 333333
# Tytułem: Podatek obrotowy za okres styczeń - maj 2020.
# PLN 450.20
# Data wykonania przelewu: 2020-05-03
#
# Konto nr 223344: dokonano wpłat i wypłat opiewających na kwoty:
# PLN 257.34
# Aktualny stan konta nr: 223344 wynosi PLN 257.34
#
# Konto nr 443322: dokonano wpłat i wypłat opiewających na kwoty:
# PLN -450.20
# PLN -13.45
# Aktualny stan konta nr: 443322 wynosi PLN 23523.85

# Process finished with exit code 0
