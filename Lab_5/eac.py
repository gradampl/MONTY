class Konto:
    def __init__(self, imie, nazwisko, adres, nr_konta, stan_konta=0.0):
        self.stan_konta = stan_konta
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
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
                          'PLN {}'.format(self.stan_konta))
        except ValueError:
            self.__wrong_sum__()

    def __przelew_dane__(self, nr_konta, odbiorca, kwota, cel, in_out):

        def __odbiorca_nadawca__(inout):
            if inout == "in":
                napis = ' nadawcy: '
            else:
                napis = ' odbiorcy: '
            return napis

        print('\nNazwa' + __odbiorca_nadawca__(in_out), odbiorca.nazwa_cz1, odbiorca.nazwa_cz2)
        print('Adres' + __odbiorca_nadawca__(in_out), str(odbiorca.adres))
        print('Nr konta: ' + str(nr_konta))
        print('Tytułem: ' + str(cel))
        print('PLN ' + str(kwota) + '\n')

    def __przelew_wew__(self, nr_konta, odbiorca, kwota, cel, in_out):
        if self.__check_number__(nr_konta):
            if in_out == "out":
                if self.__wyplata__(kwota):
                    self.odbiorca = Odbiorca(self.adres, self.imie, self.nazwisko)
                    self.__przelew_dane__(nr_konta, self.odbiorca, kwota, cel, in_out)
            else:
                if self.__wyplata__(kwota):
                    self.odbiorca = Odbiorca(self.adres, self.imie, self.nazwisko)
                    self.__przelew_dane__(nr_konta, self.odbiorca, kwota, cel, in_out)

    def __przelew_zew__(self, nr_konta, odbiorca, kwota, cel, in_out):
        if self.__check_number__(nr_konta):
            if in_out == "out":
                if self.__wyplata__(kwota):
                    self.__przelew_dane__(nr_konta, odbiorca, kwota, cel, in_out)
            else:
                if self.__wplata__(kwota):
                    self.__przelew_dane__(nr_konta, odbiorca, kwota, cel, in_out)

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
        print('\nKonto nr %d: dokonano wpłat i wypłat opiewających na kwoty:' % self.nr_konta)
        while i >= 0:
            print('PLN %.2f' % self.operacje.pop())
            i -= 1
        self.__aktualny_stan_konta__()


class Odbiorca:
    def __init__(self, adres, nazwa_cz1, nazwa_cz2=''):
        self.nazwa_cz1 = nazwa_cz1
        self.nazwa_cz2 = nazwa_cz2
        self.adres = adres


konto1 = Konto("Włodzimierz", "Bednarek", "Dębowa 4, 20-123 Niepołomice", 234567)
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
konto1.__przelew_wew__(12345j, Odbiorca("", ""), 19, "przesunięcie środków na konto oszczędnościowe", "out")
konto1.__przelew_wew__(123321, Odbiorca("", ""), 19, "przesunięcie środków na konto oszczędnościowe", "out")
konto1.__aktualny_stan_konta__()
konto1.__przelew_zew__(234567, Odbiorca("Muniowicza 17, Szkaplerzyce", 'SM "Raj Lokatora"')
                       , 90, "czynsz za maj 2020", "out")
konto1.__aktualny_stan_konta__()

konto2 = Konto("Mada", "Wiszniewska", "Kwiatowa 1, Domaniewice", 765432)
konto1.__przelew_zew__(765432, Odbiorca(konto2.adres, konto2.imie, konto2.nazwisko), 12.50, "za ręczniki", "out")
konto2.__przelew_zew__(234567, Odbiorca(konto1.adres, konto1.imie, konto1.nazwisko), 12.50, "za ręczniki", "in")
konto3 = Konto("Walery", "Stef", "Chrząszczyrzewoszyce Wielkie 13", 678909, 32.70)
konto3.__przelew_wew__(678910, '', 2.70, "założenie lokaty terminowej", "out")
konto2.__aktualny_stan_konta__()
konto3.__aktualny_stan_konta__()

konto1.__podsumowanie__()
konto2.__podsumowanie__()
konto3.__podsumowanie__()

# Result:
#
# Aktualny stan konta nr: 234567 wynosi PLN 0.00
# Nieprawidłowy format kwoty.
# Nieprawidłowy format kwoty.
# Aktualny stan konta nr: 234567 wynosi PLN 10.00
# Nie można wykonać operacji. Stan konta wynosi: PLN 10.0
# Aktualny stan konta nr: 234567 wynosi PLN 200.00
# Aktualny stan konta nr: 234567 wynosi PLN 189.00
# Nieprawidłowy numer konta
#
# Nazwa odbiorcy:  Włodzimierz Bednarek
# Adres odbiorcy:  Dębowa 4, 20-123 Niepołomice
# Nr konta: 123321
# Tytułem: przesunięcie środków na konto oszczędnościowe
# PLN 19
#
# Aktualny stan konta nr: 234567 wynosi PLN 170.00
#
# Nazwa odbiorcy:  SM "Raj Lokatora"
# Adres odbiorcy:  Muniowicza 17, Szkaplerzyce
# Nr konta: 234567
# Tytułem: czynsz za maj 2020
# PLN 90
#
# Aktualny stan konta nr: 234567 wynosi PLN 80.00
#
# Nazwa odbiorcy:  Mada Wiszniewska
# Adres odbiorcy:  Kwiatowa 1, Domaniewice
# Nr konta: 765432
# Tytułem: za ręczniki
# PLN 12.5
#
#
# Nazwa nadawcy:  Włodzimierz Bednarek
# Adres nadawcy:  Dębowa 4, 20-123 Niepołomice
# Nr konta: 234567
# Tytułem: za ręczniki
# PLN 12.5
#
#
# Nazwa odbiorcy:  Walery Stef
# Adres odbiorcy:  Chrząszczyrzewoszyce Wielkie 13
# Nr konta: 678910
# Tytułem: założenie lokaty terminowej
# PLN 2.7
#
# Aktualny stan konta nr: 765432 wynosi PLN 12.50
# Aktualny stan konta nr: 678909 wynosi PLN 30.00
#
# Konto nr 234567: dokonano wpłat i wypłat opiewających na kwoty:
# PLN -12.50
# PLN -90.00
# PLN -19.00
# PLN -11.00
# PLN 190.00
# PLN 10.00
# Aktualny stan konta nr: 234567 wynosi PLN 67.50
#
# Konto nr 765432: dokonano wpłat i wypłat opiewających na kwoty:
# PLN 12.50
# Aktualny stan konta nr: 765432 wynosi PLN 12.50
#
# Konto nr 678909: dokonano wpłat i wypłat opiewających na kwoty:
# PLN -2.70
# Aktualny stan konta nr: 678909 wynosi PLN 30.00
#
# Process finished with exit code 0
