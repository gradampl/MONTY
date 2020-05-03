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

    def __przelew_dane__(self, nr_konta, wlasciciel, kwota, cel, in_out, jaki_przelew):

        def __odbiorca_nadawca__(inout):
            if inout == "in":
                napis = ' nadawcy: '
            else:
                napis = ' odbiorcy: '
            return napis

        print('\n........... Przelew {} .............'.format(jaki_przelew))
        print('Nazwa' + __odbiorca_nadawca__(in_out),
              wlasciciel.nazwa_cz1, wlasciciel.nazwa_cz2)
        print('Adres' + __odbiorca_nadawca__(in_out), str(wlasciciel.adres))
        print('Nr konta' + __odbiorca_nadawca__(in_out) + '' + str(nr_konta))
        print('Tytułem: ' + str(cel))
        print('PLN %.2f' % kwota)
        print('Data wykonania przelewu: {}'.format(self.__time__(1)) + '\n')

    def __przelew__(self, nr_konta, wlasciciel, kwota, cel, in_out):
        if self.__check_number__(nr_konta):
            if in_out == "out":
                if self.__wyplata__(kwota):
                    self.__przelew_dane__(nr_konta,
                                          wlasciciel, kwota, cel, in_out,
                                          self.__jaki_przelew__(nr_konta))
            else:
                if self.__wplata__(kwota):
                    self.__przelew_dane__(nr_konta,
                                          wlasciciel, kwota, cel, in_out,
                                          self.__jaki_przelew__(nr_konta))

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

    def __jaki_przelew__(self, nr_konta):
        if int(str(nr_konta)[0]) == 3 \
                and int(str(nr_konta)[1]) == 2 \
                and int(str(nr_konta)[2]) == 1:
            return "wewnętrzny"
        else:
            return "zewnętrzny"

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
        print()


class Wlasciciel:
    def __init__(self, adres, nazwa_cz1, nazwa_cz2=''):
        self.nazwa_cz1 = nazwa_cz1
        self.nazwa_cz2 = nazwa_cz2
        self.adres = adres


konto1 = Konto(Wlasciciel("Dębowa 4, 20-123 Niepołomice", "Włodzimierz", "Bednarek"), 234567)
konto1.__aktualny_stan_konta__()
konto1.__wyplata__("a")
konto1.__wyplata__(-10)
konto1.__wplata__(10)
konto1.__aktualny_stan_konta__()
konto1.__wyplata__(11)
konto1.__wplata__(190)
konto1.__aktualny_stan_konta__()
konto1.__wyplata__(11)
konto1.__aktualny_stan_konta__()
konto1.__aktualny_stan_konta__()
konto1.__przelew__(321567, Wlasciciel("Muniowicza 17, Szkaplerzyce", 'SM "Raj Lokatora"')
                   , 90, "czynsz za maj 2020", "out")
konto1.__aktualny_stan_konta__()

konto2 = Konto(Wlasciciel("Kwiatowa 1, Domaniewice", "Mada", "Wiszniewska"), 765432)
konto1.__przelew__(765432, Wlasciciel(konto2.wlasciciel.adres,
                                      konto2.wlasciciel.nazwa_cz1,
                                      konto2.wlasciciel.nazwa_cz2),
                   12.50, "za ręczniki", "out")
konto2.__przelew__(234567, Wlasciciel(konto1.wlasciciel.adres,
                                      konto1.wlasciciel.nazwa_cz1,
                                      konto1.wlasciciel.nazwa_cz2),
                   12.50, "za ręczniki", "in")
konto3 = Konto(Wlasciciel("Chrząszczyrzewoszyce Wielkie 13", "Walery", "Stef"), 678909, 32.70)
konto3.__przelew__(321910, Wlasciciel("Chrząszczyrzewoszyce Wielkie 13", "Walery", "Stef"), 2.70,
                   "założenie lokaty terminowej", "out")
konto2.__aktualny_stan_konta__()
konto3.__aktualny_stan_konta__()

konto1.__podsumowanie__()
konto2.__podsumowanie__()
konto3.__podsumowanie__()
konto3.__przelew__(678909,
                   Wlasciciel("Chrząszczyrzewoszyce Wielkie 13", "Walery", "Stef"),
                   32, "za zakupy", "out")

# Result:
#
# Aktualny stan konta nr: 234567 wynosi PLN 0.00
# Nieprawidłowy format kwoty.
# Nieprawidłowy format kwoty.
# Aktualny stan konta nr: 234567 wynosi PLN 10.00
# Nie można wykonać operacji. Stan konta wynosi: PLN 10.00
# Aktualny stan konta nr: 234567 wynosi PLN 200.00
# Aktualny stan konta nr: 234567 wynosi PLN 189.00
# Aktualny stan konta nr: 234567 wynosi PLN 189.00
#
# ........... Przelew wewnętrzny .............
# Nazwa odbiorcy:  SM "Raj Lokatora"
# Adres odbiorcy:  Muniowicza 17, Szkaplerzyce
# Nr konta odbiorcy: 321567
# Tytułem: czynsz za maj 2020
# PLN 90.00
# Data wykonania przelewu: 2020-05-03
#
# Aktualny stan konta nr: 234567 wynosi PLN 99.00
#
# ........... Przelew zewnętrzny .............
# Nazwa odbiorcy:  Mada Wiszniewska
# Adres odbiorcy:  Kwiatowa 1, Domaniewice
# Nr konta odbiorcy: 765432
# Tytułem: za ręczniki
# PLN 12.50
# Data wykonania przelewu: 2020-05-03
#
#
# ........... Przelew zewnętrzny .............
# Nazwa nadawcy:  Włodzimierz Bednarek
# Adres nadawcy:  Dębowa 4, 20-123 Niepołomice
# Nr konta nadawcy: 234567
# Tytułem: za ręczniki
# PLN 12.50
# Data wykonania przelewu: 2020-05-03
#
#
# ........... Przelew wewnętrzny .............
# Nazwa odbiorcy:  Walery Stef
# Adres odbiorcy:  Chrząszczyrzewoszyce Wielkie 13
# Nr konta odbiorcy: 321910
# Tytułem: założenie lokaty terminowej
# PLN 2.70
# Data wykonania przelewu: 2020-05-03
#
# Aktualny stan konta nr: 765432 wynosi PLN 12.50
# Aktualny stan konta nr: 678909 wynosi PLN 30.00
#
# Konto nr 234567: dokonano wpłat i wypłat opiewających na kwoty:
# PLN -12.50
# PLN -90.00
# PLN -11.00
# PLN 190.00
# PLN 10.00
# Aktualny stan konta nr: 234567 wynosi PLN 86.50
#
#
# Konto nr 765432: dokonano wpłat i wypłat opiewających na kwoty:
# PLN 12.50
# Aktualny stan konta nr: 765432 wynosi PLN 12.50
#
#
# Konto nr 678909: dokonano wpłat i wypłat opiewających na kwoty:
# PLN -2.70
# Aktualny stan konta nr: 678909 wynosi PLN 30.00
#
# Nie można wykonać operacji. Stan konta wynosi: PLN 30.00
#
# Process finished with exit code 0
