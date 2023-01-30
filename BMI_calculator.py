class Zawodnik():
    def __init__(self, imie = "a", nazwisko = "b", wzrost = 1, waga = 1):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga

    def __str__(self):
        return f"{self.imie} {self.nazwisko} Twoje BMI wynosi: {(self.waga)/(self.wzrost**2)}."

def obliczanie_BMI():
    decyzja = input("A - oblicz BMI zawodnika/zawodniczki, B - wyjdź: ")
    while(True):
        if(decyzja == "A" or decyzja == "a"):
            imie = str(input("Podaj imię: "))
            nazwisko = str(input("Podaj nazwisko: "))
            wzrost = float(input("Podaj wzrost w metrach: "))
            waga = float(input("Podaj wagę w kilogramach: "))
            print(Zawodnik(imie, nazwisko, wzrost, waga))
        else:
            break

obliczanie_BMI()