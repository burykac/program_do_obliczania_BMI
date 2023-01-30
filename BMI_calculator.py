class Zawodnik():
    def __init__(self, imie = "a", nazwisko = "b", wzrost = 1, waga = 1):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga

    def __str__(self):
        return f"{imie} {nazwisko} Twoje BMI wynosi: {(waga)/(wzrost**2)}."

w = Zawodnik()

print(w)