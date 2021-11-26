#● Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
#○ __init__ : instanțiem numărător și numitor
#○ __str__ : afisam "numărător/numitor"
#○ __add__ : returnam o noua fractie care reprezinta adunarea
#○ __sub__: returnam o nouă fracție care reprezinta scădearea
#○ inverse: returnează o nouă fracție (inversa frac

class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'Fractie({self.numarator}, '/', {self.numitor})'

    def __add__(self, other):
        adunare = self.numarator + self.numitor
        return Fractie(adunare)

    def __sub__(self, other):
        scadere = self.numarator - self.numitor
        return Fractie(scadere)

    def __next__(self):
        return self.numitor/self.numarator

