from sqlalchemy.event import listens_for

# funkce se provede při nastavení
# atributu state třídy Garage
@listens_for(Garage.state, 'set', named=True)
def send_notification(**kwargs):
    # pokud nedošlo ke změně hodnoty state
    # není třeba provádět žádnou akci
    if kwargs['value'] == kwargs['oldvalue']:
        return
    # stejně tak pokud je nový stav OK
    if kwargs['value'] == Garage.STATE_OK:
        return

    # odeslání SMS na čísla
    # nájemce a správce garáží