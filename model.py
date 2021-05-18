
class Currency:
    inflation = 0.10

    def __str__(self):
        return self.name + ' ' + str(self._buy) + ' ' + str(self.__sale)

    def __init__(self, name, buy, sale):
        self.name = name
        self._buy = buy
        self.__sale = sale

    def change_value(self, buy, sale):
        self._buy = buy
        self.__sale = sale

    @classmethod
    def change_inflation(cls, inflation):
        Currency.inflation = inflation

    @staticmethod
    def show_country_state():
        states = {'stable', 'danger', 'middle'}
        return states.pop()
