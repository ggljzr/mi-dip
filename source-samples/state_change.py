from sqlalchemy.event import listens_for

# funkce se provede při nastavení
# atributu state třídy Garage
@listens_for(Garage.state, 'set', named=True)
def send_notification(**kwargs):
    if kwargs['value'] == kwargs['oldvalue']:
        # pokud nedošlo ke změně hodnoty state
        # není třeba provádět žádnou akci
        return
    # stejně tak pokud je nový stav OK
    if kwargs['value'] == Garage.STATE_OK:
        return

    # odeslání SMS na čísla
    # nájemce a správce garáží