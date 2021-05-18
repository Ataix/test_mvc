import eel
import model


eel.init('web')


@eel.expose
def create_currency(name, buy, sale):
    currency = model.Currency(name, buy, sale)
    print(currency)
    # return currency


eel.start('index.html', mode='safari')
