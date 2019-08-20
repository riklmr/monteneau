"""
get_measurements_wallonie.py

Uses chaudfontaine to actually retrieve measurement data and store it/them
in the PostgreSQL database.

Usage: change earliest_year to a recent year and start filling your DB.
Change earliest_year to earlier years as you need more/older data.
"""

import chaudfontaine
etl = chaudfontaine.Chaudfontaine()

# example combos:
# hauteur: 2536, 8221 (Gendron/Lesse, very old station)
# debit: 6526
# precipitation: 5649

## Donwload/update this specific station-year-month 
# etl.process_station_month(
#     station_type='hauteur', 
#     station_code=2536, 
#     year=None, 
#     month=None, 
#     want_covered=['bare', 'unknown', 'incomplete']
# )

## Update current month (in your local tz), for all Meuse stations
# for station_type in etl.QUANTITY_CODES.keys():
#    etl.process_meuse_month(
#        station_type=station_type, 
#        year=None, 
#        month=None, 
#        want_covered=['bare', 'unknown', 'incomplete']
#    )

# Download, for one station; the months (since earliest_year) that were not downloaded before
# etl.process_station_alltime(
#     station_type='debit', 
#     station_code=7863, 
#     earliest_year=2019, 
#     want_covered=['bare', 'unknown', 'incomplete']
# )

# Download, for all Meuse stations; the months (since earliest_year) that were not downloaded before or incomplete
for station_type in etl.QUANTITY_CODES.keys():
     etl.process_meuse_alltime(
         station_type=station_type, 
         earliest_year=2019,
         want_covered=['bare', 'unknown', 'incomplete'],
     )

# Download, for all Meuse stations; the months (since earliest_year) that were not downloaded before
# for station_type in etl.QUANTITY_CODES.keys():
#     etl.process_meuse_alltime(
#         station_type=station_type, 
#         earliest_year=2019,
#         want_covered=['bare', 'unknown'],
#     )

etl.data_coverage.save()

