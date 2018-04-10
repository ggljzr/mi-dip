from apscheduler.schedulers.background import \
    BackgroundScheduler

# BackgroundScheduler běží v samostatném vlákně,
# neblokuje tedy webovou aplikaci
scheduler = BackgroundScheduler()

# přidání pravidelného úkolu do plánovače
# Garage.check_reports je statická metoda
# třídy Garage, která provede kontrolu hlášení
# u všech garáží v databázi (a případně upraví jejich stav)
scheduler.add_job(Garage.check_reports, 'interval', minutes=5)
scheduler.start()