from flask import Blueprint, render_template

from .models.garage import Garage 

# deklarace blueprintu mod_main
mod_main = Blueprint('main', __name__)

# URL a příslušná akce jsou definovány
# vzhledem k blueprintu
@mod_main.route('/')
@login_required # kontrola přihlášení uživatele
def index():
    # získání údajů o všech garážích
    garages = Garage.query.all()

    # vygenerování stránky pomocí Jinja
    # zobrazovaná data jsou předána jako
    # parametry funkce render_template()
    return render_template('main/index.html', 
                            garages=garages, 
                            reg_mode=Garage.reg_mode)