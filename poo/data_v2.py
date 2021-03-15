class Data:
    # Construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)

print(d1.to_str())
