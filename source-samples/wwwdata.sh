# nastavení vlastníka souboru na 
# uživatele www-data ze skupiny www-data
$ sudo chown www-data:www-data /cesta/k/user_config.ini
$ sudo chown www-data:www-data /cesta/k/app.db
# povolení čtení a zápisu souborů vlastníkovi
# vlastníkovi a skupině
$ sudo chmod 660 /cesta/k/user_config.ini
$ sudo chmod 660 /cesta/k/app.db
