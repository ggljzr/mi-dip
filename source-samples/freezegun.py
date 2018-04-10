from freezegun import freeze_time

# všechna volání datetime.datetime.now()
# pocházející z této funkce vrátí
# hodnotu 2011-01-01 00:00:00
@freeze_time("2011-01-01 00:00:00")
def test_check_report(garage):
    new_garage = garage.add_garage()
    new_garage.period = 60 # explicitní nastavení periody
    new_garage.add_report_event()
    new_garage.check_report()

    assert new_garage.state == garage.STATE_OK

    # nastavení návratové hodnoty funkce now()
    # v rámci bloku with
    with freeze_time("2011-01-01 02:00:00"):
        new_garage.check_report()
        assert new_garage.state == garage.STATE_NOT_RESPONDING