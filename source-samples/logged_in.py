# app_client je testovací klient Flask aplikace
# získaný pomocí metody test_client()
def set_logged_in(app_client, value):
    with app_client as c:
        with c.session_transaction() as s:
            s['logged_in'] = value