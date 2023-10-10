
class Data:

    def __init__(self, dia, mes, ano):
        print("Calendário...".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("Data formata - {} / {} / {}".format(self.dia, self.mes, self.ano))

